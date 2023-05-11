from telegram import Update
from telegram.ext import CallbackQueryHandler,CallbackContext
from telegram.ext import CommandHandler, MessageHandler, Filters
from db import database, update
from student_menu import studentMainMenu, studentMenuButtonHandler, get_bus_timings
from lecture_menu import lecturerMainMenu
#from vix_m import campus_nav_menu, campus_nav_menu_handler, get_bus_timings


# Define the command handlers
def start(update, context):
    context.user_data['authenticated'] = False
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm your VTU student and lecturer chatbot! How can I help you today?")
    help_text = "Available commands:\n/start - Start the bot\n/vtu - College Information\n/login - Login to bot\n"
    update.message.reply_text(help_text)
    
def vtu(update, context):
     context.user_data['authenticated'] = False
     context.bot.send_message(chat_id=update.message.chat_id, text="Visvesvaraya Technological University (VTU) was established by the Government of Karnataka on 1 April 1998 with its headquarters at Belagavi, as per the provisions of the Visvesvaraya Technological University Act, 1994, an Act to establish and incorporate a university in the State of Karnataka for the development of engineering, technology and allied sciences. For effective administration, four regional offices at the four revenue divisional headquarters, namely, Belagavi, Bangalore, Mysore and Gulbarga were established. VTU was established by the Government in order to promote planned and sustainable development of technical education consistent with state and national policies and bringing various colleges affiliated earlier to different universities, with different syllabi, different procedures and different traditions under one umbrella.\n\nNote : This bot is only used for Mysore branch.\n\nAddress:\nCA Site no: 1, Hanchya – Satagalli Ring Road, Mysuru , Karnataka – 570019.\nContact Details of the Institution\nOffice: DEPARTMENT OF PG STUDIES,VTU MYSURU\nPhone No: 0821 – 2570010\nFax No: 0821 – 2570010\nWebsite Address: https://vtu.ac.in/en/pg-center-mysuru/\nE-Mail Address: pgmysore@vtu.ac.in\n\nName of PG Coordinator:\nDr. Suresh . R\nPhone No:\n0821-2570010\nE-Mail Address:\npgmysore@vtu.ac.in\n\nPG: MBA,MCA & M.Tech.")

def login(update, context):
    context.user_data['authenticated'] = False
    text = "Please enter your username and password separated by a space."
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def authenticate(update:Update, context:CallbackContext):

    if context.user_data['authenticated'] is True:
        return True

    message_text = update.message.text  
    if ' ' in message_text:
        username, password = message_text.split()
        user_role = ''
        mydb, mycursor = database()
        context.user_data['mycursor'] = mycursor
        context.user_data['mydb'] = mydb
        print(mydb)
        mycursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
        myresult = mycursor.fetchone()
        print(myresult)
        if myresult:
            user_role = myresult[0]
        if user_role == 'studentslogin':
            context.user_data['role'] = 'studentslogin'
            print("Logged in as student")
            context.bot.send_message(chat_id=update.message.chat_id, text="You are logged in as a student.")
            context.user_data['authenticated'] = True  
            studentMainMenu(update, context)
            return True              
        elif user_role == 'lecturerslogin':
            context.user_data['role'] = 'lecturerslogin'
            context.bot.send_message(chat_id=update.message.chat_id, text="You are logged in as a lecturer.")
            print("Logged in as lecturer")
            context.user_data['authenticated'] = True  
            lecturerMainMenu(update, context)
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Invalid username or password.")
    else:
        update.message.reply_text("Please enter your username and password separated by a space.")

    return False

def main():
        updater = update()
        # Create the updater and dispatcher
        dispatcher = updater.dispatcher

        updater.dispatcher.user_data['authenticated'] = False

        # Add the command handlers
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('vtu', vtu))
        dispatcher.add_handler(CommandHandler('login', login))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, authenticate))
        dispatcher.add_handler(CallbackQueryHandler(studentMenuButtonHandler, pass_user_data=True))

        # Add the message handler for getting bus timings
        
        def get_bus_timings_callback(update, context):
            if context.user_data.get('waiting_for_time'):
                # Call the get_bus_timings function
                get_bus_timings(update, context)
                # Clear the waiting_for_time flag
                context.user_data['waiting_for_time'] = False
            else:
                # If we're not waiting for a time input, do nothing
                pass

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_bus_timings_callback))

        # Start the bot
        updater.start_polling()

        # Stop the bot when you press Ctrl-C
        updater.idle()
    
if __name__ == '__main__':
    main()