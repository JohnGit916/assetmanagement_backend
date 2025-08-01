def test_register_and_login(client):
    # Register
    res = client.post("/api/auth/register", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "test123"
    })
    assert res.status_code == 201

    # Login
    res = client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "test123"
    })
    assert res.status_code == 200
    assert "access_token" in res.get_json()
