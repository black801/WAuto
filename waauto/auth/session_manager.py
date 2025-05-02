import os
import json

from waauto.utils.logger import logger

SESSIONS_DIR = "sessions"

class SessionManager:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.session_file = os.path.join(SESSIONS_DIR, f"{self.phone_number}.json")
        os.makedirs(SESSIONS_DIR, exist_ok=True)

    def save_session(self, session_data: dict):
        try:
            with open(self.session_file, "w") as f:
                json.dump(session_data, f)
            logger.success(f"تم حفظ الجلسة للرقم {self.phone_number}")
        except Exception as e:
            logger.error(f"فشل في حفظ الجلسة: {e}")

    def load_session(self):
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, "r") as f:
                    data = json.load(f)
                logger.info(f"تم تحميل الجلسة للرقم {self.phone_number}")
                return data
            except Exception as e:
                logger.error(f"فشل في قراءة الجلسة: {e}")
                return None
        else:
            logger.warning(f"لا توجد جلسة محفوظة للرقم {self.phone_number}")
            return None

    def delete_session(self):
        if os.path.exists(self.session_file):
            os.remove(self.session_file)
            logger.info(f"تم حذف الجلسة للرقم {self.phone_number}")
        else:
            logger.warning(f"لا توجد جلسة لحذفها للرقم {self.phone_number}")