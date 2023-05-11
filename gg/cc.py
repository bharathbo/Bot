import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

CHOOSING, SUBJECTS, MARKS, CREDITS = range(4)

# Create a Telegram bot object
bot = telegram.Bot(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU')

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am your CGPA/Percentage calculator bot. Please click on the appropriate button below to get started.")
    # Create CGPA and Percentage buttons
    keyboard = [[InlineKeyboardButton("CGPA", callback_data='CGPA'),
                 InlineKeyboardButton("Percentage", callback_data='Percentage')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the buttons to the user
    update.message.reply_text('Please select one of the following:', reply_markup=reply_markup)
    return CHOOSING

# Define a function to handle the CGPA and Percentage buttons
def choose_calculation_type(update, context):
    query = update.callback_query
    query.answer()
    context.user_data['calculation_type'] = query.data
    context.bot.send_message(chat_id=update.effective_chat.id, text="How many subjects do you have?")
    # Change the handler to the num_subjects function
    return SUBJECTS

# Define a function to handle the number of subjects message
def add_subject(update, context):
    num_subjects = int(update.message.text)
    context.user_data['num_subjects'] = num_subjects
    context.user_data['marks'] = []
    context.user_data['credits'] = []
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your marks and credits for each subject one by one, separated by a space.")
    # Change the handler to the marks function
    return MARKS

# Define a function to handle the marks and credits for each subject
def add_marks(update, context):
    marks = context.user_data.get('marks')
    if marks is None:
    # handle the case where the key is not presen
     credits = context.user_data['credits']
    user_input = update.message.text.split()
    if len(user_input) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your marks and credits for each subject one by one, separated by a space.")
        return MARKS
    try:
        marks.append(float(user_input[0]))
        credits.append(float(user_input[1]))
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter valid marks and credits for each subject one by one, separated by a space.")
        return MARKS

    if len(marks) < context.user_data['num_subjects']:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the marks and credits for the next subject.")
        return MARKS
    else:
        if context.user_data['calculation_type'] == 'CGPA':
            total_marks = sum([marks[i]*credits[i] for i in range(len(marks))])
            total_credits = sum(credits)
            cgpa = total_marks/total_credits
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your CGPA is {cgpa:.2f}")
        else:
            total_marks = sum(marks)
            total_credits = sum(credits)
            percentage = (total_marks/total_credits)*100
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your percentage is {percentage:.2f}%")
                # Reset user_data for the next user
            context.user_data.clear()
            return ConversationHandler.END

def cancel(update, context):
    context.user_data.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bye! Hope to see you again soon.")
    return ConversationHandler.END

updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)
dispatcher = updater.dispatcher

# Add handlers for the /start, CGPA and Percentage buttons, and unknown commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(choose_calculation_type))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, add_marks))
dispatcher.add_handler(MessageHandler(Filters.command, add_subject))
dispatcher.add_handler(MessageHandler(Filters.command, cancel))


# Start the bot
updater.start_polling()
