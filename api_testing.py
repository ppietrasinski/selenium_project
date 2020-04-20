import requests

url = 'https://jsonplaceholder.typicode.com/users/'
# resp = requests.get()

# resp = requests.get('https://todolist.example.com/tasks/')
# resp = requests.get(url)
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise Exception('GET /names/ {}'.format(resp.status_code))
# for todo_item in resp.json():
#     print('id {} has name {}'.format(todo_item['id'], todo_item['name']))


json_file = {"name": "Pawel Test", "username": "Test", "email": "test.email@email.com"}
resp = requests.post(url, json=json_file)
print(resp.status_code)
# print(resp.json())