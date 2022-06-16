import json
from flask import Flask, request, jsonify
import subprocess
import os
import requests
# how you do debugging in python
# import pdb
# pdb.set_trace()

app = Flask(__name__)
port = os.getenv("PORT", 3005)

# grab any sort of auth stuff from env
auth_thing = os.getenv("whatever_env")

app.logger.debug("This is how you log in Flask not sure why you'd use this over print")

def load_some_stuff():
    """How to add descriptions to your functions"""
    # setting headers and stuff ... not sure json is right for a get
    headers = {'Content-type' : 'application/json', 'whatever': 'else you need to set'}
    r = requests.get("https://google.com", auth={auth_thing}, verify=False, headers=headers)
    content = r.json()
    # if you want to just filter the content that comes back
    thing = filter(lambda stuff: stuff["some_property"] == "something" and  stuff["some_other_thing"] == "something_else")

    # think you can write it like this too
    thing = filter(lambda thingy: thingy["name"] == "Taylor", content)

    # map works the same way
    thing = map(lambda thingy: thingy["name"] == "Taylor", content)

    return list(thing)

def do_some_terminal_thing(package):
    # an example of how to install things
    result = subprocess.run(["npm", "install", package])
    if result.returncode != 0:
        # should be 0 if all good
        app.logger.info(f"Failed to download {package}")

def some_random_function(returning_me):
    return returning_me

# setup some route handling
@app.route('/api/test', methods=['POST'])
def return_something():
    # grab content
    content = request.json
    # just returning something here
    return jsonify({"done": "success"})

# How you do classes
class SomeReusableThing:
    """Reusable guy"""
    # You don't need to init if you don't want to
    def __init__(self, name):
        print(f"Hi my name is {name} and I was just made")
    def some_method_that_opens_files():
        # this way of opening files closes the resources when you're done
        with open("path/to/file", "rwb") as f:
            # if you were to load json
            some_json = json.load(f)
            # if you wanted to read the file as bytes
            bytes = f.read()
            # then maybe hash for whatever reason
            readable_hash = hashlib.sha256(bytes).hexdigest()
            # maybe you wanna write a response to a file
            r = requests.get("https://google.com", auth={auth_thing}, verify=False, headers=headers)
            for chunk in r.iter_content(chunk_size=8192):
                # this is if it's encoded in chunks
                # if it's not I think you just set chunk_size to None
                f.write(chunk)
            # maybe you want to add a breakpoint
            # breakpoint()
            return readable_hash




if __name__ == '__main__':
    # subprocess.run("/some/config/script/in/shell/script.sh")
    app.run(debug=True, host='0.0.0.0', port=port)