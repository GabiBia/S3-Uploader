# Connection to AWS
import boto3

s3 = boto3.resource('s3')
# Upload a file
path = '/Users/gbialoskorska/desktop/certificates/test.txt'
file = 'test.txt'
bucket = 'gabibiacertificates'

s3uploader = s3.meta.client.upload_file(path, bucket, file)

print("done")

# TODO: Bucket as a variable - argument feature
# TODO: File as an argument feature

