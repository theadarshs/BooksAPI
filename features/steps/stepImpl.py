import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configuration import *

@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    context.payLoad = addBookPayload("sfhfhf","76845");

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )

@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookid = response_json['ID']
    print(context.bookid)
    assert response_json["Msg"] == "successfully added"

@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getconfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    context.payLoad = addBookPayload(isbn,aisle);

@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('theadarshs', 'Cardano@11')
    #import warnings
    #warnings.filterwarnings('ignore', message='Unverified HTTPS request')

@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubrepo)

@then('status code of response should be {statuscode:d}')
def step_impl(context,statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode


