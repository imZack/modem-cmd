#!/usr/bin/env python

'''
modem-cmd main script
@author: YuLun Shih <shih@yulun.me>
'''
from __future__ import print_function
import sys
from serial import Serial
from serial import SerialTimeoutException


def modem_cmd(port, cmd, timeout=20):
    serial = Serial(port=port,
                    timeout=int(timeout),
                    writeTimeout=int(timeout))

    cmd = cmd + '\r'
    serial.write(cmd)

    line = serial.readline()
    if line == '':  # timeout
        return ''
    if cmd != line[:-2]:  # trim \r\n
        return 'modem_cmd ERROR'

    line = serial.readline()

    if line == '':  # timeout
        return ''

    return line[:-1]


def main(argv):
    # print(VERSION)
    if len(argv) < 3:
        print('Usage: %s MODEM_DEVICE COMMAND [TIMEOUT]' % argv[0])
        exit(1)

    try:
        print(modem_cmd(*argv[1:]))
        exit(0)
    except SerialTimeoutException:
        print('Write timeouts')
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main(sys.argv)
