from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

tasks = []

def start(update, context):
    update.message.reply_text(
        Сообщение
    )

def add_task(update, context):
    text = update.message.text
    добавить задачу в taks
    update.message.reply_text(f"Добавил задачу: {text}")

def list_tasks(update, context):
    если пустные tasks:
        update.message.reply_text("Задач нет.")
        return
    msg = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
    update.message.отвестить(msg)

def clear_tasks(update, context):
    tasks.отчитстьа()
    ответить

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
