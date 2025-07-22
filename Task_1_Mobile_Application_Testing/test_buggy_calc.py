from android_emulator_controler import AndroidEmulatorControler
import pytest

emu = AndroidEmulatorControler()

@pytest.fixture
def verify_connetion():
    if emu.make_a_connection():
        print("Successful connection!")
        print("=========== FIND PACKAGE NAME ===================")
        package_name = emu.find_application_name("buggy")
        print("============ RUN APP =======================")
        emu.trigger_application(package_name)
    else:
        raise AssertionError("Connection failed.")

@pytest.mark.parametrize("a, b, expected", [(10, 20, 30), (121, 213, 334), (12.31, 12.33, 24.64)])
def test_1_buggy_calc_addition(a, b, expected, verify_connetion):
        print("=============ADDITION======================")
        emu.execute_mathematical_operation(number_1=str(a), operation="+", number_2=str(b))

@pytest.mark.parametrize("a, b, expected", [(50, 25, 25), (1, 2, -1), (10000.1, 1.2, 998.9)])
def test_2_buggy_calc_subtraction(a, b, expected, verify_connetion):
        print("=============SUBTRACTION======================")
        emu.execute_mathematical_operation(number_1=str(a), operation="-", number_2=str(b))

@pytest.mark.parametrize("a, b, expected", [(8, 4, 2), (1000, 500, 2), (5, 2, 2.5)])
def test_3_buggy_calc_division(a, b, expected, verify_connetion):
        print("=============DIVISION======================")
        emu.execute_mathematical_operation(number_1=str(a), operation="/", number_2=str(b))

@pytest.mark.parametrize("a, b, expected", [(15, 15, 225), (2.5, 2.5, 6.25), (1.25, 4, 6)])
def test_4_buggy_calc_division(a, b, expected, verify_connetion):
        print("=============MULTIPLICATION======================")
        emu.execute_mathematical_operation(number_1=str(a), operation="*", number_2=str(b))




