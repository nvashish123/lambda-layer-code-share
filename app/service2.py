import json
import customcode as cc


def lambda_handler(event, context):

    cc.cust_fun()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello from service2",
        }),
    }
