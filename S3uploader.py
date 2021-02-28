# Connection to AWS
import boto3
import argparse

s3 = boto3.resource('s3')

# Parsers
parser = argparse.ArgumentParser()  # Use ArgumentParser class

file = parser.add_argument('--file', type=str)  # Use add_argument function to create a variable
path = parser.add_argument('--path', type=str)
bucket = parser.add_argument('--bucket', type=str)

args = parser.parse_args()  # parse all variables

# Upload a file
s3uploader = s3.meta.client.upload_file(args.path, args.bucket, args.file)  # with value of arguments
print('done')
