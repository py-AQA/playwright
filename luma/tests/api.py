import pytest
from playwright.sync_api import Page, expect
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
    print(response.json())
    save_json(response.json(), 'create_user.json')
    assert response.status == 200, "error, status code not correctly"


def test_api_1_get_user(page: Page, header):
    user = read_json('create_user.json')['uuid']
    print(user, header)
    response = page.request.get(f'https://dev-gs.qa-playground.com/api/v1/users/{user}', headers=header)

    print(response.status)
    print(response.json())

    url = f'https://dev-gs.qa-playground.com/api/v1/users/{user}'
    print(url)
    # save_json(response.json(), 'list_user.json')
    assert response.status == 200, "error, status code not correctly"


def test_api_1_dell_user(page: Page, header):
    user = read_json('create_user.json')['uuid']
    # users = read_json('list_user.json')['users']
    print(user)
    # first_uuid = users[0]['uuid']
    #
    # response = page.request.delete(f'https://dev-gs.qa-playground.com/api/v1/users/{first_uuid}', headers=header)
    # url = f'https://dev-gs.qa-playground.com/api/v1/users/{first_uuid}'

    response = page.request.delete(f'https://dev-gs.qa-playground.com/api/v1/users/{user}', headers=header)
    url = f'https://dev-gs.qa-playground.com/api/v1/users/{user}'

    print(url)
    print(response.status)
    # print(response.json())
    # print(response.json()['users'][0])
    assert response.status == 204, "error, status code not correctly"


import requests
import pytest

BASE_URL = "https://release-gs.qa-playground.com/api/v1"
AUTH_HEADER = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE5Mzc4Mjc3LCJpYXQiOjE3MTg3NzgyNzcsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjI4NDIzYTljLThhNWMtNDRlYy04YTBkLThkNTUyZTY3ODUzZCIsImVtYWlsIjoidHJhbGwxODExMTk4NUBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImdpdGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8xNjEwMDI1OTk_dj00IiwiZW1haWwiOiJ0cmFsbDE4MTExOTg1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJLb25zdGFudGluIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJLb25zdGFudGluIiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJHcm9tLVphZGlyYTg1IiwicHJvdmlkZXJfaWQiOiIxNjEwMDI1OTkiLCJzdWIiOiIxNjEwMDI1OTkiLCJ1c2VyX25hbWUiOiJHcm9tLVphZGlyYTg1In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MTg3NzgyNzd9XSwic2Vzc2lvbl9pZCI6ImQ3NmE3NGI2LWJlZjctNGEzYy05ZDU4LWFlOWY5MWE5YzU4ZSIsImlzX2Fub255bW91cyI6ZmFsc2V9.V3VhSModWq0vgB0KTDFHT6e9DLu-L06cLjJ2jaB9s2s"

}


def headers(x_task_id):
    return {
        "Authorization": AUTH_HEADER["Authorization"],
        "X-Task-Id": x_task_id
    }


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205


def test_delete_user(header):
    # Step 1: Get user list
    print(header)
    response = requests.get(f"{BASE_URL}/users", headers=header)
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0, "No users found"

    # Step 2: Choose a user and get user uuid
    user_uuid = users[0]['uuid']

    # Step 3: Send DELETE request to delete the user
    response = requests.delete(f"{BASE_URL}/users/{user_uuid}", headers=header)
    assert response.status_code == 204

    # Step 5: Validate that the user was deleted from the user list
    response = requests.get(f"{BASE_URL}/users", headers=header)
    assert response.status_code == 200
    users = response.json()
    assert not any(user['uuid'] == user_uuid for user in users), "User not deleted"

    # Step 6: Verify that user information doesn't return
    response = requests.get(f"{BASE_URL}/users/{user_uuid}", headers=header)
    assert response.status_code == 404


