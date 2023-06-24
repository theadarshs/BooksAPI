import requests
from utilities.resources import *
import configparser
from payLoad import *
from utilities.configuration import *

#Add Book

url = getconfig()['API']['endpoint']+ApiResources.addBook
headers = {'Content-Type': 'application/json;charset=UTF-8'}
response = requests.post(url,json=addBookPayload("fefrewd"),headers=headers,)
print(response.json())
response_json = response.json()
print(type(response.json()))
bookid = response_json['ID']
print(bookid)

#delete book

url = getconfig()['API']['endpoint']+ApiResources.deleteBook
headers = {'Content-Type': 'application/json;charset=UTF-8'}
response_delete = requests.post(url,json={"ID" : bookid},headers=headers,)
assert response_delete.status_code == 200
res_json = response_delete.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

#authentication
se = requests.session()
se.auth = auth=('theadarshs','Cardano@11')
url = "https://api.github.com/user"
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

github_response = requests.get(url,verify=False,auth=('theadarshs','Cardano@11'))

print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response= se.get(url2)
print(response.status_code)




















