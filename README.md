# mg-rest-util
Util functions common to all rest services

[![Documentation Status](https://readthedocs.org/projects/mg-rest-util/badge/?version=latest)](http://mg-rest-util.readthedocs.io/en/latest/?badge=latest) [![Code Health](https://landscape.io/github/Multiscale-Genomics/mg-rest-util/master/landscape.svg?style=flat)](https://landscape.io/github/Multiscale-Genomics/mg-rest-util/master)

# Requirements
- Python 2.7.10+
- pyenv
- pyenv virtualenv
- Python Modules:
  - Flask
  - Flask-Restful
  - httplib2

# Installation
Cloneing from GitHub:
```
git clone https://github.com/Multiscale-Genomics/mg-rest-util.git
```
To get this to be picked up by pip if part of a webserver then:
```
pip install --editable .
pip install -r requirements.txt
```
This should install the required packages listed in the `setup.py` script.


Installation via pip:
```
pip install git+https://github.com/Multiscale-Genomics/mg-rest-util.git
```
