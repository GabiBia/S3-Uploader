This script allows you to upload a file into your S3 bucket. 
It contains three arguments: 
- '--file' - the name of target file in your S3 bucket
- '--path' - the path to your file
- '--bucket' - the name of the bucket, you want to upload your file to

Example of usage:

python3 S3uploader.py --path 'user/desktop/test.txt' --file 'test.txt' --bucket 'examplebucket'
