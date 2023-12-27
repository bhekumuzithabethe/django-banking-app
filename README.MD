# Thabethe Banking

## Overview
Thabethe banking is a banking project, whereby a consultant can create a clients,bank accounts, and client banking cards. 

Consultants can only be registerd or created by the bank manager, and the bank manager is able to do everything the bank consultant can do.

User's or clients can view their account transactions,account balance and account number. Clients can make withdrawalls using their card number and the account the client wants to withdraw money from. Transferes can only be made if a user has multiple bank accounts with us, if a client wishes to send money to a beneficiary they can make use of the pay tab to pay an account registered in our database. Clients are also able to make deposits given an account number they wish to deposit into.

The project is built using  Django 5, HTML 5, CSS 3, and Bootstrap 5 with a Bootswatch Cosmo theme.
![Home Page]()
## Prerequisites

1. [Python 3.8-3.12](https://www.python.org/)
This project uses Django v4.2.4. For Django to work, you must have a correct Python version installed on your machine. More information [Here](https://django.readthedocs.io/en/stable/faq/install.html)
1. [Visual Studio Code](https://code.visualstudio.com/)

## Installation

* Create a virtual environment.<br>
From the root directory, run:
>On macOS:
```
virtualenv venv
```
>On Windows:
```
python -m venv venv
```

* Activate the virtual environment.<br>
From the root directory, run: 
>On macOS:
```
source venv/bin/activate
```

>On Windows:
```
venv\scripts\activate
```

* Install required dependencies.<br>
From the root directory, run:
```
pip install requirements.txt
```

* Create an admin user to access the Django Admin interface.<br>
From the root directory, run:
```
python manage.py createsuperuser
```
When prompted, enter a username, email, and password.


## Run the application
From the root directory, run:
```
python manage.py runserver
```

## To view the application

Go to http://127.0.0.1:8000/. <br>
Once running use the following details to login as the bank manager
>username: admin<br>password:1234
You can create a client, then a bank account on the bank manager's portal. Once you are a client you can register your user account on the login page, but you firstly need to make sure you are atleast a client, even if you don't have an account bt atleast be our client because you will have to authenticate your identity number,first name, last name and your email address. If you are not a client you won't be able to the authenticated to create your user account. Once authenticated you'll be promted to enter you first and last name once again, your username,email and password to create your user account. <br>
As the bank manager you can create a bank consultant, this is optional as the bank manager can do all the functions done bt a consultant.

## Copyright and License
Copyright © 2023 - current year Thabethe Programming. Code released under the MIT license.