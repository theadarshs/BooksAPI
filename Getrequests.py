import json
import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php?',
             params={'AuthorName':'Rahul Shetty2'},)

#print(response.text)
#print(type(response.text))
#dict_response = json.loads(response.text)
#print((dict_response[0]['isbn']))
json_response = response.json()
print(type(json_response))
print(json_response)
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
#retrive the book details with isbn RGHCC
for actualbook in json_response:
    if actualbook['isbn']== 'bnid34':
        print(actualbook)
        break
expectedbook = {
    'book_name': 'Devops',
    'isbn': 'bnid34',
    'aisle': '89'
    }
assert actualbook == expectedbook