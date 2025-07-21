import requests
import json

api_url_users = 'http://127.0.0.1:5003/users'

expected_user_data_1 = [
    {"email": "alice@example.com", "id": 1, "name": "Alice"},
    {"email": "bob@example.com", "id": 2, "name": "Bob"}
]

new_user = {"name": "John", "email": "john@john.com"}

expected_user_data_2 = [
    {"email": "alice@example.com", "id": 1, "name": "Alice"},
    {"email": "bob@example.com", "id": 2, "name": "Bob"},
    {"email": "john@john.com", "id": 3, "name": "John"}
]


def if_mock_api_is_running():
    response = requests.request('GET', api_url_users)
    sc = response.status_code
    if sc == 200:
        print("API is running. Status code: {sc}")
    else:
        raise AssertionError(f"Problem with API. Status code: {sc}")
    return sc


def get_users(sc):
    if sc in [200, 201]:
        response = requests.request('GET', api_url_users)
        json_response = json.dumps(response.json())
        response_list_get = json.loads(json_response)
    else:
        raise AssertionError(f"Data unavailable. Status code: {sc}")
    return response_list_get


def data_validation(obs_data, exp_data):
    exp_list = []
    obs_list = []

    for exp_item in exp_data:
        for k, v in exp_item.items():
            exp_list.append(k)
            exp_list.append(v)

    for obs_item in obs_data:
        for k, v in obs_item.items():
            obs_list.append(k)
            obs_list.append(v)

    print("===================================")
    print(f"EXPECTED users data: {exp_list}")
    print(f"OBSERVED users data: {obs_list}")
    print("===================================")

    exp_list_len = len(exp_list)
    obs_list_len = len(obs_list)

    # Protection against comparing unequal length lists
    if exp_list_len >= obs_list_len:
        longer_len = exp_list_len
    else:
        longer_len = obs_list_len

    # List comparison
    for i in range(longer_len):
        if exp_list[i] == obs_list[i]:
            pass
        else:
            raise AssertionError(f"Retrieved is wrong: {exp_list[i]} != {obs_list[i]}")


def post_user():
    response_post = requests.post(url=api_url_users, json=new_user)
    sc_post = response_post.status_code
    print(sc_post)
    if sc_post == 201:
        pass
    else:
        raise AssertionError(f"Error during user creation. Status code: {sc_post}")

    return sc_post


def error_handling(users_list_ids):
    for user_id in users_list_ids:
        print("\n===================================")
        api_url_users_id = api_url_users + "/" + str(user_id)
        print(f"{api_url_users_id}")
        response_get = requests.request('GET', api_url_users_id)
        sc_get = response_get.status_code
        if sc_get == 200:
            json_response_get = json.dumps(response_get.json())
            print(f"User {user_id}: {json_response_get}")
            print("===================================")
        elif sc_get == 404:
            print(f"User {user_id}: not found. Status code: {sc_get}")
        elif sc_get == 500:
            print(f"User {user_id}: Intentional error for testing purposes. Status code: {sc_get}")
        else:
            raise AssertionError("Not expected status code received: sc_get")


def test_1_get_test():
    """
    GET /users: Retrieve a list of users.
    GET Test: Validate user data retrieval.
    """
    sc = if_mock_api_is_running()
    response_list_get = get_users(sc)
    data_validation(response_list_get, expected_user_data_1)


def test_2_post_test():
    """
    POST /users: Add a new user. The request expects JSON in the format:
     `{"name": ..., "email": ...}`.
     Implement robust error handling and reporting for invalid input.
     POST Test: Validate the creation of new users.
    """
    sc = post_user()
    response_list_get = get_users(sc)
    data_validation(response_list_get, expected_user_data_2)


def test_3_error_handling_test():
    """
    GET /users/<id>: Retrieve a user by ID. Handle the following responses:
    404: User not found.
    500: Intentional error for testing purposes (when `ID = 999`).
    Error Handling Test: Validate expected error responses (e.g., 400 or 500 status codes).
    """
    error_handling(users_list_ids=[1, 2, 3, 4, 999])
