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
    keyboard = [
        [InlineKeyboardButton("📊 فتح حساب تداول", url="https://t.me/your_channel")],
        [InlineKeyboardButton("💬 الدعم الفني", url="https://t.me/your_support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً بك في بوت M.A Broker للخدمات المالية والتداول! 📈\nاختر من القائمة أدناه:",
        reply_markup=reply_markup
    )

def main():
    # تشغيل سيرفر الـ HTTP في الخلفية
    Thread(target=run_http_server, daemon=True).start()

    # تشغيل بوت التلغرام
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
