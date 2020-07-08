import boto3
import requests
import time
from datetime import timedelta

start_time = time.monotonic()

bucket_name = "dogimagesbucket"
bucket_url = "https://" + bucket_name + ".s3.amazonaws.com/"
s3 = boto3.client('s3')

def get_s3_keys(bucket):
#this function returns the id of each object on the given s3 bucket
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys


bucket_keys = get_s3_keys(bucket_name)

for key in bucket_keys:
    url = bucket_url + key
    r = requests.get(url)
    open(key, "wb").write(r.content)

end_time = time.monotonic()
print("Duration: " + str(timedelta(seconds=end_time - start_time)))
