#!/bin/bash
echo "-> Run mock api."
cd /mnt/c/Users/mniedziolka/PycharmProjects/homework_Mateusz_repo/Task_2_API_Testing
python3 mock_api.py &
PYTHON_PID=$! # |AI|
echo "-> Go to folder Task_3_Gherkin_Scenario_Creation."
cd /mnt/c/Users/mniedziolka/PycharmProjects/homework_Mateusz_repo/Task_3_Gherkin_Scenario_Creation
echo "-> Activate the environment."
. ./venv/Scripts/activate
echo "-> pip install behave if needed."
echo "-> Add the project root directory to PYTHONPATH"
export PYTHONPATH=$PYTHONPATH://mnt/c/Users/mniedziolka/PycharmProjects/homework_Mateusz_repo/ # |AI|
echo "-> Execute behave."
cd /mnt/c/Users/mniedziolka/PycharmProjects/homework_Mateusz_repo/Task_3_Gherkin_Scenario_Creation/mock_api_gherkin_bahave/features
behave
echo "-> Stop mock api."
kill $PYTHON_PID # |AI|

