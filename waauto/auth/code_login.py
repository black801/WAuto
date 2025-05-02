import time
import random

from waauto.utils.logger import logger
from waauto.auth.session_manager import SessionManager

class CodeLogin:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.session_manager = SessionManager(phone_number)

    def request_code(self):
        """
        محاكاة إرسال كود إلى الهاتف
        """
        self.generated_code = str(random.randint(100000, 999999))
        logger.info(f"تم إرسال كود التحقق {self.generated_code} إلى الرقم {self.phone_number}")
        return self.generated_code

    def verify_code(self, code: str):
        """
        تحقق من الكود المرسل
        """
        if code == self.generated_code:
            logger.success(f"تم تسجيل الدخول بنجاح للرقم {self.phone_number}")
            self.session_manager.save_session({"phone": self.phone_number, "session": f"session_{int(time.time())}"})
            return True
        else:
            logger.error("فشل في التحقق من الكود")
            return False