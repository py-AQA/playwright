import pytest
from playwright.sync_api import Page
import json
import csv
import os


def save_json(data, filename: str):
    with open(filename, 'w') as file:
        json.dump(data, file)
    assert os.path.exists(filename), "File was not created successfully"
    return filename


def read_json(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def save_csv(data, filename: str):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["uuid"])
        for uuid in data:
            writer.writerow([uuid])
    csvfile.close()


@pytest.fixture()
def header():
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE5Mzc4Mjc3LCJpYXQiOjE3MTg3NzgyNzcsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjI4NDIzYTljLThhNWMtNDRlYy04YTBkLThkNTUyZTY3ODUzZCIsImVtYWlsIjoidHJhbGwxODExMTk4NUBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImdpdGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8xNjEwMDI1OTk_dj00IiwiZW1haWwiOiJ0cmFsbDE4MTExOTg1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJLb25zdGFudGluIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJLb25zdGFudGluIiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJHcm9tLVphZGlyYTg1IiwicHJvdmlkZXJfaWQiOiIxNjEwMDI1OTkiLCJzdWIiOiIxNjEwMDI1OTkiLCJ1c2VyX25hbWUiOiJHcm9tLVphZGlyYTg1In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MTg3NzgyNzd9XSwic2Vzc2lvbl9pZCI6ImQ3NmE3NGI2LWJlZjctNGEzYy05ZDU4LWFlOWY5MWE5YzU4ZSIsImlzX2Fub255bW91cyI6ZmFsc2V9.V3VhSModWq0vgB0KTDFHT6e9DLu-L06cLjJ2jaB9s2s",
        "X-Task-Id": "API-1",
        'accept': 'application/json',
        'content-Type': 'application/json'
    }


def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())


@pytest.mark.ok
def test_add_user(page: Page):
    data = [
        {
            "id": 9743,
            "username": "cheburek",
            "firstName": "belyashovovich",
            "lastName": "pelmen",
            "email": "kitcen",
            "password": "nyam-nyam",
            "phone": "333",
            "userStatus": 0
        }
    ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=header)
    print(response.status)
    print(response.json())


@pytest.mark.xfail
# status ==405
def test_add_pet(page: Page):
    data = [
        {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
    ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/#/pet/addPet', data=data, headers=header)
    print(response.status)
    print(response.json())


def test_api_1_post_user(page: Page, header):
    data = {

        "email": "max3@gmail.com",
        "password": "password",
        "name": "Maximus",
        "nickname": "maximus"
    }



    response = page.request.post('https://dev-gs.qa-playground.com/api/v1/users', data=data, headers=header)

    print(response.status)
    # print(response.json())
    save_json(response.json(), 'create_user.json')


def test_api_1_get_user(page: Page, header):

    user = read_json('create_user.json')['uuid']
    response = page.request.get(f'https://dev-gs.qa-playground.com/api/v1/users/{user}', headers=header)

    print(response.status)
    print(response.json())
    # print(response.json()['users'][0])


def test_api_1_dell_user(page: Page, header):

    user = read_json('create_user.json')['uuid']

    response = page.request.delete(f'https://dev-gs.qa-playground.com/api/v1/users/{user}', headers=header)
    url = f'https://dev-gs.qa-playground.com/api/v1/users/{user}'
    print(url)
    print(response.status)
    print(response.json())
    # print(response.json()['users'][0])