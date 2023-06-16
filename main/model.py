from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class MyEC2Setting(BaseModel):
    ACCESS_KEY = os.getenv('ACCESS_KEY', 'your_access_key')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    AMI_ID = os.getenv('AMI_ID', 'your_ami_id')
    INSTANCE_TYPE = os.getenv('INSTANCE_TYPE', 'your_instance_type')

    KEY_NAME = os.getenv('KEY_NAME', 'your_key_name')
    REGION_NAME = os.getenv('REGION_NAME', 'your_region_name')
    PEM_FILE_ADDRESS = os.getenv('PEM_FILE_ADDRESS', 'your_pem_file_address')
    SSH_USER = os.getenv('SSH_USER', 'your_ssh_user')


class Setting(BaseModel):
    EC2: MyEC2Setting = MyEC2Setting()


SETTING = Setting()
