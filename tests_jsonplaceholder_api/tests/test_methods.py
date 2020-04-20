import requests
import tests_jsonplaceholder_api.test_data.endpoints as ep
import tests_jsonplaceholder_api.test_data.jsons as js

def create_new_user():
    json = js.create_json_add_new_user()
    url = ep.url + ep.users_endpoint
    return requests.post(url, json)

def add_post_by_user_with_id(id):
    json = js.create_post_by_user_json(id)
    url = ep.url + ep.posts_endpoint
    return requests.post(url, json)
