from telegram.ext import ApplicationBuilder, ContextTypes, JobQueue
import datetime
import pytz

async def scheduled_message(context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = '1490785771'  # Replace with the actual chat ID
    await context.bot.send_message(chat_id=chat_id, text="It's time")

if __name__ == '__main__':
    # Initialize the bot with the provided token
    application = ApplicationBuilder().token('7283944645:AAHhp91P8BPEKFOSUqJtktzuQ_2sNWFWaj0').build()

    # Get the JobQueue instance
    job_queue = application.job_queue

    # Define the time zone (IST)
    ist = pytz.timezone('Asia/Kolkata')

    # Define the time when the message should be sent (6:54 PM IST)
    time_to_send = datetime.time(hour=19, minute=10, tzinfo=ist)

    # Schedule the job
    job_queue.run_daily(scheduled_message, time_to_send)

    # Start the bot
    application.run_polling()
