import allure


@allure.feature("Auth API")
@allure.story("Login")
@allure.title("POST /auth/login succeeds with valid credentials")
def test_login_success(api_client, api_base_url):
    payload = {"username": "emilys", "password": "emilyspass"}

    response = api_client.post(f"{api_base_url}/auth/login", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body["username"] == payload["username"]
    assert "accessToken" in body


@allure.feature("Auth API")
@allure.story("Login")
@allure.title("POST /auth/login fails with invalid credentials")
def test_login_invalid_credentials(api_client, api_base_url):
    payload = {"username": "emilys", "password": "wrong-password"}

    response = api_client.post(f"{api_base_url}/auth/login", json=payload)

    assert response.status_code == 400
    assert "invalid credentials" in response.json()["message"].lower()


@allure.feature("Auth API")
@allure.story("Current user")
@allure.title("GET /auth/me returns the logged-in user for a valid access token")
def test_get_current_user_with_valid_token(api_client, api_base_url):
    login_response = api_client.post(
        f"{api_base_url}/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
    )
    access_token = login_response.json()["accessToken"]

    response = api_client.get(
        f"{api_base_url}/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200
    assert response.json()["username"] == "emilys"


@allure.feature("Auth API")
@allure.story("Current user")
@allure.title("GET /auth/me is rejected without an access token")
def test_get_current_user_without_token(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/auth/me")

    assert response.status_code == 401
    assert "token" in response.json()["message"].lower()
