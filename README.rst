modem-cmd (Python)
==================
.. image:: https://pypip.in/version/modem-cmd/badge.svg
    :target: https://pypi.python.org/pypi/modem-cmd/
    :alt: Latest Version

Send arbitrary AT commands to your modem

**Usage: modem-cmd MODEM\_DEVICE COMMAND [TIMEOUT]**

::

    pip install modem-cmd

Example
-------

Command line
~~~~~~~~~~~~

**Get signal**

::

    $ modem-cmd /dev/ttyUSB2 AT+CSQ
    +CSQ: 12,99

**Get Operator**

::

    $ modem-cmd /dev/ttyUSB2 AT+COPS?
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

GPLv3+
