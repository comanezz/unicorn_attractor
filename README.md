[![Build Status](https://travis-ci.org/comanezz/unicorn_attractor-milestone5.svg?branch=master)](https://travis-ci.org/comanezz/unicorn_attractor-milestone5)

# Unicorn attractor website

Milestone Project 4: Full Stack Framework with Django - Code Institute

This website allows people who are using my software to report bugs and ask to work on new features they would like to have implemented. They are able to create bug/feature tickets, comment them and like them. To implement the feature they have to contribute for 20 euros. Feature with the most contributions will be handled first. This is how we are going to prioritize our workflow.

This website helps me to show the skills that I learned, how to build a full-stack website and manage data. 

## Demo

A live demo can be found [here](https://unicorn-attractor-aymeric.herokuapp.com/).

## UX
**The primary target audiences are Unicorn attractor software users that would like to submit bugs, request new features and comments on posts if they want to share their experience or ask questions.**

#### User Stories:

- A user have an issue in the Unicorn attractor software and wants to report it to have it fixed.
- A user wants to implement a new feature that will be good to improve the software.
- A user wants to see all the bug tickets that have been created to see if the problem they encounter have already been mentioned.
- A user wants to see all the feature tickets that have been created to see if the feature they would like to have has already been requested.
- A user wants to comment on tickets (bug or feature) to discuss them or share with other user.

#### Wireframes

- [Home view](https://github.com/comanezz/unicorn_attractor-milestone5/blob/master/static/wireframes/home_wireframe.jpg)
- [Page list view](https://github.com/comanezz/unicorn_attractor-milestone5/blob/master/static/wireframes/page_list_wireframe.jpg)
- [Form view](https://github.com/comanezz/unicorn_attractor-milestone5/blob/master/static/wireframes/form_wireframe.jpg)

## Features

**All pages**

- Each page has a responsive **navbar**.
- Navbar
    - Logo navigate to the home page. 
    - All others button redirect the user to the appropriate page.

**Home page**

This page present a brief description of the website and what the user will be able to do. It allows the user to see what can be done regarding bugs and how to see/create a ticket. It also allows the user to understand what can be done for new features and how to see/create them. For each bug or feature section, there is two shortcut button possible: View tickets/requests or create ticket/request.

**Bug / Feature List page**

This page allows the user to view all the bugs/features that have been created by users. They can see relevant information related to a specific bug/feature as number of: comments, votes, contributions and the status. But they do not see the full title or description of the ticket.
If a user is logged, he has the possibility to create a new bug/feature ticket.
If there is too many bugs/features listed, a pagination allowing user to navigate between pages will appears.
If a user is not logged, he can still click on new ticket button but he will be redirected to the log in form.

**Bug detail page**

This page allows the user to see the bug ticket in details. Meaning that they will see the full title and description. Also the user can see all the comments and replies that have been posted.
If the user is logged, he can upvote or downvote the ticket, comment or reply to comments. 
If the user is the author of the ticket, he is able to edit that ticket. Otherwise, no edit to the ticket is possible.
If the user is not logged in, he will not be able to upvote or use the comment section. However he will still be able to read comments and replies.

**Feature detail page**
This page allows the user to see the feature ticket in details. Meaning that they will see the full title and description. Also the user can see all the comments and replies that have been posted.
If the user is logged, he can upvote or downvote the ticket, comment or reply to comments. He can also contribute to features he wants to see implemented.
If the user is the author of the ticket, he is able to edit that ticket. Otherwise, no edit to the ticket is possible.
If the user is not logged in, he will not be able to upvote or use the comment section. However he will still be able to read comments and replies.

**Profile page**

This page allows the logged in users to see their personnal informations as: username, email and the date that they first joined the website. Also the user is able to see how many bugs/features tickets he has created. 
If the user is not logged in, no profile page button will appear.

**Register page**

This page allows the user to create an account and be able to login into the website. 

**Login page**

This page allows the user to login into the website or reset his password. 

**Pending contribution page**

This page allows the user to see all feature tickets added to their cart and allow them to proceed to checkout and pay.

**Checkout page**

This page allows the user to pay for the selected items. 

### Features Left to Implement
- In the bug/feature detail page. When we click on the reply button, the reply section opens and close when you have added a comment. Then, you have to click on the reply button again to see the new comment added. Maybe add a feature where the reply section stays open when we add a new comment. 
- Add history of purchase into the profile page. 
- On profile account, add the possibility to modify the email of the user. If the user need to change his email address but still keep his current account instead of creating a new one.
- I would like to merge two apps into one app for example feature and bug because they are very similar. 

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
    - Check if deleting an item from the cart is possible. Item removed.

- Checkout app
    - Check that the checkout page shows the right number of items selected.

- Bugs / Features app
    - Try to upvotes and downvote the ticket. Make sure that it adds +1/-1 to the vote section.
    - Try to add comments and replies. Which add +1 into the comments section everytime a comment or reply has been added.

- Account app
    - Make sure that the profile page shows the correct information about the user.
    - Make sure that the profile page shows the numbers of tickets created by user.
    - Make sure that the user is able to reset his password.

### Issue found
- Coverage html not working properly. It is showing wrong data saying that a lots of things is missing and also does not show all the test files added after the first command coverage html. Checked with tutors, they were not able to help regarding that and mentioned that it was not a big deal as long as I run enough test.
You can run the test locally by using python3 manage.py test in the terminal. 

- When we go to the password reset confirm page. When we use DevTool and switch to see the mobile view the page is not responsive. But it is if we access directly from a mobile. For example when we click on the reset link from the mobile directly the page is responsive. 

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
        - Helped me with comments, reply, upvote and other things.
    - [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
        - Helped me understand how annotation works and also the function vars() which is really helpful to see value it returns.
    - [Samuli Natri](https://www.youtube.com/channel/UC_F-PRC-SXbaGj_kmMZSotA)
        - Helped me with pagination.

- Useful link that helped me:
    - [Help me learn about url pattern with primary key and slug fields.](https://simpleisbetterthancomplex.com/references/2016/10/10/url-patterns.html)

    - [Help me understand slug field.](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django)

    - [Help me understand how to modify the modified date field in a model](https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add)