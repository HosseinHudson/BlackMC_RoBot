import json
import os
from datetime import datetime, timedelta
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7692983748:AAGIrTGrR6rstOAoIwg_ElI6MxSWXQBxrVQ"
ADMIN_ID = 5938039998
BOT_USERNAME = "BlackMC_RoBot"
DATA_FILE = "users.json"


if not os.path.exists(DATA_FILE):
with open(DATA_FILE, "w", encoding="utf-8") as f:
json.dump({}, f, ensure_ascii=False)


def get_iran_date():
now = datetime.utcnow()
iran_time = now + timedelta(hours=3, minutes=30)
return iran_time.strftime("%Y/%m/%d")


def save_user(user_id, username):
with open(DATA_FILE, "r", encoding="utf-8") as f:
data = json.load(f)

user_id = str(user_id)
if user_id not in data:
data[user_id] = {
"username": username or "",
"coins": 0,
"invited": 0,
"join_date": get_iran_date()
}

with open(DATA_FILE, "w", encoding="utf-8") as f:
json.dump(data, f, ensure_ascii=False)


def get_user_data(user_id):
with open(DATA_FILE, "r", encoding="utf-8") as f:
data = json.load(f)
return data.get(str(user_id), None)


def get_main_menu():
buttons = [
[KeyboardButton("🌐 آیپی سرور")],
[KeyboardButton("👤 حساب کاربری"), KeyboardButton("🛒 خرید رنک")],
[KeyboardButton("🎧 ارتباط با پشتیبانی"), KeyboardButton("🚨 ثبت گزارش")]
]
return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
user = update.effective_user
save_user(user.id, user.username)
await update.message.reply_text(
"🎮 به ربات رسمی سرور BlackMC خوش اومدی!\n\n"
"📌 از طریق منو می‌تونی:\n"
"🌐 آی‌پی سرور رو بگیری\n"
"🧾 حساب کاربری ببینی\n"
"🛒 رنک بخری\n"
"🚨 گزارش بدی\n"
"🎧 با پشتیبانی در ارتباط باشی\n\n"
"📢 کانال رسمی ما: @BlackMC_Channel",
reply_markup=get_main_menu()
)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = update.message.text
user = update.effective_user
save_user(user.id, user.username)

if text == "🌐 آیپی سرور":
await update.message.reply_text(
"🌐 آی‌پی سرور BlackMC:\n\n"
"Hossein_Hudson.aternos.me:60000\n\n"
"سرور از تمامی ورژن‌های محبوب ماینکرافت پشتیبانی می‌کند.\n"
"با ما بیای بازی کنیم و خوش بگذرونیم! 🎮✨"
)

elif text == "👤 حساب کاربری":
data = get_user_data(user.id)
if data:
await update.message.reply_text(
f"👤 اطلاعات حساب کاربری شما:\n\n"
f"🆔 آیدی: @{user.username or 'ندارد'}\n"
f"🪙 تعداد سکه‌ها: {data['coins']}\n"
f"📅 تاریخ عضویت: {data['join_date']}\n"
f"👥 تعداد دعوت شده‌ها: {data['invited']}\n\n"
f"📢 برای دیدن لینک دعوت خود روی «📢 زیرمجموعه‌گیری» بزنید.",
reply_markup=ReplyKeyboardMarkup([
[KeyboardButton("📢 زیرمجموعه‌گیری")],
[KeyboardButton("🔙 برگشت به منو")]
], resize_keyboard=True)
)

elif text == "📢 زیرمجموعه‌گیری":
await update.message.reply_text(
f"📢 لینک دعوت شما:\n"
f"https://t.me/{BOT_USERNAME}?start=ref_{user.id}"
)

elif text == "🔙 برگشت به منو":
await update.message.reply_text("منوی اصلی 👇", reply_markup=get_main_menu())

elif text == "🎧 ارتباط با پشتیبانی":
await update.message.reply_text("برای ارتباط با پشتیبانی به آیدی زیر مراجعه کنید 👇\n@Hossein_Hudson")

elif text == "🚨 ثبت گزارش":
await update.message.reply_text("لطفاً پیام گزارش خود را ارسال کنید ✍️")
context.user_data["report_mode"] = True

elif text == "🛒 خرید رنک":
await update.message.reply_text("رنک مورد نظر را انتخاب کنید 👇", reply_markup=ReplyKeyboardMarkup([
[KeyboardButton("🤍Iron Rank🤍"), KeyboardButton("💛Gold Rank💛")],
[KeyboardButton("💙Diamond Rank💙"), KeyboardButton("💚Emerald Rank💚")],
[KeyboardButton("🖤Netherite Rank🖤"), KeyboardButton("🧡Phoenix Rank🧡")],
[KeyboardButton("🤍God Rank🤍"), KeyboardButton("💙Sponsor Rank💙")],
[KeyboardButton("🔙 برگشت به منو")]
], resize_keyboard=True))

