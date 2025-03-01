import boto3

from configs.configs import NO_MFA_USER_FILE
from utils.file_handler import FileHandler


class MFAHandler:
    def __init__(self):
        self.iam_client = boto3.client('iam')

    def list_iam_users(self):
        return self.iam_client.list_users()['Users']

    def get_users_with_mfa_not_enabled(self):
        print('Collecting no MFA users started...')
        users = self.list_iam_users()
        no_mfa_users = []
        for user in users:
            iam_user = user['UserName']
            res = self.iam_client.list_mfa_devices(UserName=iam_user)

            if not res['MFADevices']:
                print(f'MFA not enabled user: {iam_user}')
                no_mfa_users.append(iam_user)
        return no_mfa_users

    def save_no_mfa_users_into_file(self):
        no_mfa_users = self.get_users_with_mfa_not_enabled()
        file_handler = FileHandler()
        file_handler.write_csv_file(NO_MFA_USER_FILE, no_mfa_users)

