# Everysense Rest API client

[![Build Status](https://travis-ci.org/daiyanze/everyclient.svg?branch=master)](https://travis-ci.org/daiyanze/everyclient)
[![Release Version](https://img.shields.io/pypi/v/everyclient.svg)](https://pypi.python.org/pypi/everyclient)
[![License](https://img.shields.io/pypi/l/everyclient.svg)](https://pypi.python.org/pypi/everyclient)

### Requirements
* Python (2.7, 3.4, 3.5, 3.6)
* [urllib3[secure]](https://github.com/shazow/urllib3)(1.20)

### Installation

Pypi
```
pip install everyclient
```

Local
```
1. Download package

2. cd everyclient

3. python setup.py install
```

### Example Usage
``` python
from everyclient import EveryClient
EveryClient().auth_user(["account","password"])
```

### API Docs
Please follow the link below and read our API document

[Rest API Documentation](http://dev.every-sense.com)
