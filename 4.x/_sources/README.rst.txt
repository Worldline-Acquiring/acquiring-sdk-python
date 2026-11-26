Worldline Acquiring Python SDK
==============================

Introduction
------------

The Python SDK helps you to communicate with the Worldline Acquiring API. Its primary features are:

-  convenient Python library for the API calls and responses

   -  marshals Python request objects to HTTP requests
   -  unmarshals HTTP responses to Python response objects or Python exceptions

-  handling of all the details concerning authentication
-  handling of required metadata

See the `Worldline Acquiring Documentation <https://docs.acquiring.worldline-solutions.com/Developer-Tools/sdk/python>`__ for more information on how to use the SDK.

Structure of this repository
----------------------------

This repository consists out of four main components:

#. The source code of the SDK itself: ``/worldline/acquiring/sdk/``
#. The source code of the SDK unit tests: ``/tests/unit/``
#. The source code of the SDK integration tests: ``/tests/integration/``

Note that the source code of the unit tests and integration tests can only be found on GitHub.

Requirements
------------

Python 3.11 or higher is required. In addition, the following packages are required:

-  `requests <https://requests.readthedocs.io/>`__ 2.32.4 or higher
-  `requests-toolbelt <https://toolbelt.readthedocs.io/>`__ 1.0.0 or higher

These packages will be installed automatically if the SDK is installed manually or using pip following the below instructions.

Installation
------------

To install the SDK using pip, execute the following command:

.. code:: bash

   pip install acquiring-sdk-python

Alternatively, you can install the SDK from a source distribution file:

#. Download the latest version of the Python SDK from GitHub. Choose the ``acquiring_sdk_python-x.y.z.tar.gz`` file from the `releases <https://github.com/Worldline-Acquiring/acquiring-sdk-python/releases>`__ page, where ``x.y.z`` is the version number.

#. Execute the following command in the folder where the SDK was downloaded to:

   .. code:: bash

      pip install acquiring_sdk_python-x.y.z.tar.gz

Uninstalling
------------

After the Python SDK has been installed, it can be uninstalled using the following command:

.. code:: bash

   pip uninstall acquiring-sdk-python

The required packages can be uninstalled in the same way.

Running tests
-------------

There are two types of tests: unit tests and integration tests. The unit tests will work out-of-the-box; for the integration tests some configuration is required.
First, some environment variables need to be set:

-  ``acquiring.api.oauth2.clientId`` for the OAUth2 client id to use.
-  ``acquiring.api.oauth2.clientSecret`` for the OAuth2 client secret to use.
-  ``acquiring.api.merchantId`` for your merchant ID.

In addition, to run the proxy integration tests, the following environment variables need to be set:

-  ``acquiring.api.proxy.uri`` for the URI of the proxy to use.
-  ``acquiring.api.proxy.username`` and ``acquiring.api.proxy.password`` if the proxy requires authentication.

The proxy integration tests are skipped if ``acquiring.api.proxy.uri`` is not set.

The following commands can now be executed from the ``tests`` directory to execute the tests:

-  Unit tests:

   .. code:: bash

      python run_unit_tests.py

-  Integration tests:

   .. code:: bash

      python run_integration_tests.py

-  Both unit and integration tests:

   .. code:: bash

      python run_all_tests.py
