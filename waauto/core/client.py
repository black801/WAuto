import asyncio
from waauto.utils.logger import logger
from waauto.auth.session_manager import SessionManager

class WhatsAppClient:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.session_manager = SessionManager(phone_number)
        self.session = None

    async def connect(self):
        logger.info(f"جاري الاتصال بحساب واتساب للرقم {self.phone_number}...")

        session_data = self.session_manager.load_session()
        if session_data:
            self.session = session_data
            logger.success("تم استعادة الجلسة بنجاح.")
        else:
            logger.warning("لا توجد جلسة محفوظة. تحتاج إلى تسجيل الدخول أولاً.")

    async def send_message(self, chat_id: str, message: str):
        if not self.session:
            logger.error("لم يتم الاتصال بالحساب بعد.")
            return

        # محاكاة إرسال الرسالة
        logger.info(f"تم إرسال الرسالة إلى {chat_id}: {message}")
        # هنا يتم دمج الكود الفعلي للعميل الحقيقي لاحقاً

    async def logout(self):
        self.session_manager.delete_session()
        self.session = None
        logger.info("تم تسجيل الخروج من الحساب.")

    def is_connected(self):
        return self.session is not None