import allure


@allure.feature("Carts API")
@allure.story("List carts")
@allure.title("GET /carts returns a paginated list of carts")
def test_get_all_carts(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/carts", params={"limit": 5})

    assert response.status_code == 200

    body = response.json()
    assert body["limit"] == 5
    assert len(body["carts"]) == 5
    assert body["total"] > 0


@allure.feature("Carts API")
@allure.story("Get single cart")
@allure.title("GET /carts/{id} returns the matching cart with computed totals")
def test_get_single_cart(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/carts/1")

    assert response.status_code == 200

    cart = response.json()
    assert cart["id"] == 1
    assert cart["totalProducts"] == len(cart["products"])
    assert cart["total"] > 0


@allure.feature("Carts API")
@allure.story("Add cart")
@allure.title("POST /carts/add creates a cart with the correct totals")
def test_add_cart(api_client, api_base_url):
    payload = {"userId": 1, "products": [{"id": 1, "quantity": 2}]}

    response = api_client.post(f"{api_base_url}/carts/add", json=payload)

    assert response.status_code == 201

    cart = response.json()
    assert cart["userId"] == payload["userId"]
    assert cart["totalQuantity"] == 2
    assert cart["products"][0]["id"] == 1
