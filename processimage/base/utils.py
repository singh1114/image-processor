import os

import boto3

from django.conf import settings


def get_joined_path(image_path: tuple, filename: str):
    full_path = ''
    for a in image_path:
        full_path = os.path.join(full_path, a)

    return os.path.join(full_path, filename)


def add_media_to_path(file_path):
    return os.path.join('media', file_path)


def upload_image(file, file_path):
    s3 = boto3.resource(
        's3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
    bucket.put_object(
        Body=file.getvalue(), Key=add_media_to_path(file_path))
    return file_path
