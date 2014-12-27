modem-cmd (Python)
==================

Send arbitrary AT commands to your modem

**Usage: python -m modemcmd MODEM\_DEVICE COMMAND [TIMEOUT]**

::

    pip install modem-cmd

Example
-------

Command line
~~~~~~~~~~~~

**Get signal**

::

    $ python -m modemcmd /dev/ttyUSB2 AT+CSQ
    +CSQ: 12,99

**Get Operator**

::

    $ python -m modemcmd /dev/ttyUSB2 AT+COPS?
    +COPS: 0,0,"Chunghwa Telecom",2

API
~~~

::

    from modemcmd import modemcmd
    from modemcmd import ModemcmdException
    from modemcmd import ModemcmdTimeoutException

    try:
        result = modemcmd('/dev/ttyUSB2', 'AT+CSQ', 10)
    except ModemcmdTimeoutException as e:
        print e
    except ModemcmdException as e:
        print e

License
-------

MIT: http://yulun.mit-license.org
