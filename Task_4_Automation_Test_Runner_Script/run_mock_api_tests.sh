#!/bin/bash
echo "-> Go to folder Task_2_API_Testing."
cd /mnt/c/Users/mniedziolka/PycharmProjects/homework_Mateusz_repo/Task_2_API_Testing
echo "-> Activate the environment."
. ./venv/Scripts/activate
echp "-> pip install flask if needed."
echo "-> Run mock api."
python3 mock_api.py &
PYTHON_PID=$! # |AI|
echo "-> Run mock api tests."
pytest -v test_mock_api.py
echo "-> Stop mock api."
kill $PYTHON_PID # |AI|

