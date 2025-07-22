# Setup & Run Instructions

## General environment requirements 
- System : Windows 11, WSL
- IDE: PyCharm
- Android Studio: Phone emulator: 'Medium Phone API 36.0' ('emulator-5554')
- 'buggy_calc_debug.apk' installed on a phone emulator in the Android Studio
- 'mock_api.py' based on 'flask'
- 'platform-tools' with Android Debug Bridge (adb) 

## Instructions for running tests
### Mobile App testing
#### Setup:
- You need to run Android Studio and Phone emulator first.
- The next step is to install 'buggy_calc_debug.apk' directly in the Android Studio
(You can just drop provided app on the emulator's screen). 
#### Running individual tests
- In 'Task_1_Mobile_Application_Testing' folder You can use e.g.:
***pytest test_buggy_calc.py::test_3_buggy_calc_division*** in CLI to run only one test.
#### Running all tests collectively
- In 'Task_1_Mobile_Application_Testing' folder You can use: ***pytest test_buggy_calc.py*** in CLI
to run whole test file.

### Mock API testing
#### Setup
- You can run 'mock_api.py' manually
#### Running individual tests
- If You manually run 'mock_api.py' You can trigger test directly in Pycharm, in a 'test_mock_api.py' by
clicking green arrow next to the single test.
- In 'Task_2_API_Testing' folder You can use e.g.:
***python3 mock_api.py & PYTHON_PID=$! ; pytest test_mock_api.py::test_2_post_test; kill $PYTHON_PID*** 
in CLI to run only one test.
#### Running all tests collectively
- In 'Task_2_API_Testing' folder You can use:
***python3 mock_api.py & PYTHON_PID=$! ; pytest test_mock_api.py; kill $PYTHON_PID*** in CLI
to run whole test file or bash scripts: 'run_mock_api_tests.sh' or 'run_gherkin_behave_tests.sh'
(WSL environment) in 'Task_4_Automation_Test_Runner_Script' folder.

## Test Descriptions
- Mobile App testing: We want to verify all basic mathematical operations like addition, subtraction,
division and multiplication
- Mock API testing: We want to verify HTTPS methods like GET, POST (endpoint: /users, /users/id).

## Environment Details
- Python 3.10.12
- Packages: pytest 8.2.2, Flask 3.1.1, behave 1.2.6
- Android Studio Narwhal | 2025.1.1 Patch 1