from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

def student_main_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
         InlineKeyboardButton("Campus navigator", callback_data='campus_nav')],
        [InlineKeyboardButton("Study Resources", callback_data='study_resources'),
         InlineKeyboardButton("Attendance Report", callback_data='attendance_report')],
        [InlineKeyboardButton("CGPA Calculator", callback_data='cgpa_calculator'),
         InlineKeyboardButton("Roadmaps", callback_data='roadmaps')],
        [InlineKeyboardButton("Notifications", callback_data='notifications'),
         InlineKeyboardButton("Campus drive updates", callback_data='campus_drive_updates')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    update.message.reply_text(text="Please select an option from the menu:", reply_markup=reply_markup)

back_to_main_menu_button = InlineKeyboardButton(
    "Back to Main Menu", callback_data="student_main_menu"
)

# Create the keyboard with the button
keyboard = [[back_to_main_menu_button]]
reply_markup = InlineKeyboardMarkup(keyboard)

def bus_timings_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("From College to City", callback_data='from_college_to_city'),
         InlineKeyboardButton("From City to College", callback_data='from_city_to_college')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='student_main_menu')]
    ]
    # Create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please select a bus timing:", reply_markup=reply_markup)


def campus_nav_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("College Location", callback_data='college_location'),
         InlineKeyboardButton("Administrative Block", callback_data='administrative_office')],
        [InlineKeyboardButton("MCA Department", callback_data='mca_department'),
         InlineKeyboardButton("Library", callback_data='library_location')],
        [InlineKeyboardButton("VTU Bus Stop", callback_data='vtu_bus_stop'),
         InlineKeyboardButton("VTU Canteen", callback_data='canteen_location')],
        [InlineKeyboardButton("Back to Main Menu", callback_data='student_main_menu')]
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
    elif data == 'mca_department':
        query.answer()
        query.edit_message_text(text="Here is the MCA department location:")
        query.bot.send
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
    query.answer()
    query.edit_message_text(
        text="Please select a bus stop:",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Bus Stop A", callback_data="bus_stop_a"),
                    InlineKeyboardButton("Bus Stop B", callback_data="bus_stop_b"),
                ],
                [
                    InlineKeyboardButton("Bus Stop C", callback_data="bus_stop_c"),
                    InlineKeyboardButton("Bus Stop D", callback_data="bus_stop_d"),
                ],
                [
                    InlineKeyboardButton("Back to Main Menu", callback_data='student_main_menu')]
                ],
        ),
    )
def main() -> None:
    # Create the Updater and pass in your bot's token
    updater = Updater(token='6267642713:AAH9C0BKY7C56-jrBw6fPVssrl_ElDhM5kU', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', student_main_menu))

    # Add callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(bus_timings_menu_handler, pattern='^bus_timings$'))
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu_handler, pattern='^campus_nav$'))
    dispatcher.add_handler(CallbackQueryHandler(bus_timings_menu, pattern='^bus_stop_'))
    dispatcher.add_handler(CallbackQueryHandler(campus_nav_menu, pattern='^college_location'))

    
    dispatcher.add_handler(CallbackQueryHandler(student_main_menu, pattern='^student_main_menu$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(student_main_menu, pattern='student_main_menu'))


    # Start the bot
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
    # updater.start_polling()
    # updater.idle()
