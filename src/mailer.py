import smtplib
from src.definitions import *
from src.email import Email
from src.utils.csv_parser import csv_as_dict_list
from src.utils.slug import to_slug
from time import sleep


class Mailer(object):

  def __init__(self, sender_name=None, sender_email=None, password=None):
    self.sender_name = sender_name
    self.sender_email = sender_email
    self.password = password
    self.server = self._configure_server()

  def send_emails(self, template=None, recipient_csv=None,
                  email_column_name=None, interval=0.5):
    # Parse recipient CSV data from provided csv.
    recipient_data = self._parse_recipient_data(recipient_csv)

    # For each recipient, create an email tailored to them, and send the email.
    for data in recipient_data:
      # Create Email class instance with template and recipient data.
      email = Email(sender_name=self.sender_name,
                    sender_email=self.sender_email,
                    email_column_name=to_slug(email_column_name),
                    template=template
                    **data)

      # Send the email.
      self._send_email(email)

      # Sleep for the specified interval.
      sleep(interval)

    # Close SMTP server connection.
    self.server.close()

  def _configure_server(self):
    # Create server instance
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

    # Configure server and go into TLS mode.
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Login to sender's account on SMTP server.
    server.login(self.sender_email, self.password)

    return server

  def _parse_recipient_data(self, csv_filename):
    # Construct csv path from filename.
    csv_filepath = os.path.join(DATA_DIR, csv_filename)

    # Read in CSV data.
    recipient_data = csv_as_dict_list(path=csv_filepath,
                                      slugify_headers=True,
                                      sep=',',
                                      header=0)

    return recipient_data

  def _send_email(self, email):
    print('Sending email to {}...'.format(email.recipient_email))
    self.server.sendmail(self.sender_email, email.recipient_email, email.stringify())
