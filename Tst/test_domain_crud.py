from fastapi import FastAPI
from starlette.testclient import TestClient
from Src.API.router import server_API
from Src.Logics.storage_manager import storage_manager

app = FastAPI()
app.include_router(server_API().api)

client = TestClient(app)

def test_crud_create_group_success():
    """Check successful creation of a new group_nomenclature_model"""
    # Preparation
    storage_manager().reset()
    payload = {
        "__class__": "group_nomenclature_model",
        "id": "test_group_id_123",
        "name": "test_sweets"
    }

    # Action
    response = client.post("/api/domain", json=payload)

    # verification
    assert response.status_code == 201
    data = response.json()
    assert data["__class__"] == "group_nomenclature_model"
    assert data["name"] == "test_sweets"
    assert data["id"] == "test_group_id_123"


def test_crud_create_duplicate_error():
    """Check error when trying to create a group with an existing name"""
    # Preparation
    storage_manager().reset()
    payload = {
        "__class__": "group_nomenclature_model",
        "name": "ingredients",
    }

    # Action
    response = client.post("/api/domain", json=payload)

    # verification
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_crud_read_success():
    """Check successful reading of a domain entity by name"""
    # Preparation
    storage_manager().reset()
    
    # Action
    response = client.get("/api/domain/order")

    # verification
    assert response.status_code == 200
    data = response.json()
    assert data["__class__"] == "group_nomenclature_model"
    assert data["name"] == "order"


def test_crud_read_not_found():
    """Check reading of a non-existent domain entity"""
    # Preparation
    storage_manager().reset()

    # Action
    response = client.get("/api/domain/does_not_exist_999")

    # verification
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_crud_update_success():
    """Check successful update (PUT) of an existing domain entity"""
    # Preparation
    storage_manager().reset()
    payload = {
        "__class__": "group_nomenclature_model",
        "id": "update_group_id_456",
        "name": "to_be_updated"
    }
    client.post("/api/domain", json=payload)
    
    updated_payload = {
        "__class__": "group_nomenclature_model",
        "id": "update_group_id_456",
        "name": "updated_name"
    }

    # Action
    response = client.put("/api/domain/update_group_id_456", json=updated_payload)

    # verification
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "updated_name"
    
    get_old = client.get("/api/domain/to_be_updated")
    assert get_old.status_code == 404


def test_crud_update_referenced_error():
    """Check error when trying to update a referenced entity"""
    # Preparation
    storage_manager().reset()
    payload = {
        "__class__": "group_nomenclature_model",
        "name": "new_ingredients_name"
    }

    # Action
    response = client.put("/api/domain/ingredients", json=payload)

    # verification
    assert response.status_code == 400
    assert "entity is referenced by another entity" in response.json()["detail"]


def test_crud_delete_success():
    """Check successful deletion of an unreferenced entity"""
    # Preparation
    storage_manager().reset()
    payload = {
        "__class__": "group_nomenclature_model",
        "id": "delete_group_id_789",
        "name": "to_be_deleted"
    }
    client.post("/api/domain", json=payload)

    # Action
    response = client.delete("/api/domain/delete_group_id_789")

    # verification
    assert response.status_code == 204
    
    get_response = client.get("/api/domain/delete_group_id_789")
    assert get_response.status_code == 404


def test_crud_delete_referenced_error():
    """Check error when trying to delete a referenced entity"""
    # Preparation
    storage_manager().reset()
    
    # Action
    response = client.delete("/api/domain/gram")

    # verification
    assert response.status_code == 409
    assert "entity is referenced by another entity" in response.json()["detail"]


def test_crud_delete_force_success():
    """Check forced deletion of a referenced entity"""
    # Preparation
    storage_manager().reset()
    
    # Action
    response = client.delete("/api/domain/gram?force=true")

    # verification
    assert response.status_code == 204
    
    get_response = client.get("/api/domain/gram")
    assert get_response.status_code == 404  

def test_crud_delete_referenced_error():
    """Check error when trying to delete a referenced entity"""
    # Preparation
    storage_manager().reset()
    
    # Action
    response = client.delete("/api/domain/gram")
    
    # verification
    assert response.status_code == 409

def test_crud_patch_success():
    """Check successful partial update (PATCH) of an existing domain entity"""
    # Preparation
    storage_manager().reset()
    
    payload = {
        "__class__": "group_nomenclature_model",
        "id": "patch_group_id_999",
        "name": "original_patch_name"
    }
    create_response = client.post("/api/domain", json=payload)
    assert create_response.status_code == 201

    patch_payload = {
        "name": "patched_name"
    }

    # Action
    response = client.patch("/api/domain/patch_group_id_999", json=patch_payload)

    # verification
    assert response.status_code == 200
    data = response.json()
    
    assert data["name"] == "patched_name"
    
    assert data["id"] == "patch_group_id_999"
    assert data["__class__"] == "group_nomenclature_model"

    get_old = client.get("/api/domain/original_patch_name")
    assert get_old.status_code == 404

    get_new = client.get("/api/domain/patched_name")
    assert get_new.status_code == 200