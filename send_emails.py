from src.mailer import Mailer
from src.definitions import *


if __name__ == '__main__':
  # Configure our mailer.
  mailer = Mailer(sender_name=SENDER_NAME,
                  sender_email=SENDER_EMAIL,
                  password=EMAIL_ACCOUNT_PW)

  # Send email using template to recipients inside csv.
  mailer.send_emails(template=EMAIL_TEMPLATE,
                     recipient_csv=CSV,
                     email_column_name=EMAIL_COLUMN_NAME)
