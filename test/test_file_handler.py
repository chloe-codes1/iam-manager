from utils.file_handler import FileHandler
from configs.configs import NO_MFA_USER_FILE


class TestFileHandler:

    def test_write_csv_file(self):
        no_mfa_users = ['dummy', 'dum', 'duh']
        file_handler = FileHandler()
        file_handler.write_csv_file(NO_MFA_USER_FILE, no_mfa_users)

