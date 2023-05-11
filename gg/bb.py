from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

def student_main_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus navigator", callback_data='campus_nav_menu')],
        [InlineKeyboardButton("Campus drive updates", callback_data='campus_drive_updates')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.message.reply_text(text="Please select an option from the menu:", reply_markup=reply_markup)

def back_to_main_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus navigator", callback_data='campus_nav_menu')],
        [InlineKeyboardButton("Campus drive updates", callback_data='campus_drive_updates')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                  text="Please select an option from the menu:", reply_markup=reply_markup)
    # Display the main menu
    student_main_menu(None, None) # Pass None for update and context

def back_to_main_menu_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # Display the main menu
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus navigator", callback_data='campus_nav_menu')],
        [InlineKeyboardButton("Campus drive updates", callback_data='campus_drive_updates')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat_id, text="Please select an option from the menu:", reply_markup=reply_markup)

def campus_nav_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("College Location", callback_data='college_location'),
         InlineKeyboardButton("Administrative Block", callback_data='administrative_office')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='back_to_main_menu')],
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please select a location:", reply_markup=reply_markup)

def campus_nav_menu_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    if data == 'college_location':
        query.answer()
        query.edit_message_text(text="Here is the College location:")
        query.bot.send_location(chat_id=query.message.chat_id,
                                latitude=12.32502071887786, longitude=76.69908306303493)    
    elif data == 'administrative_office':
        query.answer()
        query.edit_message_text(text="Here is the Administrative block location:")
        query.bot.send_location(chat_id=query.message.chat_id,
                                latitude=12.32485471021284, longitude=76.69942354884806)
    elif data == 'back_to_main_menu':
        student_main_menu(update, context)
        return
    else:
        # Display campus navigation menu
        campus_nav_menu(update, context)
        return
    return student_main_menu(update, context)
def main() -> None:
    # Create the Updater and pass in the bot's token.
    updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)
    # Get the dispatcher to register handlers.
    dispatcher = updater.dispatcher
    # Register the handlers.
    dispatcher.add_handler(CommandHandler('start', student_main_menu))
    dispatcher.add_handler(CallbackQueryHandler(student_main_menu, pattern='^main_menu$'))

def main() -> None:
    # Create the Updater and pass in the bot's token.
    updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)
    # Get the dispatcher to register handlers.
    dispatcher = updater.dispatcher
    # Register the handlers.
    dispatcher.add_handler(CommandHandler('start', student_main_menu))
    dispatcher.add_handler(CallbackQueryHandler(student_main_menu, pattern='^main_menu$'))
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu_handler, pattern='^campus_nav_menu$'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_main_menu_handler, pattern='^back_to_main_menu$'))
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu_handler, pattern='^college_location$'))
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu_handler, pattern='^administrative_office$'))
    # Start the Bot.
    updater.start_polling()
    # Run the Bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()
if __name__ == '__main__':
    main()

