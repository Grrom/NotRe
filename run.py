import json
import os

from requests import Request

from dotenv import load_dotenv

from function import read_notion_view


load_dotenv()

test_body = {
    "organization": os.getenv("TEST_NOTION_ORGANIZATION"),
    "database-id": os.getenv("TEST_NOTION_DATABASE_ID"),
    "view-id": os.getenv("TEST_NOTION_VIEW_ID"),
}

request = Request(
    method="POST",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    headers={"Content-Type": "application/json", "Authorization": os.getenv("TOKEN_V2")}, 
    data=json.dumps(test_body),
)


read_notion_view(request)
