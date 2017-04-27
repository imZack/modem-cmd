from __future__ import print_function
from serial import Serial
from serial import SerialException
from serial import SerialTimeoutException


class ModemcmdTimeoutException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ModemcmdException(Exception):
    def __init__(self, msg):
        self.msg = msg


def modemcmd(port, cmd, timeout=0.3):
    try:
        serial = Serial(port=port,
                        timeout=float(timeout))
    except SerialException as e:
        raise ModemcmdException(e)

    cmd = cmd + '\r'
    try:
        serial.write(cmd)
    except SerialTimeoutException:
        raise ModemcmdTimeoutException('Write timeout')

    lines = serial.readlines()
    if lines == '':  # timeout
        raise ModemcmdTimeoutException('Read timeout')

    return "".join(lines)
