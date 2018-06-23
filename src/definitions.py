import os

# Base dir of project.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Put CSVs inside here.
DATA_DIR = BASE_DIR + '/data'

# Put HTML email templates inside here.
TEMPLATE_DIR = BASE_DIR + '/templates'

# Configure SMTP server
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587

# Configure Sender.
SENDER_NAME = '<Your Name>'
SENDER_EMAIL = '<Your Email>'
EMAIL_ACCOUNT_PW = '<Your Email Account Password>'

# Configure CSV info.
RECIPIENT_CSV_FILENAME = 'example.csv'  # CSV filename inside of data/ that holds recipient info
EMAIL_COLUMN_NAME = 'Email Address'  # Name of the column inside the CSV that holds all recipient *emails*

# Specify email template to use.
EMAIL_TEMPLATE = 'example.html'  # HTML filename inside of templates/ that holds the email body contents

# Specify email subject.
EMAIL_SUBJECT = '<Your Email Subject>'
