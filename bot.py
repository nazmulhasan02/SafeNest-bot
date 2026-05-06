from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "Your token here"

# 🧠 memory store (user-wise history)
user_history = {}

def get_menu():
    keyboard = [
        [InlineKeyboardButton(" What type of Service", callback_data="service type")],
        [InlineKeyboardButton(" Delivery Time", callback_data="delivery time")],
        [InlineKeyboardButton(" Payment method ", callback_data="payment method")],
        [InlineKeyboardButton(" Refund policy", callback_data="refund policy")],
        [InlineKeyboardButton("Visit Facebook page", callback_data="facebook page")],
        [InlineKeyboardButton(" Show History", callback_data="check history")]
    ]
    return InlineKeyboardMarkup(keyboard)

def save_history(user_id, text):
    if user_id not in user_history:
        user_history[user_id] = []
    user_history[user_id].append(text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Safe Nest  \n 👋 আমাদের সম্পর্কে বিস্তারিত জানতে নিচের অপশন পছন্দ করুন",
        reply_markup=get_menu()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data

     # facebook
    if data == "facebook page":
        text = "https://www.facebook.com/safe.nest.0"
        save_history(user_id, text)

        await query.message.reply_text(text)
        await query.message.reply_text("👇  menu:", reply_markup=get_menu())

     # 🚚service type
    if data == "service type":
        text = "help to find trusted home"
        save_history(user_id, text)

        await query.message.reply_text(text)
        await query.message.reply_text("👇  menu:", reply_markup=get_menu())

    # 🚚 Delivery
    if data == "delivery time":
        text = " Delivery time: 2-3 days"
        save_history(user_id, text)

        await query.message.reply_text(text)
        await query.message.reply_text("👇  menu:", reply_markup=get_menu())

    # 💳 Payment
    elif data == "payment method":
        text = " Payment via: Bkash / Nagad / Cash"
        save_history(user_id, text)

        await query.message.reply_text(text)
        await query.message.reply_text("👇 menu:", reply_markup=get_menu())

    # 🔄 Refund
    elif data == "refund policy":
        text = " Refund available within 3 days"
        save_history(user_id, text)

        await query.message.reply_text(text)
        await query.message.reply_text("👇  menu:", reply_markup=get_menu())

    # 📜 History
    elif data == "check history":
        history = user_history.get(user_id, [])

        if not history:
            await query.message.reply_text("No history yet 😅")
        else:
            msg = "📜 Your History:\n\n" + "\n".join(history)
            await query.message.reply_text(msg)

        await query.message.reply_text("👇  menu:", reply_markup=get_menu())

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")
app.run_polling()