elif text == "🤍Iron Rank🤍":
photo_file_id = "AgACAgQAAxkBAAIChGhJmib--LGuOqRsjTelrldyi4eTAAKIyzEbWaNQUg16XpAehpXIAQADAgADeAADNgQ"
caption = (
"🤍Iron Rank🤍\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Iron هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 1\n"
"Projectile Protection 1\n"
"Tools Enchant:\n"
"Efficiency 1\n"
"Sword Enchant:\n"
"Smite 1\n\n"
"Price : 30T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "💛Gold Rank💛":
photo_file_id = "AgACAgQAAxkBAAIChmhJnDt7s9VIVC9x0A9_3WjH5f2KAAKVyzEbWaNQUgvjSexaiZSSAQADAgADeQADNgQ"
caption = (
"💛Gold Rank💛\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Gold هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 2\n"
"Projectile Protection 2\n"
"Unbreaking 1\n"
"Tools Enchant:\n"
"Efficiency 2\n"
"Unbreaking 1\n"
"Sword Enchant:\n"
"Smite 2\n\n"
"Price : 65T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "💙Diamond Rank💙":
photo_file_id = "AgACAgQAAxkBAAICiGhJnEh7nTBimPd87nKKNy5NzbCDAAKWyzEbWaNQUg8dkx7xblCEAQADAgADeQADNgQ"
caption = (
"💙Diamond Rank💙\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Diamond هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 3\n"
"Projectile Protection 2\n"
"Unbreaking 2\n"
"Tools Enchant:\n"
"Efficiency 3\n"
"Unbreaking 2\n"
"Sword Enchant:\n"
"Smite 3\n\n"
"Price : 90T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "💚Emerald Rank💚":
photo_file_id = "AgACAgQAAxkBAAICjGhJngwwgP2heGBheEVsSvkP8XpAAKXyzEbWaNQUgvVhxSvi8dkAQADAgADeAADNgQ"
caption = (
"💚Emerald Rank💚\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Emerald هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 4\n"
"Projectile Protection 3\n"
"Unbreaking 3\n"
"Tools Enchant:\n"
"Efficiency 4\n"
"Unbreaking 3\n"
"Sword Enchant:\n"
"Smite 4\n\n"
"Price : 120T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "🖤Netherite Rank🖤":
photo_file_id = "AgACAgQAAxkBAAICkGhJnpnm-XNbsDMzC-lQVEfZ6QoRAALzyxEbWaNQUgyzkxQeE3TZAQADAgADeQADNgQ"
caption = (
"🖤Netherite Rank🖤\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Netherite هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 5\n"
"Projectile Protection 4\n"
"Unbreaking 4\n"
"Tools Enchant:\n"
"Efficiency 5\n"
"Unbreaking 4\n"
"Sword Enchant:\n"
"Smite 5\n\n"
"Price : 179T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "🧡Phoenix Rank🧡":
photo_file_id = "AgACAgQAAxkBAAICmGhJnuhSdOhxwdz5iAZh-2Zr9h9vAALozxEbWaNQUgLj3es4q-pjAQADAgADeQADNgQ"
caption = (
"🧡Phoenix Rank🧡\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Phoenix هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 6\n"
"Projectile Protection 5\n"
"Unbreaking 5\n"
"Tools Enchant:\n"
"Efficiency 6\n"
"Unbreaking 5\n"
"Sword Enchant:\n"
"Smite 6\n\n"
"Price : 219T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "🤍God Rank🤍":
photo_file_id = "AgACAgQAAxkBAAICnGhJnyV-DPpqlHHNvFv27LxaW7vRAALqzxEbWaNQUgsZC5eMYWrIAQADAgADeQADNgQ"
caption = (
"🤍God Rank🤍\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit God هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 7\n"
"Projectile Protection 6\n"
"Unbreaking 6\n"
"Tools Enchant:\n"
"Efficiency 7\n"
"Unbreaking 6\n"
"Sword Enchant:\n"
"Smite 7\n\n"
"Price : 289T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

elif text == "💙Sponsor Rank💙":
photo_file_id = "AgACAgQAAxkBAAICoGhJn5qG7MF9DZjoif66y4nqj7y3AAKszxEbWaNQUgoZJftrzZQPAQADAgADeQADNgQ"
caption = (
"💙Sponsor Rank💙\n"
"🌟Permissones🌟 :\n"
"Fly\n"
"Kit Sponsor هر 7 روز یک بار\n"
"🔱Item Enchants🔱 :\n"
"Armors Enchant:\n"
"Protection 8\n"
"Projectile Protection 7\n"
"Unbreaking 7\n"
"Tools Enchant:\n"
"Efficiency 8\n"
"Unbreaking 7\n"
"Sword Enchant:\n"
"Smite 8\n\n"
"Price : 389T"
)
await update.message.reply_photo(photo=photo_file_id, caption=caption)

else:
# پیام پیش‌فرض برای متن‌های ناشناخته
await update.message.reply_text("لطفاً یکی از گزینه‌های منو را انتخاب کنید.")

if name == "main":
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()

