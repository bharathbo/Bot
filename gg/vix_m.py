from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus Navigation", callback_data='campus_nav')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.message.reply_text('Hi! Welcome to the college bot. How can I help you?', reply_markup=reply_markup)


def bus_timings_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Morning", callback_data='morning'),
         InlineKeyboardButton("Afternoon", callback_data='afternoon'),
         InlineKeyboardButton("Evening", callback_data='evening')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        text="Please select a bus timing:", reply_markup=reply_markup)


def campus_nav_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("College Location", callback_data='college_location'),
         InlineKeyboardButton("Administrative Block", callback_data='administrative_office')],
        [InlineKeyboardButton("MCA Department", callback_data='mca_department'),
         InlineKeyboardButton("Library", callback_data='library')],
        [InlineKeyboardButton("VTU Bus Stop", callback_data='vtu_bus_stop'),
         InlineKeyboardButton("VTU Canteen", callback_data='vtu_canteen')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        text="Please select a location:", reply_markup=reply_markup)


def campus_nav_menu_handler(update: Update, context: CallbackContext) -> None:
    campus_nav_menu(update, context)
    query = update.callback_query
    data = query.data
    if data == 'college_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the College location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.32502071887786, longitude=76.69908306303493)
    elif data == 'administrative_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the Administrative block location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.32485471021284, longitude=76.69942354884806)
    elif data == 'mca_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the MCA department location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.325321385497382, longitude= 76.69967578350156)
    elif data == 'library_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the Library location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.3256185, longitude=76.6998923)
    elif data == 'bus_stop_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the Bus stop location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.325811298476443, longitude=76.69907662656824)
    elif data == 'canteen_location':
        context.bot.send_message(chat_id=query.message.chat_id, text="Here is the Canteen location")
        context.bot.send_location(chat_id=query.message.chat_id, latitude=12.325118, longitude=76.700115)


def bus_timings_menu_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    if data == 'from_college_to_city':
        query.answer()
        query.edit_message_text(
            text="Here are the bus timings from College to City:")
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=open('from_college_to_city.jpg', 'rb'))
    elif data == 'from_city_to_college':
        query.answer()
        query.edit_message_text(
            text="Here are the bus timings from City to College:")
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=open('from_city_to_college.jpg', 'rb'))
    else:
        query.answer()
        query.edit_message_text(
            text="Invalid option selected. Please select a valid option from the menu.")


def menu_button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    if data == 'bus_timings':
        bus_timings_menu(update, context)
    elif data == 'campus_nav':
        campus_nav_menu(update, context)
    elif data == 'college_location':
        query.answer()
        query.edit_message_text(text="Here is the College location:")
        query.bot.send_location(chat_id=query.message.chat_id,
                                latitude=12.32502071887786, longitude=76.69908306303493)
    elif data == 'administrative_office':
        query.answer()
        query.edit_message_text(
            text="Here is the Administrative Office location:")
        query.bot.send_location(chat_id=query.message.chat_id,
                                latitude=12.316922296675514, longitude=76.66610473298852)
    else:
        query.answer()
        query.edit_message_text(
            text="Invalid option selected. Please select a valid option from the menu.")
        
def main() -> None:
    # Create an instance of Updater class
    updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register start function as the command handler for '/start'
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Register menu_button_handler function as the callback query handler
    dispatcher.add_handler(CallbackQueryHandler(menu_button_handler))

    # Register bus_timings_menu_handler function as the callback query handler
    dispatcher.add_handler(CallbackQueryHandler(bus_timings_menu_handler, pattern='bus_timings'))

    # Register campus_nav_menu_handler function as the callback query handler
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu_handler, pattern='campus_nav'))

    # Start the bot
    updater.start_polling()

    # # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()
if __name__ == '__main__':
    main()