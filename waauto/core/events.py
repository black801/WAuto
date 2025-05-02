from waauto.utils.logger import logger

class EventHandler:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message_data: dict):
        sender = message_data.get("sender")
        text = message_data.get("text")

        if not sender or not text:
            logger.warning("تم استقبال رسالة غير صالحة.")
            return

        logger.info(f"رسالة جديدة من {sender}: {text}")

        # رد تلقائي تجريبي
        if "مرحبا" in text or "hello" in text.lower():
            await self.client.send_message(sender, "أهلاً بك! كيف يمكنني مساعدتك؟")

    async def on_connect(self):
        logger.success("تم الاتصال بنجاح بحساب واتساب.")

    async def on_disconnect(self):
        logger.warning("تم فصل الاتصال من واتساب.")