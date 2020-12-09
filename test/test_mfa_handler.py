from mfa.mfa_handler import MFAHandler


class TestMFAHandler:
    def test_save_no_mfa_users_into_file(self):
        mfa_handler = MFAHandler()
        mfa_handler.save_no_mfa_users_into_file()