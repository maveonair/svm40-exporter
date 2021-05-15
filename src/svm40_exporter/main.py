import time
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_svm40 import Svm40ShdlcDevice

from prometheus_client import start_http_server, Gauge

AIR_QUALITY_GAUGE = Gauge("svm40_air_quality", "Air Quality")
HUMIDITY_GAUGE = Gauge("svm40_humidity", "Humidity")
TEMP_GAUGE = Gauge("svm40_temperature", "Temperature")


def main():
    print("Prometheus Metrics endpoint is listening on 9140")
    start_http_server(9140)

    with ShdlcSerialPort(port="/dev/ttyUSB0", baudrate=115200) as port:
        device = Svm40ShdlcDevice(ShdlcConnection(port), slave_address=0)
        device.device_reset()

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # Start measurement
        device.start_measurement()
        print("Measurement started... ")
        while True:
            _report_metrics(device)

            time.sleep(10.0)


def _report_metrics(device):
    air_quality, humidity, temperature = device.read_measured_values()

    AIR_QUALITY_GAUGE.set(air_quality.voc_index)
    HUMIDITY_GAUGE.set(humidity.percent_rh)
    TEMP_GAUGE.set(temperature.degrees_celsius)
