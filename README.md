# Silkscreenservice
**Milestone project 4: Full Stack Frameworks with Django - Code Institute**

For a silkscreen-press company a need for a services order system has been requested. 
The main goal of the system is to make the job of our studio employees easier and more efficient. 
For the customer we would like to provide an easy to understand and easy to use system so, 
they will be able to make their service requests easier.

In short:
- A system for employees to be more efficient.
- A easy to understand system for customers to remove some workload from the studio employees.

## Demo
A live demo version can be found **[here](https://silkscreenservice.herokuapp.com/)**

![Design](https://github.com/D1ang/Silkscreenservice/blob/master/mockups/presentation.png)

## UX
To make the system as clear as possible to the end-user a basic but very clean design has been chosen.
Options are minimalistic and the end-user will not be overloaded with options to choose from.
The navigation bar, buttons and dashboard have been built with this in mind and have an easy to understand logic.

## User stories
With years of field experience, we have built a well-known form and work ethic in creating designs.
We asked our customers from day to day what they would like to see in a sample and came up with the following points:

 - As a user, I want to easily fill in the forms for a service request (**services**)
 - As a user, I want to upload my artwork fast in the same system (**checkout form**)
 - As a user, I want a secured overview of my order history (**dashboard**)
 - As a user, I want to the system to remember my cart for if I want to make changes later on (**cart**)
 - As a user, I don't want to fill in my details everytime, but do want to change them if needed (**profile**)
 - As an employee, I want to know which service are required per order (**order**)
 - As an employee, I want to change the status of an order (**admin list actions**)
 - As an employee, I would like to download the artwork (**order details**)
 - As an employee, I want to search and filter the orders (**search & filter**)

### Strategy
The goal of the tool is to make it as easy as possible to access, short and informative,
while striving for a minimalist and user-friendly design as possible.

### Scope
For customers, we wanted to provide them with an easy to understand (first-view-use) system.
This way, they would be able to request services: faster, easier and on their own,
so our studio employees have more free time for other job-related tasks and be able to do
their service tasks more efficient.

### Structure
The system is structured to get the right information as quickly as possible.
The order of the options provided are placed in a logic workflow while the design provided will use a messages bar
that should be easy to understand and gives the customer a straight away no-nonsense feedback.
The navbar is available when needed and a footer is provided with contact information.

### Skeleton
By using Figma the following wireframes were created:

[Silkscreenservice wireframe](https://github.com/D1ang/EasyLedger/blob/master/mockups/wireframe.pdf)

[Responsive phone wireframe](https://github.com/D1ang/EasyLedger/blob/master/mockups/wireframe-sm.pdf)

### Surface
The colours chosen are: yellow, red, black and blue.
Blue is the most used colour most commonly associated with harmony, faithfulness, confidence, and imagination.
A very clean, abstract and an almost childish design has been chosen to force the attention to the provide design.
Users won't be scared or afraid to use the system by this easy to understand design.
The font Poppins had been chosen because of its look that fits perfectly to the buttons and graphics on the homepage.
As for the dashboard a lighter version of Poppins has been used as it looks very clean and is easy to read.
The buttons are style in 2 versions full black or black outlined to fit the overall design.


## Technologies
1.  Figma - *To create a wireframe*
2.  HTML - *To create the basics*
3.  CSS - *To improve placements and design*
4.  JavaScript - *The engine to create user interaction*
5.  Python 3.8.2 - *To communicate to the backend*
6.  Postgres 4.2.6 - *Opensource database to save the transactions*
7.  Django 3.0.7 - *Micro web framework in python*
8.  Bootstrap 4.4.1 - *To make the design responsive*
9.  Font Awesome 5.13.0 - *Easy icon access for the icons*
10. Font Awesome animations 0.3.0 - *additional animations for the Font Awesome icons*

### JavaScript Libraries
1. jQuery 3.4.1 - *To improve input field feedback*
2. flatpickr 4.6.3 - *lightweight, powerful JavaScript datetimepicker with no dependencies*
3. DataTables 1.10.20 - *Adds advanced interaction controls to HTML tables*

### Python & Django Plugins
1. Pillow 7.1.2 *Python Imaging Library*
2. stripe 2.48.0 *Creditcard payments end transaction security*
3. django-allauth 0.42.0 *Authentication, registration & account management*
4. django-countries 6.1.2 *Provides country choices for use with forms*
5. django-crispy-forms 1.9.1 *Controls the rendering behavior of Django forms*

## Features
xxxx

### Features Left to Implement
In the future I would like to add a custom admin page with more functionality.
Also, I would like to add some animations to the landing pages to make a nicer user experience.

## Testing
All fields will function, and everything will be properly written to the database.

This site was tested across multiple screen sizes on Chrome, Safari, and Internet Explorer. To ensure compatibility and responsiveness it is also tested on an android based mobile device (OnePlus5).

xxxx

## Bugs

XXXX

The following tests have been used to ensure proper site functionality:

- [GTmetrix](https://gtmetrix.com/): To test on website loading times.
- [W3C HTML Validator](https://validator.w3.org/): This validator checks the mark-up validity of Web documents in HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This validator checks the mark-up validity of Web documents in CSS.
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB): Inspecting on overflow errors.
- [Autoprefixer CSS online](https://autoprefixer.github.io/): Autoprefixer is a PostCSS plugin which parses your CSS and adds vendor prefixes.
- [JSHint](https://jshint.com/): A static code analysis tool for JavaScript.
- [Visual Studio Code](https://code.visualstudio.com/): Using the built-in tools to test on proper code.

## Deployment
The example of this code is hosted by using Heroku and Amazon, this code is deployed to GitHub directly from the master branch.
The deployed site will update automatically upon new commits to the master branch.

To run locally, you can clone this repository directly into the editor of your choice by entering
`git clone https://github.com/D1ang/Silkscreenservice.git` into your terminal.
To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

When the code is downloaded as a .zip it can be unzipped.
To get it up and running some extra steps need to be taken as will be explained in the following text:

- The code will be executed in the browser that is set as main browser, this can be Chrome or one of the other available browsers.

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
