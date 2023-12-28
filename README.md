Webhooks for covid conversational bot


### Configuring Postgres

    CREATE USER covidbot with ENCRYPTED PASSWORD 'covidBotPass';

    CREATE DATABASE coviddb WITH OWNER covidbot;


### Import Data

    python manage.py db_dump

