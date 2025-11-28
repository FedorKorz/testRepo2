from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

tasks = []

def start(update, context):
    update.message.reply_text(
        "Привет! Напиши задачу, и я её сохраню.\n"
        "/list — показать задачи\n"
        "/clear — очистить"
    )

def add_task(update, context):
    text = update.message.text
    tasks.append(text)
    update.message.reply_text(f"Добавил задачу: {text}")

def list_tasks(update, context):
    if not tasks:
        update.message.reply_text("Задач нет.")
        return
    msg = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
    update.message.reply_text(msg)

def clear_tasks(update, context):
    tasks.clear()
    update.message.reply_text("Все задачи удалены!")

def main():
    updater = Updater("8551731437:AAFvI5u9ZxCaohPaBUutAARB5nM9xih2cec", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("list", list_tasks))
    dp.add_handler(CommandHandler("clear", clear_tasks))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, add_task))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
