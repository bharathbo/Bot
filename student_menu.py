from telegram import Update
from telegram.ext import CallbackContext,CallbackQueryHandler
from telegram.ext import CommandHandler, MessageHandler, Filters
from db import database, update

def studentMainMenu(update, context):
    # Create the keyboard with the desired buttons
    # define the keyboard
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = [[InlineKeyboardButton("Bus Timings", callback_data='bus_timings'),
             InlineKeyboardButton("Campus navigator", callback_data='campusNav')],
            [InlineKeyboardButton("Study Resources", callback_data='study_resources'),
            InlineKeyboardButton("Attendance Report", callback_data='attendance_report')],
            [InlineKeyboardButton("CGPA Calculator", callback_data='cgpa_calculator'),
            InlineKeyboardButton("Roadmaps", callback_data='roadmaps')],
            [InlineKeyboardButton("Notifications", callback_data='notifications'),
            InlineKeyboardButton("Campus drive updates", callback_data='campus_drive_updates')]]
            
    # create the keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message to the user with the custom keyboard
    context.bot.send_message(chat_id=update.message.chat_id, text="Please select an option from the menu:", reply_markup=reply_markup)

GET_TIME, SHOW_TIMINGS = range(2)
def start_bus_timings(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the time in HH:MM format:")
    return GET_TIME


def studentMenuButtonHandler(update, context):
    query = update.callback_query
    data = query.data
    print("Button clicked: ", query.data)
    if query.data == 'bus_timings':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the time in HH:MM format:")
        # context.user_data['waiting_for_time'] = True
        context.user_data['message_handler'] = MessageHandler(Filters.text & ~Filters.command, get_bus_timings)
        context.dispatcher.add_handler(context.user_data['message_handler'])
        # Start the bus timings conversation

    elif query.data == 'campusNav':
        campusNav(update, context)
    elif query.data in ['college_location', 'administrative_location', 'mca_location', 'library_location', 'bus_stop_location', 'canteen_location']:
        campusNav_button_click(update, context)

#New functions starts from here


def campusNav(update, context):
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = [
        [InlineKeyboardButton("College Location", callback_data='college_location'),
         InlineKeyboardButton("Administrative Block", callback_data='administrative_location')],
        [InlineKeyboardButton("MCA Department", callback_data='mca_location'),
         InlineKeyboardButton("Library", callback_data='library_location')],
        [InlineKeyboardButton("VTU bus stop", callback_data='bus_stop_location'),
         InlineKeyboardButton("VTU Canteen", callback_data='canteen_location')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please select a location:", reply_markup=markup)

def campusNav_button_click(update, context):
    print("Clicked on location buttons")
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

# Define a function to get the bus timings based on the user's input
def get_bus_timings(update: Update, context: CallbackContext):
    mydb, mycursor = database()
    context.user_data['mycursor'] = mycursor
    context.user_data['mydb'] = mydb
    print(mydb)

    # Get the user's input
    time = update.message.text.strip()
    print(f"User entered time: {time}")

    # Query the database to get the next bus number and arrival time
    sql = "SELECT bus_number, arrival_time FROM bus_timings WHERE %s BETWEEN departure_time AND arrival_time ORDER BY departure_time LIMIT 1"
    mycursor.execute(sql, (time,))
    result = mycursor.fetchone()

    # If a bus was found, send the details to the user
    if result:
        bus_number, arrival_time = result
        message = f"The next bus is bus number {bus_number}, arriving at {arrival_time}."
    # Otherwise, let the user know there are no more buses for the day
    else:
        message = "There are no more buses for the day."

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    context.dispatcher.remove_handler(context.user_data.pop('message_handler'))

# Create the updater and dispatcher
# updater = Updater(token='Your bot token', use_context=True)
updater = update()
dispatcher = updater.dispatcher

# Add the command handlers
dispatcher.add_handler(CallbackQueryHandler(studentMenuButtonHandler))
dispatcher.add_handler(CommandHandler('smenu', studentMainMenu))
dispatcher.add_handler(CallbackQueryHandler(campusNav_button_click))
# dispatcher.add_handler(CommandHandler('bus_timings', bus_timings))

# Start the bot
updater.start_polling()

# # Stop the bot when you press Ctrl-C
updater.idle()

