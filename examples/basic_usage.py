from waauto.auth.code_login import login_with_code
from waauto.auth.session_manager import save_session
from waauto.utils.logger import logger

def main():
    phone_number = input("Enter your WhatsApp phone number (e.g. +201000000000): ").strip()
    session = login_with_code(phone_number)
    
    if session:
        save_session(session)
        logger.info(f"Session saved for {phone_number}")
    else:
        logger.error("Login failed. Please try again.")

if __name__ == "__main__":
    main()