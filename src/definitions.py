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
SENDER_NAME = 'Ben Whittle'
SENDER_EMAIL = 'benwhittle31@gmail.com'
EMAIL_ACCOUNT_PW = 'Maxine20/'  # Ex: Your Gmail account password

# Configure CSV info.
RECIPIENT_CSV_FILENAME = 'example.csv'
EMAIL_COLUMN_NAME = 'Email Address'

# Specify email template to use.
EMAIL_TEMPLATE = 'example.html'

# Specify email subject.
EMAIL_SUBJECT = 'Example Email Subject'
