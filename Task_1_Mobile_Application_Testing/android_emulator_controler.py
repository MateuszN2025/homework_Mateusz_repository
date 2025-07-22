import subprocess
import os
import xml.etree.ElementTree as ET  # |AI|


class AndroidEmulatorControler:

    def __init__(self, adb_path=os.path.join('.', 'platform-tools', 'adb.exe'), device_ip='127.0.0.1:5555'):
        self.adb_path = adb_path
        self.device_ip = device_ip
        self.device_serial = None

    def make_a_connection(self):
        response = subprocess.run([self.adb_path, 'connect', self.device_ip], capture_output=True, text=True)
        if 'connected' in response.stdout:
            print("Device is connected.")
            device_result = subprocess.run([self.adb_path, 'devices'], capture_output=True, text=True)
            print(f"device_result.stdout.splitlines() -> {device_result.stdout.splitlines()}")
            devices = [line.split()[0] for line in device_result.stdout.splitlines() if '\tdevice' in line]
            if devices:
                self.device_serial = devices[0]
                print(f"Using devices: {self.device_serial}")
                return True
            else:
                print("No devices were found")
                return False

    def find_application_name(self, application_name):
        response = subprocess.run(
            [self.adb_path, '-s', self.device_serial, 'shell', 'pm', 'list', 'packages', application_name],
            capture_output=True,
            text=True)
        
        print("running...find_application_name")
        print(f"response.stdout: {response.stdout}")

        for line in response.stdout.splitlines():
            if application_name in line:
                package_name = line.split(':')[1]
                return package_name

        # Found package name:
        # package_name = 'com.admsqa.buggycalc'
        return None

    def trigger_application(self, package_name):
        response = subprocess.run(
            [self.adb_path, '-s', self.device_serial, 'shell', 'monkey', '-p', package_name, '-c',
             'android.intent.category.LAUNCHER 10'],
            # |AI| used to solve the problem with monkey and "Error: Count not specified"
            capture_output=True,
            text=True)

        print(f"package_name: {package_name}")
        print("running...trigger_application")
        print(f"response.stdout: {response.stdout}")
        
        if response.returncode == 0:
            print(f"{package_name} started")
            return True
        else:
            print(f"Failed to start {package_name}")
            return False

    def clearing_inputs(self, iterations=5):

        subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'tap', "500", "300"])
        for i in range(iterations):
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'keyevent', '67'])
            # |AI| used to get keyevent to clear the field
            # keyevent 67 is a backspace key

        subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'tap', "500", "400"])
        for i in range(iterations):
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'keyevent', '67'])

    def execute_mathematical_operation(self,
                                       number_1: str,
                                       operation: str,
                                       number_2: str):
        button_coordinates = {}

        if self.device_serial:

            # #########################################
            #  Clearing input fields
            # #########################################
            self.clearing_inputs(iterations=20)

            # #########################################
            # Injecting number for calculations
            # #########################################
            text_field_number1 = {"x_coor": "500", "y_coor": "300"}
            text_field_number2 = {"x_coor": "500", "y_coor": "400"}

            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'tap',
                            text_field_number1["x_coor"], text_field_number1["y_coor"]])
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'text', number_1])

            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'tap',
                            text_field_number2["x_coor"], text_field_number2["y_coor"]])
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'text', number_2])

            # #########################################
            # Choosing the type of the operation
            # #########################################
            if operation == "+":
                expected_result = float(number_1) + float(number_2)
                button_coordinates = {"x_coor": "500", "y_coor": "500"}
            elif operation == "-":
                expected_result = float(number_1) - float(number_2)
                button_coordinates = {"x_coor": "500", "y_coor": "600"}
            elif operation == "/":
                try:
                    expected_result = float(number_1) / float(number_2)
                except ZeroDivisionError:
                    print("ZeroDivisionError")
                finally:
                    button_coordinates = {"x_coor": "500", "y_coor": "700"}
            elif operation == "*":
                expected_result = float(number_1) * float(number_2)
                button_coordinates = {"x_coor": "500", "y_coor": "900"}

            # #########################################
            # Clicking operation button
            # #########################################
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'input', 'tap',
                            button_coordinates["x_coor"], button_coordinates["y_coor"]])

            # #########################################
            # Gathering logs. # |AI|
            # #########################################
            subprocess.run([self.adb_path, '-s', self.device_serial, 'shell', 'uiautomator', 'dump'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            subprocess.run([self.adb_path, '-s', self.device_serial, 'pull', '/sdcard/window_dump.xml',
                            'local_ui_dump_logs.xml'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # #########################################
            # Result verification
            # #########################################
            with open('local_ui_dump_logs.xml', 'r') as f:
                xml_string = f.read()

            xml_string = ET.fromstring(xml_string)  # |AI|
            observed_result_from_xml = 0

            for node in xml_string.findall('.//node'): # |AI|
                try:
                    observed_result_from_xml = float(node.get('text')) # |AI|
                except ValueError:
                    pass
                else:
                    observed_result_from_xml = float(node.get('text'))
                    break

            if observed_result_from_xml is None:
                assert Exception("No result")
            else:
                print(f"Expected result = {expected_result}")
                print(f"Observed result = {observed_result_from_xml}")
                assert expected_result == observed_result_from_xml, "Wrong calculations!"

        else:
            print("Device serial is not specified.")
