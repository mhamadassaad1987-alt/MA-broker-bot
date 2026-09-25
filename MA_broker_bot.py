import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- سيرفر HTTP وهمي لإرضاء نظام Render ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"M.A Broker Bot is Online!")

def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# --- بيانات البوت ---
TOKEN = "8895944449:AAEtJYCSz9RXld1xmSljjgirnE10xSkz3sM"

# --- الأوامر الرئيسية ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # رابط الواتساب المباشر לרقم 71229665
    whatsapp_url = "https://wa.me/96171229665?text=%D8%A3%D9%87%D9%84%D8%A7%D9%8B%20%D8%A3%D8%A8%D9%88%20%D9%82%D8%A7%D8%B3%D9%85%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1%20%D8%B9%D9%86%20%D8%AE%D8%AF%D9%85%D8%A7%D8%AA%20M.A%20Broker"
    
    # رابط حساب التليجرام المباشر عبر الرقم / اليوزر
    telegram_account = "https://t.me/+96171229665"  # يمكنك استبدال "+96171229665" بـ اليوزر الخاص بك إذا كان متوفراً (مثل https://t.me/your_username)

    keyboard = [
        [InlineKeyboardButton("📱 التواصل عبر الواتساب (71229665)", url=whatsapp_url)],
        [InlineKeyboardButton("💬 التواصل عبر التليجرام (Abou kassem)", url=telegram_account)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً بك في بوت M.A Broker للخدمات المالية والتداول! 📈\nمرحباً بك مع **Abou kassem**، اختر إحدى الطرق أدناه للتواصل المباشر معنا:",
        reply_markup=reply_markup
    )

def main():
    Thread(target=run_http_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
