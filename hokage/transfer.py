import boto3
import json

class Transfer():
    def __init__(self, region):
        self.client = boto3.client('transfer', region_name=region)

    def exists_user(self, server_id, user_name):
        try:
            return self.describe_user(server_id=server_id, user_name=user_name) is not None
        except self.client.ResourceNotFoundException:
            return False

    def describe_user(self, server_id, user_name):
        return self.client.describe_user(
            ServerId=server_id,
            UserName=user_name
        )

    def create_user(self, user_name, role, ssh_public_key_body, server_id, home_directory_type, home_directory_mappings):
        return self.client.create_user(
            UserName=user_name,
            Role=role,
            SshPublicKeyBody=ssh_public_key_body,
            ServerId=server_id,
            HomeDirectoryType=home_directory_type,
            HomeDirectoryMappings=home_directory_mappings
        )
