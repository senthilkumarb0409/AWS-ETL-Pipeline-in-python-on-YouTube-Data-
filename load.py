import os
import boto3
from botocore.exceptions import NoCredentialsError


bucket_name = "etlpipelinedataonyoutubedata"  
object_name = "sample.xlsx"  


s3_client = boto3.client('s3')


def upload_to_s3(file_path, bucket, object_name):
    try:
        
        s3_client.upload_file(file_path, bucket, object_name)
        print(f"File {file_path} successfully uploaded to {bucket}/{object_name}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


if __name__ == "__main__":
    
    excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video_details.xlsx")
    
    
    if os.path.exists(excel_file_path):
        upload_to_s3(excel_file_path, bucket_name, object_name)
    else:
        print(f"Excel file {excel_file_path} does not exist. Please ensure transform.py has run successfully.")
