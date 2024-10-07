import json
from urllib.request import Request

from dotenv import load_dotenv
from function import do_something

load_dotenv()

request = Request(
    method="POST",
    url="http://testinglang.com",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"data": "hello-world"}),
)

do_something(request)
