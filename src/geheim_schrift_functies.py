import json
import src.geheim_schrift

def versleutel(event, context):
    request = json.loads(event['body'])
    body = {
        "resultaat": src.geheim_schrift.versleutel_zin(request['zin'], request['sleutel'])
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps(body)
    }

    return response

def ontsleutel(event, context):
    request = json.loads(event['body'])
    body = {
        "resultaat": src.geheim_schrift.ontsleutel_zin(request['zin'], request['sleutel'])
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps(body)
    }

    return response
