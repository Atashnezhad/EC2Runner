import unittest
from main.ec2_runner import MyEC2
from main.model import SETTING
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TestEC2Runner(unittest.TestCase):

    def setUp(self) -> None:
        self.my_ec2_object = MyEC2()
        self.setting = SETTING
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def tearDown(self) -> None:
        pass

    def test_check_envs(self):
        # check if envs are set
        self.assertIsNotNone(self.setting.EC2.ACCESS_KEY)
        self.assertIsNotNone(self.setting.EC2.SECRET_KEY)
        self.assertIsNotNone(self.setting.EC2.AMI_ID)
        self.assertIsNotNone(self.setting.EC2.INSTANCE_TYPE)
        self.assertIsNotNone(self.setting.EC2.KEY_NAME)
        self.assertIsNotNone(self.setting.EC2.REGION_NAME)
        self.assertIsNotNone(self.setting.EC2.PEM_FILE_ADDRESS)
        self.assertIsNotNone(self.setting.EC2.SSH_USER)

    def test_print_envs(self):
        print(self.setting.EC2.ACCESS_KEY)
        self.logger.info(self.setting.EC2.SECRET_KEY)
        self.logger.info(self.setting.EC2.AMI_ID)
        self.logger.info(self.setting.EC2.INSTANCE_TYPE)
        self.logger.info(self.setting.EC2.KEY_NAME)
        self.logger.info(self.setting.EC2.REGION_NAME)
        self.logger.info(self.setting.EC2.PEM_FILE_ADDRESS)
        self.logger.info(self.setting.EC2.SSH_USER)
