import requests


def _make_request(base_url, api_key, method, path, **kwargs):
    url = f"{base_url}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    return requests.request(method, url, headers=headers, timeout=10, **kwargs)

# --- POST /api-v2/projects ---


def test_create_project_positive(base_url, api_key, unique_title):
    """Позитивный: создание проекта должно вернуть 201 OK"""
    path = "/api-v2/projects"
    payload = {"title": unique_title}
    resp = _make_request(base_url, api_key, "POST", path, json=payload)

    assert resp.status_code == 201


def test_create_project_negative_empty_title(base_url, api_key):
    """Негативный: пустой title должен вызвать ошибку валидации (400)"""
    path = "/api-v2/projects"
    payload = {"title": ""}
    resp = _make_request(base_url, api_key, "POST", path, json=payload)

    assert resp.status_code == 400
    error_data = resp.json()
    assert "error" in error_data

# --- GET /api-v2/projects/{id} ---


def test_get_project_positive(base_url, api_key, created_project_id):
    """Позитивный: получение существующего проекта должно вернуть 200 OK"""
    path = f"/api-v2/projects/{created_project_id}"
    resp = _make_request(base_url, api_key, "GET", path)

    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == created_project_id


def test_get_project_negative_not_found(base_url, api_key):
    """Негативный: получение несуществующего проекта должно вернуть 404"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    path = f"/api-v2/projects/{fake_id}"
    resp = _make_request(base_url, api_key, "GET", path)

    assert resp.status_code == 404
    error_data = resp.json()
    assert "error" in error_data

# --- PUT /api-v2/projects/{id} ---


def test_update_project_positive(base_url, api_key, created_project_id):
    """Позитивный: обновление проекта должно вернуть 200 OK"""
    new_title = f"UPDATED_{created_project_id[:8]}"
    path = f"/api-v2/projects/{created_project_id}"
    payload = {"title": new_title}
    resp = _make_request(base_url, api_key, "PUT", path, json=payload)

    assert resp.status_code == 200


def test_update_project_negative_not_found(base_url, api_key):
    """Негативный: обновление несуществующего проекта должно вернуть 404"""
    fake_id = "ffffffff-ffff-ffff-ffff-ffffffffffff"
    path = f"/api-v2/projects/{fake_id}"
    payload = {"title": "This will never update"}
    resp = _make_request(base_url, api_key, "PUT", path, json=payload)

    assert resp.status_code == 404
    error_data = resp.json()
    assert "error" in error_data
