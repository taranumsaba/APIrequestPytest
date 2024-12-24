# import pytest
# from Config.config import UserData
#
# def test_get_posts(api_client):
#     response = api_client.get(f"{UserData.Base_url}/posts")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert len(response.json()) > 0
#
# def test_get_post_by_id(api_client):
#     post_id = 1
#     response = api_client.get(f"{UserData.Base_url}/posts/{post_id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == post_id
#
# def test_create_post(api_client):
#     new_post = {
#         "title": "foo",
#         "body": "bar",
#         "userId": 1
#     }
#     response = api_client.post(f"{UserData.Base_url}/posts", json=new_post)
#     assert response.status_code == 201
#     assert response.json()["title"] == new_post["title"]
#     assert response.json()["body"] == new_post["body"]
#     assert response.json()["userId"] == new_post["userId"]
#
# def test_update_post(api_client):
#     post_id = 1
#     updated_post = {
#         "id": post_id,
#         "title": "updated title",
#         "body": "updated body",
#         "userId": 1
#     }
#     response = api_client.put(f"{UserData.Base_url}/posts/{post_id}", json=updated_post)
#     assert response.status_code == 200
#     assert response.json()["title"] == updated_post["title"]
#     assert response.json()["body"] == updated_post["body"]
#
# def test_delete_post(api_client):
#     post_id = 1
#     response = api_client.delete(f"{UserData.Base_url}/posts/{post_id}")
#     assert response.status_code == 200
#     assert response.json() == {}
