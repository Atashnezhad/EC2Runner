import unittest
from main.ec2_runner import MyEC2
from main.model import SETTING


class TestEC2Runner(unittest.TestCase):

    def setUp(self) -> None:
        self.my_ec2_object = MyEC2()
        self.setting = SETTING

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

