import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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

# Define a function to handle the CGPA and Percentage buttons
def button(update, context):
    query = update.callback_query
    query.answer()
    context.user_data['calculation_type'] = query.data
    context.user_data['marks'] = []  # initialize an empty list for marks
    context.bot.send_message(chat_id=update.effective_chat.id, text="How many subjects do you have?")


# Define a function to handle the number of subjects message
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Define a function to handle the number of subjects message
def num_subjects(update, context):
    num_subjects = int(update.message.text)
    context.user_data['num_subjects'] = num_subjects
    context.user_data['marks'] = []
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your marks for each subject one by one.")

# Define a function to handle the marks message
def marks(update, context):
    marks = context.user_data['marks']
    credits = context.user_data.get('credits', [])  # use get() to handle missing 'credits' key
    user_input = update.message.text.split()
    if len(user_input) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your marks and credits for each subject one by one, separated by a space.")
        return
    try:
        marks.append(int(user_input[0]))
        credits.append(int(user_input[1]))
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter valid marks and credits for each subject one by one, separated by a space.")
        return

    if len(marks) < context.user_data['num_subjects']:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your marks and credits for the next subject.")
    else:
        # calculate CGPA or Percentage and send it to the user
        result = calculate_cgpa(marks, credits) if context.user_data['calculation_type'] == 'CGPA' else calculate_percentage(marks, credits)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your {context.user_data['calculation_type']} is: {result:.2f}")

def calculate_cgpa(courses):
    total_credits = 0
    total_grade_points = 0
    for course in courses:
        credits, grade = course
        total_credits += credits
        total_grade_points += (credits * grade)
    cgpa = total_grade_points / total_credits
    return cgpa

def calculate_percentage(cgpa):
    percentage = (cgpa - 0.75) * 10
    return percentage

# Define a function to handle unknown commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Create an Updater object
updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)

# Get the Dispatcher object from the Updater object
dispatcher = updater.dispatcher

# Add handlers for the /start, CGPA and Percentage buttons, and unknown commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, marks))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Start the bot
updater.start_polling()
