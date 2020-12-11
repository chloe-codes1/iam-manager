from mfa.mfa_handler import MFAHandler

if __name__ == "__main__":
    mfa_handler = MFAHandler()
    mfa_handler.save_no_mfa_users_into_file()
    