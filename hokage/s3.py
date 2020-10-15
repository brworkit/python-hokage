import boto3

DEFAULT_LOCATION = 'us-east-1'

def create_bucket_with_options(bucket_name,
                               tag_set,
                               server_side_encryption_rules,
                               acl='private',
                               region='us-east-1',
                               enable_versioning=False,
                               location_constraint=DEFAULT_LOCATION):

    print("create_bucket_with_options")
    print(f"bucket_name: {bucket_name}")
    print(f"region: {region}")
    print(f"enable_versioning: {enable_versioning}")
    print(f"location_constraint: {location_constraint}")

    s3_resource = boto3.resource('s3', region_name=region)

    response_bucket_create = None

    if location_constraint == DEFAULT_LOCATION:
        response_bucket_create = s3_resource.create_bucket(
            ACL=acl,
            Bucket=bucket_name
        )
    else:
        response_bucket_create = s3_resource.create_bucket(
            ACL=acl,
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region}
        )


    if enable_versioning:
        bkt_versioning = s3_resource.BucketVersioning(bucket_name)
        bkt_versioning.enable()

    s3_client = boto3.client('s3', region_name=region)

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
