import datetime
import json
import os
from dotenv import load_dotenv
from flask import Response
from notion.client import NotionClient

load_dotenv()

client = NotionClient(os.getenv("TOKEN_V2"))


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)


def read_notion_view(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = json.loads(request.data)

    organization = request_json.get("organization")
    if organization is None:
        raise ValueError("Organization is required")

    database_id = request_json.get("database-id")
    if database_id is None:
        raise ValueError("Database ID is required")

    view_id = request_json.get("view-id")
    if view_id is None:
        raise ValueError("View ID is required")

    cv = client.get_collection_view(
        f"https://www.notion.so/{organization}/{database_id}?v={view_id}"
    )

    res: list[dict] = []

    for row in cv.collection.get_rows():
        res.append(row.get_all_properties())

    return Response(
        json.dumps(res, cls=DateTimeEncoder), status=200, mimetype="application/json"
    )
