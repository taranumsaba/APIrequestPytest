# test_gorest_api.py
import pytest

class TestGorest:
    var_id = None
    def test_create_user(self, api_client):
        new_user = {
            "name": "mary",
            "gender": "male",
            "email": "marynew@gmail.com",
            "status": "active"
        }
        response = api_client.post(f"{api_client.base_url}/users", json=new_user)
        data = response.json()
        print(data)
        TestGorest.var_id = data.get("id")
        assert response.status_code == 201
        assert response.json()["name"] == new_user["name"]
        assert response.json()["email"] == new_user["email"]

    def test_get_users(self, api_client):
        response = api_client.get(f"{api_client.base_url}/users")
        print(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_get_user_by_id(self, api_client):
        user_id = TestGorest.var_id# Replace with a valid user ID
        response = api_client.get(f"{api_client.base_url}/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["id"] == user_id

    def test_update_user(self, api_client):
        user_id = TestGorest.var_id  # Replace with a valid user ID
        updated_user = {
            "name": "mary_updated",
            "email": "mary123@gmail.com",
            "status": "inactive"
        }
        response = api_client.put(f"{api_client.base_url}/users/{user_id}", json=updated_user)
        print(response.json())
        assert response.status_code == 200
        assert response.json()["name"] == updated_user["name"]
        assert response.json()["email"] == updated_user["email"]

    def test_delete_user(self,api_client):
        user_id = TestGorest.var_id  # Replace with a valid user ID
        response = api_client.delete(f"{api_client.base_url}/users/{user_id}")
        print(response.status_code)
        assert response.status_code == 204
