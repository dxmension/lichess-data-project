import os
import json
import boto3
from typing import Any
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AWS_SERVER_PUBLIC_KEY = os.environ.get("AWS_SERVER_PUBLIC_KEY", "")
AWS_SERVER_SECRET_KEY = os.environ.get("AWS_SERVER_SECRET_KEY", "")

class S3Service:
    def __init__(self, bucket_name: str, region_name: str = "eu-north-1"):
        self.bucket_name = bucket_name
        self.session = boto3.Session(
            aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
            aws_secret_access_key=AWS_SERVER_SECRET_KEY,
            region_name=region_name
        )
        self.s3_client = self.session.resource("s3")
    
    def upload_json(self, data: Any, prefix: str, filename: str) -> str:
        key = f"{prefix}/{filename}.json"
        obj = self.s3_client.Object(self.bucket_name, key)

        obj.put(
            Body=json.dumps(data, ensure_ascii=False).encode("UTF-8"),
            ContentType="application/json"
        )

        return key