import allure


@allure.feature("Products API")
@allure.story("List products")
@allure.title("GET /products returns a paginated list of products")
def test_get_all_products(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/products", params={"limit": 5})

    assert response.status_code == 200

    body = response.json()
    assert body["limit"] == 5
    assert len(body["products"]) == 5
    assert body["total"] > 0


@allure.feature("Products API")
@allure.story("Get single product")
@allure.title("GET /products/{id} returns the matching product")
def test_get_single_product(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/products/1")

    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 1
    assert "title" in product
    assert "price" in product


@allure.feature("Products API")
@allure.story("Get single product")
@allure.title("GET /products/{id} returns 404 for a non-existent product")
def test_get_nonexistent_product(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/products/999999")

    assert response.status_code == 404
    assert "not found" in response.json()["message"].lower()


@allure.feature("Products API")
@allure.story("Search products")
@allure.title("GET /products/search respects the limit and returns a total")
def test_search_products(api_client, api_base_url):
    response = api_client.get(
        f"{api_base_url}/products/search",
        params={"q": "phone", "limit": 3},
    )

    assert response.status_code == 200

    body = response.json()
    assert len(body["products"]) <= 3
    assert body["total"] > 0


@allure.feature("Products API")
@allure.story("Search products")
@allure.title("GET /products/search returns an empty list for a query with no matches")
def test_search_products_no_match(api_client, api_base_url):
    response = api_client.get(
        f"{api_base_url}/products/search",
        params={"q": "zzzzzz-no-such-product"},
    )

    assert response.status_code == 200

    body = response.json()
    assert body["products"] == []
    assert body["total"] == 0


@allure.feature("Products API")
@allure.story("List products")
@allure.title("GET /products respects skip and limit for pagination")
def test_get_products_pagination(api_client, api_base_url):
    first_page = api_client.get(
        f"{api_base_url}/products", params={"limit": 5, "skip": 0}
    ).json()
    second_page = api_client.get(
        f"{api_base_url}/products", params={"limit": 5, "skip": 5}
    ).json()

    first_ids = {product["id"] for product in first_page["products"]}
    second_ids = {product["id"] for product in second_page["products"]}

    assert first_page["skip"] == 0
    assert second_page["skip"] == 5
    assert first_ids.isdisjoint(second_ids)


@allure.feature("Products API")
@allure.story("Categories")
@allure.title("GET /products/categories returns a non-empty list of category slugs")
def test_get_product_categories(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/products/categories")

    assert response.status_code == 200

    categories = response.json()
    assert len(categories) > 0
    assert all("slug" in category for category in categories)


@allure.feature("Products API")
@allure.story("Categories")
@allure.title("GET /products/category/{category} returns only products from that category")
def test_get_products_by_category(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/products/category/beauty")

    assert response.status_code == 200

    body = response.json()
    assert body["total"] > 0
    assert all(product["category"] == "beauty" for product in body["products"])


@allure.feature("Products API")
@allure.story("Add product")
@allure.title("POST /products/add creates a new product")
def test_add_product(api_client, api_base_url):
    payload = {"title": "Test Product"}

    response = api_client.post(f"{api_base_url}/products/add", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


@allure.feature("Products API")
@allure.story("Update product")
@allure.title("PUT /products/{id} updates the given fields")
def test_update_product(api_client, api_base_url):
    payload = {"title": "Updated Title"}

    response = api_client.put(f"{api_base_url}/products/1", json=payload)

    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 1
    assert product["title"] == payload["title"]


@allure.feature("Products API")
@allure.story("Delete product")
@allure.title("DELETE /products/{id} marks the product as deleted")
def test_delete_product(api_client, api_base_url):
    response = api_client.delete(f"{api_base_url}/products/1")

    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 1
    assert product["isDeleted"] is True
    assert "deletedOn" in product
