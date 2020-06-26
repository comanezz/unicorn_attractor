[![Build Status](https://travis-ci.org/comanezz/unicorn_attractor-milestone5.svg?branch=master)](https://travis-ci.org/comanezz/unicorn_attractor-milestone5)

# Unicorn attractor website

Milestone Project 4: Full Stack Framework with Django - Code Institute

This website allow users who are using my software to report bugs and ask to work on features they would like to implement into the software. They are able to create bug/feature tickets, comment them and like them. To implement the feature they have to pay for a certain amount. 

This website helps me to show the skills that I learned how to build a full-stack website and manage data. 

## Demo

A live demo can be found [here](https://unicorn-attractor-aymeric.herokuapp.com/).

## UX
**The primary target audiences are users from unicorn software that they would like to submit bugs, feature request. Comments on posts if they want to sure their knowledge or ask for questions.**

#### User Stories:

- A user have an issue in the software and wants to report it to fix it.
- A user wants to implement a feature that will be good to improve the use of the software.
- A user wants to see all the bug/feature tickets that have been created.
- A user wants to discuss about a bug/feature ticket by using comments.

#### Wireframes

- [Home view](https://github.com/comanezz/unicorn_attractor-milestone5/tree/master/static/wireframes/home_wireframes.jpg)
- [Page list view](https://github.com/comanezz/unicorn_attractor-milestone5/tree/master/static/wireframes/page_list_wireframes.jpg)
- [Form view](https://github.com/comanezz/unicorn_attractor-milestone5/tree/master/static/wireframes/form_wireframes.jpg)

## Features

**All pages**

- Each page has a responsive **navbar**.
- Navbar
    - Logo navigate to the home page. 
    - All others button redirect the user to the appropriate page.

**Bug / Feature List page**
This page allows the users to view all the bugs/features that has been created by user. They can see relevant information related to a specific bug as number of: comments, votes, contributions and the status. But they do not see the full title or description of the ticket.
If user is logged, he have the possibility to create a new bug/ticket ticket. 
If there is too many bugs/features list, there is a pagination allowing user to navigate between pages.

**Bug detail page**
This page allows users to the the bug ticket in full. Meaning that they will see the full title and description. Also the user can see all the comments and replies that has been posted.
If user is logged, he can upvote or downvote the ticket and comment or replies comments. 
If the user is the author of the ticket, he is able to edit that ticket.

**Feature detail page**
This page allows users to the the feature ticket in full. Meaning that they will see the full title and description. Also the user can see all the comments and replies that has been posted.
If user is logged, he can upvote or downvote the ticket and comment or replies comments. He can also contribute to the feature if he wants to add it into his software.
If the user is the author of the ticket, he is able to edit that ticket.

**Profile page**
This page allows the user when logged to see his personnal informations as username, email and the date that he first joined the website. Also he is able to see how many bugs/features tickets he has created. 

**Register page**
This page allows the user to create an account and be able to login into the website. 

**Login page**
This page allows the user to login into the website or reset his password. 

**Cart page**
This page allows the user to see what feature tickets have been added to the cart and allowing to go to the checkout page to pay.

**Checkout page**
This page allows to pay for the items selected. 

### Features Left to Implement
- In the bug/feature detail page. When we click on the reply button, the reply section opens and close when uou have added a comment. Then, you have to click on the reply button again to see the new comment added. Maybe add a feature where the reply section stays open when we add a new comment. 
- Add history of purchase into the profile page. 

## Technologies Used

- **HTML5**
- **CSS3**
- **Python** - Programming Language used for the backend of the application
- **IDE** used to develop the website: writting, debugging and running the code.
  - [Visual Studio Code](https://code.visualstudio.com/)
- **Framework**
- [jQuery](https://jquery.com/)
- [Django](https://docs.djangoproject.com/en/1.11/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/gb)
- [Bootstrap](https://getbootstrap.com/)
- **Database** - [PostgreSQL](https://www.postgresql.org/docs/)

## Testing
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and [W3C Markup Validation Service](https://validator.w3.org/) has been used to check the validity of the website code.
- [pep8online](http://pep8online.com/) - check the validity of the Python code. 

## Automated tests
- Used [Travis](https://travis-ci.org/) to test the build.
- Used automated tests in test.py files in each app folder.

## Manual tests
- Made sure that the all website is responsive on all the devices Desktop, Laptop, Tablet and mobile.

- Cart app
    - Tried to add more than 1 same feature into the cart at a time, error message is displayed if same feature is already added in the basket.
    - Check to deleting an item from the cart. Item is removed.

- Checkout app
    - Check that the checkout page shows the right number of items selected.

- Bugs / Features app
    - Try to upvotes and downvote the ticket. Make sure that it adds +1 to the vote section.
    - Try to add comments and replies. Which add +1 into the comments section everytime a comment or reply has been added.

- Account app
    - Make sure that the profile page shows correct information about user.
    - Make sure that the profile page shows the numbers of tickets created by user.
    - Make sure that the user is able to reset his password.

### Issue found
- Coverage html not working properly. It is showing wrong data saying that a lots of things is missing and also does not show all the test files added after the first command coverage html. Checked with tutors, they were not able to help regarding that and mentioned that it was not a big deal as long as I run enough test.

## Deployment
- Project was deployed to heroku. 

    1. Created a requirements.txt used command `pip freeze > requirements.txt`.
    2. Created a Procfile used command `echo web: python app.py > Procfile`.
    3. Push everything to Github.
    4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps).
    5. On deploy tab, selected deployement method > GitHub - set up automatic deploy.
    6. In settings > Config Vars. I set up environment variables:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
        - DATABASE_URL
        - DISABLE_COLLECTSTATIC
        - EMAIL_ADDRESS
        - EMAIL_PASSWORD
        - SECRET_KEY
        - STRIPE_PUBLISHABLE
        - STRIPE_SECRET
    7. The website has been deployed.

- The code is also hosted on GitHub pages, deployed directly from the master branch.

**To copy the code, you can clone it by following these steps:**

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click **Clone or download**.
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. Open the terminal.
5. Type `git clone`, and then paste the URL you copied in Step 3.
``` console
$ git clone https://github.com/USERNAME/REPOSITORY
```
6.Press **Enter**. Your local clone will be created.

To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

### Acknowledgements
- Thanks to the following Youtubers who helped build this website:
    - [Abhishek Verma](https://www.youtube.com/channel/UCOPiE8TU4cphHqeOkos-J5A)
    - [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
    - [Samuli Natri](https://www.youtube.com/channel/UC_F-PRC-SXbaGj_kmMZSotA)

- Useful link that helped me:
    - [Help me learn about url pattern with primary key and slug fields.](https://simpleisbetterthancomplex.com/references/2016/10/10/url-patterns.html)

    - [Help me understand slug field.](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django)

    - [Help me understand how to modify the modified date field in a model](https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add)