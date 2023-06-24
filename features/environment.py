import requests
from utilities.configuration import getconfig
from utilities.resources import ApiResources

def after_scenario(context, scenario):
    if "library" in scenario.tags:
        url = getconfig()['API']['endpoint']+ApiResources.deleteBook
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        response_delete = requests.post(url,json={"ID" : context.bookid},headers=headers,)
        assert response_delete.status_code == 200
        res_json = response_delete.json()
        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"