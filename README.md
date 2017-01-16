Kima Reporting
==================

Kima Reporting is an opensource reporting tool for VCs.

Features
----------
to be written

Setup with Heroku
-------------------
1. Create your project on Heroku

2. Type the following commands

     heroku login
     heroku git:remote -a name-of-your-project
     git push heroku master

3. Setup sendgrid

First, create a Sendgrid account. Setup an inbound hook that will go to the url :

     https://name-of-your-project.herokuapp.com/!callback/mail/a-secret-password-you-choose/

4. Configure the project

In the Settings tab, reveal the config variables. Then add the following configuration variables :

    ADMIN_EMAIL -> Your e-mail address
    ADMIN_NAME -> Your name
    CALLBACK_EMAIL_PASSWORD -> The password you've entered for Sendgrid's inbound hook
    SENDGRID_USERNAME -> Your sendgrid username
    SENDGRID_PASSWORD -> Your sendgrid password
    APP_DEPLOYED -> 1

5. Migrate the database and create the initial user

Type the following commands :

    heroku run ./manage.py migrate
    heroku run ./manage.py createsuperuser

You can now launch the service :

    heroku ps:scale web=1