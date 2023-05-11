from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackContext,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from db import database, update




def lecturerMainMenu(update, context):
    # Create the keyboard with the desired buttons
    # define the keyboard
    keyboard = [[InlineKeyboardButton("Assignments", callback_data='assignments_submitted'),
             InlineKeyboardButton("Feedbacks", callback_data='feed_backs')],
            [InlineKeyboardButton("Announcements", callback_data='announcement'),
            InlineKeyboardButton("Time table", callback_data='time_table')],
            [InlineKeyboardButton("Attandance tracking", callback_data='attandance_tracking'),
            InlineKeyboardButton("Study Notes", callback_data='study_notes')]]
    # create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    context.bot.send_message(chat_id=update.message.chat_id, text="Please select an option from the menu:", reply_markup=reply_markup)

def studentMenuButtonHandler(update, context):
    query = update.callback_query
    data = query.data



# Create the updater and dispatcher
# updater = Updater(token='Your bot token', use_context=True)
updater = update()
dispatcher = updater.dispatcher

# Add the command handlers
# dispatcher.add_handler(CallbackQueryHandler(lecturerMenuButtonHandler))
dispatcher.add_handler(CommandHandler('lmenu', lecturerMainMenu))
# dispatcher.add_handler(CallbackQueryHandler())
# dispatcher.add_handler(CommandHandler('bus_timings', bus_timings))

# # Start the bot
updater.start_polling()

# # Stop the bot when you press Ctrl-C
updater.idle()
