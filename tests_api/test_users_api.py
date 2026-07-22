import allure


@allure.feature("Users API")
@allure.story("List users")
@allure.title("GET /users returns a paginated list of users")
def test_get_all_users(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/users", params={"limit": 5})

    assert response.status_code == 200

    body = response.json()
    assert body["limit"] == 5
    assert len(body["users"]) == 5
    assert body["total"] > 0


@allure.feature("Users API")
@allure.story("Get single user")
@allure.title("GET /users/{id} returns the matching user")
def test_get_single_user(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/users/1")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert "email" in user
    assert "username" in user


@allure.feature("Users API")
@allure.story("Get single user")
@allure.title("GET /users/{id} returns 404 for a non-existent user")
def test_get_nonexistent_user(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/users/999999")

    assert response.status_code == 404
    assert "not found" in response.json()["message"].lower()


@allure.feature("Users API")
@allure.story("Search users")
@allure.title("GET /users/search only returns users matching the query")
def test_search_users(api_client, api_base_url):
    response = api_client.get(
        f"{api_base_url}/users/search", params={"q": "John"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["total"] > 0
    assert all(
        "john" in f"{user['firstName']} {user['lastName']}".lower()
        for user in body["users"]
    )
