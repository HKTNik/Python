import os
import uuid
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com")


@pytest.fixture(scope="session")
def api_key():
    key = os.getenv("YOUGILE_API_KEY")
    if not key:
        pytest.skip(
            "Требуется переменная окружения YOUGILE_API_KEY для запуска тестов"
        )
    return key


@pytest.fixture
def unique_title():
    suffix = uuid.uuid4().hex[:6]
    return f"TEST_AUTO_{suffix}"


@pytest.fixture
def created_project_id(base_url, api_key, unique_title):
    url = f"{base_url}/api-v2/projects"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {"title": unique_title}

    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    assert resp.status_code == 201, f"Не удалось создать проект: {resp.text}"

    data = resp.json()
    project_id = data["id"]
    yield project_id
