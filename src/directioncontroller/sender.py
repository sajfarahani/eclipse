import argparse

known_drivers = ['start', 'stop', 'left', 'right', 'forward', 'back']


HOST = '127.0.0.1'
PORT = 65432


class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'start', 'stop', 'left', 'right', 'forward', & 'back'")
        namespace.driver = driver.lower()
        namespace.destination = destination



