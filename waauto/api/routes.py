import os
from flask import Blueprint, jsonify
from waauto.core.client import WhatsAppClient

# قراءة رقم الهاتف من المتغير البيئي WAUTO_PHONE
phone_number = os.getenv("WAUTO_PHONE", "0123456789")  # رقم افتراضي في حالة غياب المتغير

client = WhatsAppClient(phone_number=phone_number)

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return jsonify({"message": "WAuto WhatsApp API is running"})

@routes.route("/status")
def status():
    return jsonify({"status": "ready", "client": str(client)})