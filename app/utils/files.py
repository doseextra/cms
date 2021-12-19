import boto3
from os import environ


files_client = boto3.client(
    's3',
    region_name=environ.get('SAPCE_REGION') or '',
    endpoint_url='https://{}.digitaloceanspaces.com'.format(
        environ.get('SAPCE_REGION')),
    aws_access_key_id=environ.get('SPACE_ACCESS_ID') or '',
    aws_secret_access_key=environ.get('SPACE_ACCESS_SECRET') or ''
)


def save_files(file_name, file_content):
    files_client.put_object(
        Bucket='doseextra',
        Key=file_name,
        Body=file_content
    )


def delete_file(file_name):
    files_client.delete_object(
        Bucket='doseextra',
        Key=file_name
    )


def get_all_files():
    remote = files_client.list_objects(
        Bucket=environ.get('SPACE_NAME'),
        Prefix=environ.get('SPACE_PREFIX')
    )
    return remote.get('Contents')
