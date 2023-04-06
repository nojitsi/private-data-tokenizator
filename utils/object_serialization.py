import json
import base64 

def serialize_array(arr):
  return base64.b64encode(json.dumps(arr).encode("ascii")).decode("ascii")

def deserialize_array(hash):
  return json.loads(base64.b64decode(hash.encode("ascii")).decode("ascii"))
