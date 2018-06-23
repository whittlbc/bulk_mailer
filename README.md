Bulk Mailer

Send emails from your own Gmail account using Python.

# Requirements

Python 3+ (might work on Python 2 but who the fuck knows)

# Installation

1. Clone this repo to get started:

```
$ git clone https://github.com/whittlbc/bulk_mailer
```

2. Install project dependencies:

```
$ make install
```

# Usage

Follow the steps below to get up and running sending emails.

1. Navigate to https://myaccount.google.com/lesssecureapps and make sure that **Allow less secure apps** is toggled to **ON**.
Emails will fail to send from your Gmail account unless this is turned on.

2. Create (or place) a CSV inside the `data/` directory that holds all of your email recipients' information. 
Check out [the example csv](data/example.csv) for reference.

3. Create an HTML file inside of the `templates/` directory with the contents of the email you want to send.
Check out [the example template](templates/example.html) for reference.

4. Go to [`src/definitions.py`](src/definitions.py) and modify the config information that will be used when 
creating and sending emails. Variables you will probably want to change:

    * `SENDER_NAME`
    * `SENDER_EMAIL`
    * `EMAIL_ACCOUNT_PW`
    * `RECIPIENT_CSV_FILENAME`
    * `EMAIL_COLUMN_NAME`
    * `EMAIL_TEMPLATE`
    * `EMAIL_SUBJECT`
  
    Descriptions for each of these variables can be found as comments inside [`src/definitions.py`](src/definitions.py). 

5. Send your emails:

```
$ python send_emails.py
```

# License

MIT