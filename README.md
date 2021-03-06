# Bulk Mailer

Send automated emails from your own email account using Python. Currently tested and works with Gmail and Outlook.

# Requirements

Python 3+ (might work on Python 2 but who the fuck knows)

# Installation & Setup

1. Clone this repo to get started:

    ```
    $ git clone https://github.com/whittlbc/bulk_mailer.git && cd bulk_mailer
    ```

2. If you don't have `virtualenv` (run `$ which virtualenv` to check if you do), install it with pip:

    ```
    $ pip install virtualenv
    ```

3. Create and activate your virtual environment:

    ```
    $ virtualenv -p python3 venv && source venv/bin/activate
    ```

4. Install project dependencies:

    ```
    $ make install
    ```

# Usage

Follow the steps below to get up and running sending emails.

1. (If using Gmail) Navigate to https://myaccount.google.com/lesssecureapps and make sure that **Allow less secure apps** is toggled to **ON**.
Emails will fail to send from your Gmail account unless this is turned on.

2. Create (or place) a CSV inside the `data/` directory that holds all of your email recipients' information. 
Check out [this example csv](data/example.csv) for reference.

3. Create an HTML file inside of the `templates/` directory with the contents of the email you want to send.
Check out [this example template](templates/example.html) for reference.

    **To use variables from your CSV file inside of your email template**, just use the snake-case version of the column name inside of double brackets.
    For example, in order to dynamically reference an email recipient's first name, you would first check what the column name for first name is in your CSV. For the [example CSV](data/example.csv), this happens to be <br/>`First Name`.
    Therefore, for this example, you would reference that variable as `{{ first_name }}`. The same applies to all other columns.
    
    These templates actually just use [jinja2](http://jinja.pocoo.org/docs/2.10/) for parsing, so anything you could do in `jinja2`, you can do in your templates here.

4. Go to [`src/definitions.py`](src/definitions.py) and modify the config information that will be used when 
creating and sending emails. Variables you will probably want to change:

    * `SMTP_HOST`
    * `SENDER_NAME`
    * `SENDER_EMAIL`
    * `EMAIL_ACCOUNT_PW`
    * `CSV`
    * `EMAIL_COLUMN_NAME`
    * `EMAIL_TEMPLATE`
    * `EMAIL_SUBJECT`
    * `EMAIL_SENDING_INTERVAL`
    * `JSON_LOGFILE_PATH`
    * `PROMPT_BETWEEN_BATCHES`
    * `BATCH_SIZE`
  
    Descriptions for each of these variables can be found as comments inside of [`src/definitions.py`](src/definitions.py). 

5. Send your emails:

    ```
    $ python send_emails.py
    ```

6. [Celebrate](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

# License

MIT
