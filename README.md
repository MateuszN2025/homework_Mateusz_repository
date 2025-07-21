# Setup & Run Instructions

## General environment requirements: 
- System : Windows 11, WSL
- IDE: PyCharm
- Android Studio: Phone emulator: 'Medium Phone API 36.0' ('emulator-5554')

## Instructions for running individual tests or all tests collectively:
- Mobile App testing: You need to run Android Studio and Phone emulator first. Then You can use
'pytest' to run whole test file or each test individually in a test file.
- Mock API testing: You can run test individually using 'pytest' or bash scripts (WSL) in 'Task_4_Automation_Test_Runner_Script' 
folder.

## Test Descriptions
- Mobile App testing: We want to verify all basic mathematical operations like addition, subtraction,
division and multiplication
- Mock API testing: We want to verify HTTPS methods like GET, POST. Endpoint: /users, /users/id

## Environment Details
- Python version: 3.9
- Packages: pytest, flask, json, behave