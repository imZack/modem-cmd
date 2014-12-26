#!/usr/bin/env python

'''
modem-cmd main script
@author: YuLun Shih <shih@yulun.me>
'''
from __future__ import print_function
import sys
from serial import Serial
from serial import SerialException
from serial import SerialTimeoutException


class ModemcmdTimeoutException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ModemcmdException(Exception):
    def __init__(self, msg):
        self.msg = msg


def modemcmd(port, cmd, timeout=20):
    try:
        serial = Serial(port=port,
                        timeout=int(timeout),
                        writeTimeout=int(timeout))
    except SerialException as e:
        raise ModemcmdException(e)

    cmd = cmd + '\r'
    try:
        serial.write(cmd)
    except SerialTimeoutException:
        raise ModemcmdTimeoutException('Write timeout')

    line = serial.readline()
    if line == '':  # timeout
        raise ModemcmdTimeoutException('Read timeout')

    # Except echo input command
    if cmd != line[:-2]:  # trim \r\n
        return 'modemcmd ERROR'

    line = serial.readline()
    if line == '':  # timeout
        raise ModemcmdTimeoutException('Read timeout')

    return line[:-1]


def main(argv):
    if len(argv) < 3:
        print('Usage: %s MODEM_DEVICE COMMAND [TIMEOUT]' % argv[0])
        exit(1)

    try:
        print(modemcmd(*argv[1:]))
        exit(0)
    except ModemcmdTimeoutException as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main(sys.argv)
