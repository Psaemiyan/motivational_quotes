import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
from config import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD
import logging
import traceback

def send_email(subject, content, sender_email, receiver_email, password):
    msg = MIMEText(content, _charset="utf-8")
    msg['Subject'] = subject
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=msg.as_string()
            )
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email. Error: {str(e)}")
        traceback.print_exc()

def main():
    logging.basicConfig(filename='email_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        now = dt.datetime.now()
        day_today = now.weekday()

        if day_today == 1:
            with open("quotes.txt") as quote_file:
                all_quotes = quote_file.readlines()
                quote = random.choice(all_quotes)

            subject = "A Little Pick Me Up to Brighten Your Day"
            email_content = quote

            send_email(subject, email_content, SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD)
        else:
            logging.info("Not sending email today. It's not Monday.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()


