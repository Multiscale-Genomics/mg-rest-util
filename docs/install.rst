Requirements and Installation
=============================

Requirements
------------

Software
^^^^^^^^
- Python 2.7.10+
- pyenv
- pyenv virtualenv
- pip

Python Modules
^^^^^^^^^^^^^^
- Flask
- Flask-Restful
- Waitress
- Sphinx
- sphinx-autobuild

Installation
------------

Basics
^^^^^^
Directly from GitHub:

.. code-block:: none
   :linenos:

   git clone https://github.com/Multiscale-Genomics/mg-rest-util.git
   cd mg-rest-util/
   pip install -e .
   pip install -r requirements.txt

Using pip:

.. code-block:: none
   :linenos:

   pip install git+https://github.com/Multiscale-Genomics/mg-rest-util.git


Documentation
-------------
To build the documentation:

.. code-block:: none
   :linenos:

   pip install Sphinx
   pip install sphinx-autobuild
   cd docs
   make html
