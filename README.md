# Silkscreenservice
**Milestone project 4: Full Stack Frameworks with Django - Code Institute**

[![Build Status](https://travis-ci.org/D1ang/Silkscreenservice.svg?branch=master)](https://travis-ci.org/D1ang/Silkscreenservice)

For a silkscreen-press company a need for an order system has been requested.
The main goal of the system is to make the job of our studio employees easier and more efficient.
For the customer we would like to provide an easy to understand and easy to use system so,
they will be able to make their service requests easier.

In short:
 - A system for employees to be more efficient.
 - An easy to understand system for B2B customers to remove some workload from the studio employees.

![Design](https://github.com/D1ang/Silkscreenservice/blob/master/mockups/presentation.png)

## Table of Contents
  * [UX](#ux)
  * [User stories](#user-stories)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
  * [Technologies](#technologies)
    + [JavaScript Libraries](#javascript-libraries)
    + [Python & Django Plugins](#python---django-plugins)
  * [Features](#features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Admin login gave a 500 error](#admin-login-gave-a-500-error)
  * [Deployment](#deployment)
    + [Deploy requirements](#deploy-requirements)
    + [Local deployment](#local-deployment)
    + [Heroku deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

## UX
To make the system as clear as possible to the end-user, a basic but very clean design has been chosen.
Options are minimalistic and the end-user will not be overloaded with options to choose from.
The navigation bar, buttons, cart system and dashboard have been built and have an easy to understand logic.

## User stories
With years of field experience, we have built a well-known form and work ethic in creating designs.
We asked our customers from day to day what they would like to see in a sample and came up with the following points:

 - As a user, I want to easily fill in the forms for a service request (services)
 - As a user, I want to upload my artwork fast and easy in the same system (checkout form)
 - As a user, I want a secured overview of my order history (dashboard)
 - As a user, I want the system to remember my cart, for if I want to make changes later (cart)
 - As a user, I do not want to fill in my details every time, but do want to change them if needed (profile)
 - As an employee, I want to know which service are required per order (order)
 - As an employee, I want to change the status of an order (admin list actions)
 - As an employee, I would like to download the artwork (order details)
 - As an employee, I would like to upload and overwrite the artwork (order details)
 - As an employee, I want to search and filter the orders (search & filter)

### Strategy
The goal of the system is to make it as easy as possible to access, short and informative, 
while striving for a minimalist and user-friendly design.

### Scope
For customers, we wanted to provide them with an easy to understand (first-view-use) system.
This way, they would be able to request services: faster, easier and on their own, 
so our studio employees have more free time for other job-related tasks and be able to do
their service tasks more efficient.

### Structure
The system is structured to get the right information as quickly as possible.
The order of the options provided are placed in a logic workflow while the design provided will use a messages bar
that should be easy to understand and gives the customer a straight away no-nonsense feedback.
The navbar is available when needed and a footer is provided with contact-information below the page.

### Skeleton
By using Figma and LucidChart the following wireframes were created:

[Silkscreenservice wireframe](https://github.com/D1ang/Silkscreenservice/blob/master/mockups/wireframe.pdf)

[Responsive phone wireframe](https://github.com/D1ang/Silkscreenservice/blob/master/mockups/wireframe-sm.pdf)

[ERD wireframe](https://github.com/D1ang/Silkscreenservice/blob/master/mockups/model_diagram.png)

### Surface
The colours chosen are yellow, red, black, and blue.
Blue is the most used colour most associated with harmony, faithfulness, confidence, and imagination.
A very clean, abstract and an almost childish design has been chosen to force the attention to the systems functionality.
Users will not be afraid to use the system by this easy to understand design.
The font Poppins had been chosen because of its look that fits perfectly to the buttons and graphics on the homepage.
As for the dashboard a lighter version of Poppins has been used as it looks very clean and is easy to read.
The buttons are styled in 2 versions; full black or black outlined, to fit the overall design.

## Technologies
 - Figma - *To create a wireframe*
 - Lucid Chart - *To create the Entity Relationship Diagram (ERD)*
 - HTML - *To create the basics*
 - CSS - *To improve placements and design*
 - JavaScript - *The engine to create user interaction*
 - Python - *Programming language*
 - Postgres - *Opensource database to save the transactions, profile, and orders*
 - Django - *Web framework in python*
 - Bootstrap - *To make the design responsive*
 - Font Awesome - *Easy icon access for the icons*
 - Font Awesome animations - *Additional animations for the Font Awesome icons*
 - GitHub Wiki TOC generator - *Generates a MarkDown TOC online*

### JavaScript Libraries
 - jQuery - *To improve input field feedback*
 - flatpickr - *lightweight, powerful JavaScript datetimepicker with no dependencies*
 - DataTables - *Adds advanced interaction controls to HTML tables*
 - Stripe - *For credit card transactions*

### Python & Django Libraries
 - pillow - *Python Imaging Library*
 - Stripe - *Credit card payments and transaction security*
 - boto3 - *To connect to AWS*
 - django-allauth - *Authentication, registration & account management*
 - django-countries - *Provides country choices for use with forms*
 - django-phonenumber-field - *A Django library which interfaces with python-phonenumbers to validate*
 - django-crispy-forms - *Controls the rendering behaviour of Django forms*
 - django-filter - *Easy searching and filtering query sets*

## Features
This system is an e-commerce-based website with a simplistic but easy to understand build-up.
Providing the user with 2 call-to-action buttons and a "read more" button, a choice can be made in seconds.
The navbar is sticky but reacts on the users scrolling behaviour. While scrolling down the bar disappears to keep a clean screen estate,
but when scrolling up, the bar will re-appear.
The frequently used services are created by the most clicked products for the cart in the backend.
The 3 services with the most clicks will be sorted on popularity and shown here.
The services page will show all the available services that can be ordered.
To order a service the user needs to be logged in. To provide the user with some extra feedback a handy message bar will drop down from the navbar.
This bar will scroll up again after a few seconds. 
When an user will create an account or login, a dashboard will be available for a nice table-based overview of the placed services.
An admin account is available for employees to, update service request and download the by customer uploaded artwork.
Users can add or delete services to their cart which will be saved in the backend right away.
As a user logs out the cart will be remembered in the system to be finished later. 
When the customer checkout, a secured payment can be made with credit card and artwork can be uploaded, to be downloaded by the employees.

### Features Left to Implement
In later releases I would like to add models for a comments/grade system, so customers can add comments or grade the provided services.
Visitors would be able to read those. I would also like to add a function for admin to remove a customer.
As of European law this should be possible.
This can be done through the standard django admin, but it would be nicer and easier if this function is available through the custom-made dashboard.

## Testing
This system was tested across multiple screen sizes on Chrome, Safari, and Internet Explorer.
To ensure compatibility and responsiveness it is also tested on an android based mobile device (OnePlus5)
and an older tablet device (Samsung Galaxy Tab2).
The system has been field-tested by customers and employees.
Some basic unit testing has been done with Travis and own written testcodes on the home and accounts app.
Unit testing does not go as deep as the field tests, but does show that the bare basic functions are working correctly. 

The following tests have been used to ensure proper site functionality:

- [GTmetrix](https://gtmetrix.com/): To test on website loading times.
- [W3C HTML Validator](https://validator.w3.org/): This validator checks the mark-up validity of Web documents in HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This validator checks the mark-up validity of Web documents in CSS.
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB): Inspecting on overflow errors.
- [Autoprefixer CSS online](https://autoprefixer.github.io/): Autoprefixer is a PostCSS plugin which parses your CSS and adds vendor prefixes.
- [JSHint](https://jshint.com/): A static code analysis tool for JavaScript.
- [ES6 Syntax Check](https://www.piliapp.com/syntax-check/es6/): An online ECMAScript 6 Checker.
- [Visual Studio Code](https://code.visualstudio.com/): Using the built-in tools to test on proper code, like flake8 linter.
- [Travis](https://travis-ci.org/): Used halfway the project to test the code.

## Bugs

### CSS
CSS written code is tested with the W3C CSS Validator.
As it does not give any problems, the deployed version of the site does gives a couple of warnings and errors coming
from Bootstrap and the Font Awesome animations Library.

### JavaScript
All 3 JavaScript’s in this system passed the test, only a couple of warnings came up through JSHint, for example: using "let", "const" but none of them are bug worthy.
By using "ES6 Syntax Check" all the Syntax checks passed.

### Admin login gave a 500 error
When a customer logged in, the system worked perfectly. But for the admin account a 500 error came up.
This bug was fixed after making migrations and changed the max field characters to 50 chars.
Seems that the admin entered email was 28 characters and when in an earlier build was set to 25, this error came up.

## Deployment
This code is deployed to GitHub directly from the master branch.
The deployed site will update automatically upon new commits to the master branch.
This code can be run locally or deployed to a live environment. Directions are based on deployment locally and to Heroku.

### Deploy requirements
 - [VScode](https://code.visualstudio.com/) *A tool to develop software*
 - [python 3](https://www.python.org/) *A programming language*
 - [PIP](https://pip.pypa.io/en/stable/installing/) *To get python installation packages*
 - [Git](https://github.com/) *Version control for code source*
 - [AWS-S3](https://docs.aws.amazon.com/) *Web based cloud storage service*
 - [S3 Bucket](https://docs.aws.amazon.com/) *A cloud storage resource*
 - [Stripe](https://stripe.com/) *To securely collect credit card payments*

### Local deployment
1.  Download a copy of the GitHub repository by clicking the "Code" button at the top right of the 
    GitHub page and in the submenu select "Download ZIP". Extract the zip file to a folder of choice on your system. If Git is installed on your system, you can clone the repository 
    with the following command:
    ```bash
    git clone https://github.com/D1ang/Silkscreenservice.git
    ```

1.  Open the unzipped folder in your preferred IDE (in this example we are using VScode)
    Open up a terminal session and set up a virtual environment with these commands in the terminal session:
    ```bash
    pip install virtualenv
    ```
    >If you already have virtualenv installed from a different project, then this step is not needed. The pip command may differ per system this can be pip or pip3.

    ```bash
    virtualenv env
    ```
    >Your command may differ to the IDE you are using, such as ```python -m .venv venv ...``` or ```py manage.py ...```
  
    Activate the .env with the command:
    ```bash 
    env\Scripts\activate
    ```
    >This command may differ depending on your operating system, please check the Python documentation on creating an ENV.

1.  Install all required django modules with the command:
    ```bash
    pip install -r requirements.txt
    ```

1.  Create a new file at the base directory level called env.py and copy the following into the created env.py file:
    ```bash
    import os

    os.environ.setdefault( 'DEVELOPMENT', 'True')
    os.environ.setdefault('SECRET_KEY', 'your_value')
    os.environ.setdefault('STRIPE_PUBLIC_KEY', 'your_value')
    os.environ.setdefault('STRIPE_SECRET_KEY', 'your_value')
    ```

    Replace <your_value> with the values from your own created accounts:
    - [STRIPE_PUBLIC_KEY](https://dashboard.stripe.com/test/apikeys) *Required from the developer's API on*
    - [STRIPE_SECRET_KEY](https://dashboard.stripe.com/test/apikeys) *Required from the Developer's API on*
    - [SECRET_KEY](https://djecrety.ir/) *Required from an online key generator*

1.  Set up the databases by running the following management command in your terminal:
    ```bash
    python manage.py migrate
    ```

1.  Create a superuser so you can have access to the django admin by running the following command in your terminal:
    ```bash
    python manage.py createsuperuser
    ```

1.  Now that the server is running, we need to add the required data into the database in the following order:
    ```
    python manage.py loaddata groups.json
    python manage.py loaddata customers.json
    python manage.py loaddata itemtags.json
    python manage.py loaddata items.json
    ```

1.  Finally start your server by running the following management command in the terminal:
    ```bash
    python manage.py runserver
    ```
    If everything went correctly the terminal will provide a message telling that the development server is running
    at a provided URL mostly:  (http://127.0.0.1:8000/admin)

1.  Open the URL provided by the terminal including (/admin/accounts/customer/1/change/)
    Connect the customer to an user (it's the first inputfield)
    Provide the company information for all the required fields and press the "SAVE" button on the bottom right.

### Heroku deployment
To run this application in a cloud-based environment, you can deploy the code to Heroku. This section assumes you have succeeded at running the application in your local environment first, as described above.

1.  Login to Heroku and set up a new app with an unique name (NOTE: silkscreenservice is already taken)
1.  On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.
1.  After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku. Make sure you load the 
    following:
    
    |           Key           |      Value     |
    |:-----------------------:|:--------------:|
    | AWS_ACCESS_KEY_ID       |  <your_value>  |
    | AWS_SECRET_ACCESS_KEY   |  <your_value>  |
    | DATABASE_URL            |  <your_value>  |
    | SECRET_KEY              |  <your_value>  |
    | STRIPE_PUBLIC_KEY       |  <your_value>  |
    | STRIPE_SECRET_KEY       |  <your_value>  |
    | USE_AWS                 |  <your_value>  |

    Grab the DATABASE_URL link from Heroku's Config Vars as we gonna need it later to migrate
    to the Heroku Postgres database.

1.  Now that the database on Heroku is created the following rule needs to be added to the env.py file
    ```bash
    os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>')
    ```
    >Be assured to not share this URL with anybody.

1.  Because this is a new database connection, the migrate command must be executed with the following command in your terminal:
    ```bash
    python manage.py migrate
    ```
    >Do not forget to reactivate your virtual environment if the system or IDE is rebooted.

1.  Create the superuser for the postgres database so you can have access to the django admin.
    ```bash
    python manage.py createsuperuser
    ```

1.  Now we need to add the required data into the database in the following order:
    ```
    python manage.py loaddata groups.json
    python manage.py loaddata customers.json
    python manage.py loaddata itemtags.json
    python manage.py loaddata items.json
    ```

1.  With everything set push the code to a GitHub account of yourself:
    ```bash
    git init
    git commit -m 'getting ready to deploy to Heroku'
    git push -u origin
    ``` 

1.  From the Heroku dashboard of your newly created application, click on the "Deploy" tab, then scroll down to the "Deployment method" section and select GitHub.

1.  Use the GitHub link and type in the name of the repository and click the search button. Then connect the Heroku app to the desired GitHub repository.

1.  On the Deployment Tab, scroll a bit further down to the "Manual Deploy" section, select the master branch then click "Deploy Branch".

1.  Once your application is running, you may want to update the Deployment method from Manual to Automatic.

1.  From the Heroku dashboard select the Open app button on the top right.
    Add the following part to the end of the URL in the address bar (/admin/accounts/customer/1/change/) and login with the created superuser credentials.
    Connect the customer to an user (it is the first input field)
    Provide the company information for all the required fields and press the "SAVE" button on the bottom right.

1.  Go to the main admin page and click the Users option under the AUTHENTICATION AND AUTHORIZATION tab.
    Under the Permissions tab at Groups select the admin in the left box and push the arrow to switch it to the right box.
    Press SAVE on the bottom right corner of the page.
    The deployed project is now ready to be used.

## Credits

### Content
All text content for this system were written by me.
The following site has been used as an inspiration for the overall design: [Illustrations.co](https://illlustrations.co/)

### Media
Illustrations: https://illlustrations.co/

### Acknowledgements
- Django Framework 3.0 Crash Course Tutorials [link](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
- freeCodeCamp.org - How to Build an E-commerce Website [link](https://www.youtube.com/watch?v=YZvRrldjf1Y)
- W3schools.com [link](https://www.w3schools.com/)
- Django 3.0 documentation [link](https://docs.djangoproject.com/en/3.0/)
- Django Admin Cookbook [link](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/introduction.html)
- SVG compressing [link](https://www.compresss.com/compress-svg.htm)
