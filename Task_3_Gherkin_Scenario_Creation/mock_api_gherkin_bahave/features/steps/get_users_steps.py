from behave import given, when, then
from Task_2_API_Testing.test_mock_api import if_mock_api_is_running,\
    get_users, data_validation, expected_user_data_1


@given('mock api is running')
def step_1(context):
    context.sc = if_mock_api_is_running()


@when('request to a server was successfully processed get users')
def step_2(context):
    context.response_list_get = get_users(context.sc)


@then('validate user data retrieval')
def step_3(context):
    data_validation(context.response_list_get, expected_user_data_1)
