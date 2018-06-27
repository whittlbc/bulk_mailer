import json
import smtplib
from src.definitions import *
from src.email import Email
from src.utils.csv_parser import csv_as_dict_list
from src.utils.slug import to_slug
from time import sleep


class Mailer(object):

  def __init__(self, sender_name=None, sender_email=None, password=None, json_logfile_path=None):
    self.sender_name = sender_name
    self.sender_email = sender_email
    self.password = password
    self.json_logfile_path = json_logfile_path
    self.server = self._configure_server()
    self.failed_emails = {}

  def send_emails(self, template=None, recipient_csv=None, email_column_name=None,
                  interval=1, prompt_between_batches=False, batch_size=100):

    # Parse recipient CSV data from provided csv.
    recipient_data = self._parse_recipient_data(recipient_csv)

    # Split recipient data into batches.
    recipient_batches = [recipient_data[i:i + batch_size] for i in range(0, len(recipient_data), batch_size)]

    # Reset failed emails map.
    self.failed_emails = {}

    # Send emails in each batch.
    for i, batch in enumerate(recipient_batches):
      batch_num = i + 1

      self._process_batch(batch_num=batch_num, recipients=batch, template=template,
                          email_column_name=email_column_name, interval=interval)

      if not prompt_between_batches or batch_num == len(recipient_batches):
        continue

      # Determine if user wishes to proceed to next batch.
      proceed = None
      supported_answers = {'y': True, 'n': False}

      try:
        while proceed is None:
          answer = input('Continue with next batch? (y/n): ').strip().lower()
          proceed = supported_answers.get(answer)
      except KeyboardInterrupt:
        return

      # Exit early if user desires.
      if not proceed:
        return

    # Close SMTP server connection.
    self.server.close()

    if self.json_logfile_path:
      # Write failed emails to disk at the json logfile path.
      with open(self.json_logfile_path, 'w+') as f:
        f.write(json.dumps(self.failed_emails, indent=2, sort_keys=True))

    print('Done!')

  def _configure_server(self):
    # Create server instance.
    print('Connecting to {} on port {}...'.format(SMTP_HOST, SMTP_PORT))
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

    # Configure server and go into TLS mode.
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Login to sender's account on SMTP server.
    print('Logging into account {}...'.format(self.sender_email))
    server.login(self.sender_email, self.password)

    return server

  def _parse_recipient_data(self, csv_filename):
    # Construct csv path from filename.
    csv_filepath = os.path.join(DATA_DIR, csv_filename)

    print('Parsing CSV {}...'.format(csv_filepath))

    # Read in CSV data.
    recipient_data = csv_as_dict_list(path=csv_filepath,
                                      slugify_headers=True,
                                      sep=',',
                                      header=0)

    return recipient_data

  def _process_batch(self, batch_num=None, recipients=None, template=None, email_column_name=None, interval=1):
    print('\nProcessing Batch {}...\n'.format(batch_num))

    # For each recipient, create an email tailored to them, and send the email.
    for recipient in recipients:
      # Create Email class instance with template and recipient data.
      email = Email(sender_name=self.sender_name,
                    sender_email=self.sender_email,
                    email_column_name=to_slug(email_column_name),
                    template=template,
                    **recipient)

      # Send the email.
      self._send_email(email)

      # Sleep for the specified interval.
      sleep(interval)

  def _send_email(self, email):
    err = None
    err_code = None
    success = True
    to = email.recipient_email

    print('Sending email to {}...'.format(to))

    try:
      # Attempt to send the email.
      failed_emails_map = self.server.sendmail(self.sender_email, to, email.stringify())

      # Check to see if it failed.
      if to in failed_emails_map:
        err_code, err = failed_emails_map[to]
        success = False
    except smtplib.SMTPException as e:
      err = e or 'Unknown error'
      success = False

    # Log the outcome of the email (success or failure).
    outcome_msg = self._create_email_outcome_msg(to, success, err_code, err)
    print(outcome_msg + '\n')

    # Add entry to the failures map if the email failed.
    if not success:
      self.failed_emails[to] = outcome_msg

  def _create_email_outcome_msg(self, addr, success, err_code, err):
    if success:
      outcome_msg = 'Email successfully sent to {}.'.format(addr)
    elif err_code:
      outcome_msg = 'FAILED to send email to {}, with code {}, and error "{}".'.format(addr, err_code, err)
    else:
      outcome_msg = 'FAILED to send email to {}, with error "{}".'.format(addr, err)

    return outcome_msg