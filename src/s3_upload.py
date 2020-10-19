import boto3
import os

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

if __name__ == "__main__":
    s3.Bucket('Ru_apps_table_bucket').upload_file(Filename='apps.csv.gzip', Key='apps.csv.gzip')
