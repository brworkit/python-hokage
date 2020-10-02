import boto3
import json

def enqueue(queue_name, payload):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_name,
        MessageAttributes=payload["attributes"],
        MessageBody=json.dumps(payload["body"])
    )
    return response

def delete_message(queue_url, record):
    sqs = boto3.client('sqs')
    return sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=record['receiptHandle'])

def is_there_notification(context):
    return 'Records' in context and len(context) >= 1