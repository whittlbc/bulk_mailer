from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from src.definitions import *


class Email(object):

  def __init__(self, sender_name=None, sender_email=None,
               email_column_name=None, template=None, **kwargs):
    # Sender info
    self.sender_name = sender_name
    self.sender_email = sender_email

    # Recipient info
    self.recipient_email = kwargs[email_column_name]

    # Create jinja2 environment for template rendering.
    self.j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                              trim_blocks=True)  # control whitespace

    # Create email body from template and kwargs data
    self.body = self.j2_env.get_template(template).render(**kwargs)

    # Create email-able message.
    self.msg = self._create_msg()

  def stringify(self):
    return self.msg.as_string()

  def _create_msg(self):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')

    # Specify sender and recipient
    msg['From'] = '{} <{}>'.format(self.sender_name, self.sender_email)
    msg['To'] = self.recipient_email

    # Specify email subject and body
    msg['Subject'] = EMAIL_SUBJECT
    msg.attach(MIMEText(self.body, 'html'))

    return msg
