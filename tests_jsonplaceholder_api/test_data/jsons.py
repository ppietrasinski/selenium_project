from tests_kurs_selenium.test_data import test_data as td

def create_json_add_new_user():
    data = td.generate_all_data()
    return {
        "name": data['full name'],
        "username": data['name'] + 'User',
        "email": data['email']
    }

def create_post_by_user_json(id):
    return {
        "userId": str(id),
        "title": "test title",
        "body": "test message test message test message"
    }