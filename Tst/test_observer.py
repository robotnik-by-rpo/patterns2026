import os
from Src.Logics.observer import observer
from Src.Logics.logger_observer import logger_observer
from Src.Core.event_type import event_type
from Src.Logics.settings_manager import setting_manager
from Src.Logics.storage_manager import storage_manager
from fastapi import FastAPI
from starlette.testclient import TestClient
from Src.API.router import server_API


LOG_FILE = "test_observer.log"


def _reset_observer_and_log():
    """Preparation helper: clean handlers and log file"""
    observer.handlers.clear()
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    logger_observer(LOG_FILE)


def test_logger_observer_writes_event():
    """Check logger_observer writes event to file"""
    # Preparation
    _reset_observer_and_log()

    # Action
    observer.create(event_type.load_settings(), {"file": "settings.json"})

    # Verification
    assert os.path.exists(LOG_FILE)
    content = open(LOG_FILE, encoding="utf-8").read()
    assert "load_settings" in content
    assert "settings.json" in content


def test_observer_add_duplicate_ignored():
    """Check the same observer is not added twice"""
    # Preparation
    observer.handlers.clear()
    log = logger_observer(LOG_FILE)

    # Action
    observer.add(log)
    count = len(observer.handlers)

    # Verification
    assert count == 1


def test_settings_load_creates_log_event():
    """Check load settings publishes event into log"""
    # Preparation
    _reset_observer_and_log()
    manager = setting_manager()

    # Action
    manager.load("settings.json")

    # Verification
    content = open(LOG_FILE, encoding="utf-8").read()
    assert "load_settings" in content or "change_settings" in content


def test_storage_init_creates_log_events():
    """Check domain init publishes events into log"""
    # Preparation
    _reset_observer_and_log()

    # Action
    storage_manager().reset()

    # Verification
    content = open(LOG_FILE, encoding="utf-8").read()
    assert "initing_units" in content or "updating_units" in content


def test_web_post_domain_creates_log_event():
    """Check CRUD POST publishes web and domain events"""
    # Preparation
    _reset_observer_and_log()
    storage_manager().reset()
    app = FastAPI()
    app.include_router(server_API().api)
    client = TestClient(app)
    payload = {
        "__class__": "group_nomenclature_model",
        "id": "obs_test_group_001",
        "name": "observer_test_group",
    }

    # Action
    response = client.post("/api/domain", json=payload)

    # Verification
    assert response.status_code == 201
    content = open(LOG_FILE, encoding="utf-8").read()
    assert "web_POST" in content or "posting_group_nomenclature_model" in content