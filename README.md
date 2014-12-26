<a href="https://github.com/imZack/modem-cmd">
    <img src="https://cloud.githubusercontent.com/assets/690703/5554509/d42851c4-8c98-11e4-8438-cc35dc7d8bf5.png" align="right" width="200px;" />
</a>

modem-cmd (Python)
==================

Send arbitrary AT commands to your modem

Usage: python -m modemcmd MODEM_DEVICE COMMAND [TIMEOUT]

`pip install modem-cmd`

Example
-------

### Command line
**Get signal**

    $ python -m modemcmd /dev/ttyUSB2 AT+CSQ
    +CSQ: 12,99

**Get Operator**

    $ python -m modemcmd /dev/ttyUSB2 AT+COPS?
    +COPS: 0,0,"Chunghwa Telecom",2

### API

```py
from modemcmd import modemcmd
from modemcmd import ModemcmdException
from modemcmd import ModemcmdTimeoutException

try:
    result = modemcmd('/dev/ttyUSB2', 'AT+CSQ', 10)
except ModemcmdTimeoutException as e:
    print e
except ModemcmdException as e:
    print e
```

License
-------
MIT: http://yulun.mit-license.org
