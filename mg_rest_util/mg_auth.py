"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import print_function

# Required for ReadTheDocs
from functools import wraps # pylint: disable=unused-import

import sys
import json
from httplib2 import Http
from flask import request, abort

def validate_token(access_token):
    """
    Verify that a MuG access token is valid

    Parameters
    ----------
    access_token : str

    Returns
    -------
    user_ids : dict
        user_id : str
            The user_id, None if user does not exist or the test user_id if on a
            test server
        piblic_id : str
            The user_id for public datasets. This is set using the RESTful servers
            authoristation config file.
    """

    if hasattr(sys, "_auth_meta_json") is False:
        raise IOError

    with open(sys._auth_meta_json) as data_file:
        data = json.load(data_file)

    if data["auth_server"]["test"] == 1:
        return {
            "user_id": "test"
        }

    http_handler = Http()
    resp, user_data = http_handler.request(
        data["auth_server"]["url"],
        headers={
            "Authorization": access_token
        }
    )

    if not resp["status"] == "200":
        return None

    try:
        auth_data = json.loads(user_data)
    except TypeError:
        # Python 3 returns byt objects
        auth_data = json.loads(user_data.decode())

    user_ids = {
        "user_id": auth_data["mug_id"]
    }
    if "public_id" in data["public_id"]:
        user_ids["public_id"] = data["public_id"]

    return user_ids

def authorized(func):
    """
    Wrapper for authorization based on tokens

    Example
    -------
    .. code-block:: python
       :linenos:

       from mg_rest_util.mg_auth import authorized

       class GetTest(Resource):

           @authorized
           def get(self, user_id):
               if user_id is not None:
                   return "Valid user token"
               return {
                   'error': 'Forbidden',
                   'status': 403
               }
    """

    @wraps(func)
    def _wrap(*args, **kwargs):
        if "Authorization" not in request.headers:
            with open(sys._auth_meta_json) as data_file:
                data = json.load(data_file)

            if data["auth_server"]["test"] == 1:
                return {
                    "user_id": "test"
                }

            print("No token provided")
            abort(401)
            return None

        print("Checking token ...")
        user_id = validate_token(request.headers["Authorization"])
        if user_id is None:
            print("Check FAILED")
            abort(401)
            return None

        return func(user_id=user_id, *args, **kwargs)

    return _wrap
