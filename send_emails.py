from src.definitions import *
from src.mailer import Mailer


if __name__ == '__main__':
  # Configure our mailer.
  mailer = Mailer(sender_name=SENDER_NAME,
                  sender_email=SENDER_EMAIL,
                  password=EMAIL_ACCOUNT_PW,
                  json_logfile_path=JSON_LOGFILE_PATH)

  # Send email using template to recipients inside csv.
  mailer.send_emails(template=EMAIL_TEMPLATE,
                     recipient_csv=CSV,
                     email_column_name=EMAIL_COLUMN_NAME,
                     interval=EMAIL_SENDING_INTERVAL,
                     prompt_between_batches=PROMPT_BETWEEN_BATCHES,
                     batch_size=BATCH_SIZE)
