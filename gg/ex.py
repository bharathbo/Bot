import logging
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a function to send the main menu to the student
def student_main_menu(update: Update, context: CallbackContext) -> None:
    # Import InlineKeyboardButton and InlineKeyboardMarkup here
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    # Create the keyboard with the desired buttons
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus Navigator", callback_data='campus_nav')],
        [InlineKeyboardButton("Study Resources", callback_data='study_resources'),
         InlineKeyboardButton("Attendance Report", callback_data='attendance_report')],
        [InlineKeyboardButton("CGPA Calculator", callback_data='cgpa_calculator'),
         InlineKeyboardButton("Roadmaps", callback_data='roadmaps')],
        [InlineKeyboardButton("Notifications", callback_data='notifications'),
         InlineKeyboardButton("Campus Drive Updates", callback_data='campus_drive_updates')],
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.message.reply_text(
        text="Please select an option from the menu:", reply_markup=reply_markup)

# Define a function to send the campus navigation menu to the student
def campus_nav_menu_handler(update: Update, context: CallbackContext) -> None:
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
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

# Define a function to send the bus timings menu to the student
def bus_timings_menu_handler(update: Update, context: CallbackContext) -> None:
    # Import InlineKeyboardButton and InlineKeyboardMarkup here
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    update.callback_query.answer()
    keyboard = [
        [InlineKeyboardButton("From College to City", callback_data='from_college_to_city'),
         InlineKeyboardButton("From City to College", callback_data='from_city_to_college')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')],
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.edit_message_text(
        text="Please select an option:", reply_markup=reply_markup)


# Define a function to handle the button clicks in the menu


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


def bus_timings_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("From College to City",callback_data='from_college_to_city'),
            InlineKeyboardButton("From City to College", callback_data='from_city_to_college')
        ],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        text="Please select an option:", reply_markup=reply_markup)


def campus_nav_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Academic Block", callback_data='academic_block'),
         InlineKeyboardButton("Library", callback_data='library')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        text="Please select a location:", reply_markup=reply_markup)


def bus_timings_handler(update: Update, context: CallbackContext) -> None:
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


def campus_nav_handler(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                "Main Building", callback_data='main_building'),
            InlineKeyboardButton("Library", callback_data='library'),
        ],
        [
            InlineKeyboardButton("Canteen", callback_data='canteen'),
            InlineKeyboardButton(
                "Sports Complex", callback_data='sports_complex'),
        ],
        [
            InlineKeyboardButton("Back to Menu", callback_data='back_to_menu'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Please choose a location:", reply_markup=reply_markup)


def location_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    if data == 'main_building':
        query.answer()
        query.bot.send_location(
            chat_id=query.message.chat_id, latitude=12.323564, longitude=76.676684)
        query.bot.send_message(chat_id=query.message.chat_id,
                               text="The Main Building is located here.")
    elif data == 'library':
        query.answer()
        query.bot.send_location(
            chat_id=query.message.chat_id, latitude=12.326196, longitude=76.679170)
        query.bot.send_message(chat_id=query.message.chat_id,
                               text="The Library is located here.")
    elif data == 'canteen':
        query.answer()
        query.bot.send_location(
            chat_id=query.message.chat_id, latitude=12.325215, longitude=76.679711)
        query.bot.send_message(chat_id=query.message.chat_id,
                               text="The Canteen is located here.")
    elif data == 'sports_complex':
        query.answer()
        query.bot.send_location(
            chat_id=query.message.chat_id, latitude=12.324778, longitude=76.680638)
        query.bot.send_message(chat_id=query.message.chat_id,
                               text="The Sports Complex is located here.")
    elif data == 'back_to_menu':
        query.answer()
        student_main_menu(update, context)


def main() -> None:
    # Create the Updater and pass in the bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater("6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers to the dispatcher
    dispatcher.add_handler(CommandHandler("start", student_main_menu))
    dispatcher.add_handler(CallbackQueryHandler(menu_button_handler))

    # # Start the Bot
    updater.start_polling()

    # # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()
if __name__ == '__main__':
    main()
