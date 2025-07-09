import logging
from io import StringIO, BytesIO
from minio import Minio
from minio.error import S3Error
import datetime
from app_constants import *

# In-memory log buffer
log_buffer = StringIO()

# Configure logger
log_handler = logging.StreamHandler(log_buffer)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

logger = logging.getLogger("SilverLoader")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.addHandler(logging.StreamHandler())  # Optional: Also log to stdout

# Upload logs from buffer to MinIO
def flush_logs_to_minio(object_name):
    try:
        client = Minio(
            MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False  # Set to True if using HTTPS
        )
        if not client.bucket_exists(MINIO_BUCKET):
            client.make_bucket(MINIO_BUCKET)

        content = log_buffer.getvalue().encode("utf-8")
        client.put_object(
            MINIO_BUCKET,
            object_name,
            data=BytesIO(content),
            length=len(content),
            content_type='text/plain'
        )
        logger.info(f"Uploaded log to MinIO at {MINIO_BUCKET}/{object_name}")
        
        # Clear the buffer after upload
        log_buffer.truncate(0)
        log_buffer.seek(0)
        
    except S3Error as e:
        logger.error(f"Failed to upload log: {e}")