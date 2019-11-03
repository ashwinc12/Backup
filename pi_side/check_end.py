import os
from google.cloud import storage
for fname in os.listdir('.'):
    if fname.endswith('.mp4'):
        # do stuff on the file
        client = storage.Client()
        # https://console.cloud.google.com/storage/browser/[bucket-id]/
        bucket = client.get_bucket('class-hub-bucket')
        # Then do other things...
        blob2 = bucket.blob('remote/path/output.mp4')
        blob2.upload_from_filename(filename='/home/class-hub1/output.mp4')
        os.remove('output.mp4')
        break