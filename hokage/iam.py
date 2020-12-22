import boto3
import json


def create_policy():
    print("create_policy")

    """
    docstring
    """
    client = boto3.client('iam', region_name="us-east-1")

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowListingOfUserFolder",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetBucketLocation"
                ],
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::data-request-boticario-dev"
                ]
            },
            {
                "Sid": "HomeDirObjectAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:GetObjectVersion"
                ],
                "Resource": "arn:aws:s3:::data-request-boticario-dev/*"
            }
        ]
    }

    response = client.create_policy(
        PolicyName='DataSetupTestPolicy',
        PolicyDocument=json.dumps(policy)
    )

    print(response)


async def funcname(parameter_list):

    pass

if __name__ == "__main__":
    create_policy()
