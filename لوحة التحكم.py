import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ⚠️ حط التوكن الجديد هنا (بعد ما تعمل Revoke للقديم من @BotFather)
TOKEN = "7654700777:AAEjka2tiZV7DlrRgXWdfquf7OOw5nkNuKw"

# إعداد اللوجات
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ==================== أوامر البوت ====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """الترحيب عند ضغط /start"""
    user = update.effective_user
    name = user.first_name or "صديقي"

    keyboard = [
        [InlineKeyboardButton("📢 قناتنا", url="https://t.me/telegram")],
        [
            InlineKeyboardButton("ℹ️ عن البوت", callback_data="about"),
            InlineKeyboardButton("🎁 هدية", callback_data="gift"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        f"أهلاً وسهلاً يا <b>{name}</b> 👋\n\n"
        f"🎉 نورت البوت!\n"
        f"اضغط على الأزرار اللي تحت عشان تبدأ 👇"
    )

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode="HTML",
    )
    logger.info(f"مستخدم جديد: {user.id} - {name}")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """الأوامر المتاحة"""
    await update.message.reply_text(
        "📋 <b>الأوامر المتاحة:</b>\n\n"
        "/start - بدء البوت 🚀\n"
        "/help - المساعدة ❓",
        parse_mode="HTML",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """التعامل مع الأزرار التفاعلية"""
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(
            "🤖 <b>عن البوت</b>\n\n"
            "بوت تجريبي معمول بـ Python ❤️\n"
            "باستخدام مكتبة python-telegram-bot",
            parse_mode="HTML",
        )
    elif query.data == "gift":
        await query.edit_message_text(
            "🎁 مبروك! خد الهدية دي:\n\n🍬🍭🍫",
        )


# ==================== التشغيل ====================

def main():
    if "حط_التوكن" in TOKEN:
        print("❌ لازم تحط التوكن بتاعك في متغير TOKEN!")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ البوت شغّال... اضغط Ctrl+C للإيقاف")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()