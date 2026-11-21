from fastapi import FastAPI
from starlette.testclient import TestClient
from Src.API.router import server_API
from Src.Logics.storage_manager import storage_manager

app = FastAPI()
app.include_router(server_API().api)

client = TestClient(app)

def test_filter_domain_by_name_success():
    """Check filtering domain entities by name with LIKE"""
    # Preparation
    storage_manager().reset()
    payload = {
        "filters": [
            {
                "field_name": "name",
                "filter_type": "LIKE",
                "value": "flour"
            }
        ]
    }

    # Action
    response = client.post("/api/domain/filter/nomenclature_model", json=payload)

    # Verification
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for item in data:
        assert "flour" in item["name"].lower()


def test_filter_domain_nested_unit_success():
    """Check filtering domain entities by nested base_unit.name"""
    # Preparation
    storage_manager().reset()
    payload = {
        "filters": [
            {
                "field_name": "base_unit.name",
                "filter_type": "EQUALS",
                "value": "kilogram"
            }
        ]
    }

    # Action
    response = client.post("/api/domain/filter/nomenclature_model", json=payload)

    # Verification
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for item in data:
        assert item["base_unit"]["name"] == "kilogram"


def test_filter_domain_unknown_type_error():
    """Check error when filtering by unknown domain type"""
    # Preparation
    storage_manager().reset()
    payload = {
        "filters": [
            {
                "field_name": "name",
                "filter_type": "LIKE",
                "value": "flour"
            }
        ]
    }

    # Action
    response = client.post("/api/domain/filter/unknown_model", json=payload)

    # Verification
    assert response.status_code == 500
    assert "Unknown domain type" in response.json()["detail"]


def test_osv_report_by_nomenclature_success():
    """Check OSV report generation with filter by nomenclature name"""
    # Preparation
    storage_manager().reset()
    payload = {
        "filters": [
            {
                "field_name": "name",
                "filter_type": "LIKE",
                "value": "flour"
            }
        ]
    }

    # Action
    response = client.post("/api/domain/osv/nomenclature_model", json=payload)

    # Verification
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for item in data:
        assert "id" in item
        assert "name" in item
        assert "opening_balance" in item
        assert "income" in item
        assert "expense" in item
        assert "closing_balance" in item
        assert "flour" in item["name"].lower()
        assert item["closing_balance"] == (
            item["opening_balance"] + item["income"] - item["expense"]
        )


def test_osv_report_all_items_without_filter():
    """Check OSV report generation without filter returns all objects"""
    # Preparation
    storage_manager().reset()
    
    # Action
    response = client.post("/api/domain/osv/group_nomenclature_model", json={})

    # Verification
    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0
    for item in data:
        assert "name" in item
        assert item["closing_balance"] == (
            item["opening_balance"] + item["income"] - item["expense"]
        )