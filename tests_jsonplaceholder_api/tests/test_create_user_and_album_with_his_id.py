from tests_jsonplaceholder_api.tests import test_methods as tm

def test_create_user_and_album_with_his_id():
    res_new_user = tm.create_new_user()
    id = res_new_user.json()['id']
    assert res_new_user.status_code == 201

    res_new_post = tm.add_post_by_user_with_id(id)
    assert res_new_post.status_code == 201
    print(res_new_post.json())



