import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-1',
    aws_access_key_id='mykey',
    aws_secret_access_key='mysecretkey'
)

if __name__ == "__main__":
    s3.Bucket('Ru_apps_table_bucket').upload_file(Filename='apps.csv', Key='apps.csv')
