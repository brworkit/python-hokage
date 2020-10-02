import boto3

def create_bucket_with_options(bucket_name, tag_set, server_side_encryption_rules, acl='private'):
    s3_resource = boto3.resource('s3')

    response_bucket_create = s3_resource.create_bucket(
        ACL=acl,
        Bucket=bucket_name
    )

    s3_client = boto3.client('s3')

    response_bucket_tagging = s3_client.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': tag_set,
        },
    )

    response_bucket_encryption = s3_client.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': server_side_encryption_rules
        }
    )

    return response_bucket_create, response_bucket_tagging, response_bucket_encryption
