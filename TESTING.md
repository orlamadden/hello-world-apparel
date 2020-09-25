# Hello World Apparel - Testing

[Go back to main README.md file](README.md)

[View deployed website on Heroku](https://hello-world-apparel.herokuapp.com/)

## Table of Contents

1. [User Stories Testing](#user-stories-testing)
2. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
3. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)

---
## User Stories Testing

During the testing phase, I asked family and friends if they could achieve the goals outlined below in the user stories.

As a user of the site I want and/or expect:

1. to browse products on the website
- all users used the main navigation as their starting point to search for products :white_check_mark:
- the filter function and sort by was used to navigate through the product list :white_check_mark:
2. to view details about a product I like on the website
- all users were able to get pricing information and description about the product by clicking into product details :white_check_mark:
- 2 users noted that specific information about t-shirt material was not available, so this is noted for future release :grey_question:
3. to create an account
- all users were able to successfully create an account :white_check_mark:
- 1 user used their Facebook login credentials to sign up :white_check_mark:
4. to view ratings on a product to aid in my decision making
5. to contact the company
- all users found the contact page :white_check_mark:
- all users successfully submitted a contact forms :white_check_mark:
- all forms were visible to the website admin in the admin dashboard :white_check_mark:
6. to search for items
- search functionality was used by one user to search for 'coffee tshirt' :white_check_mark:
- as outlined in #1, the filter function and sort by was beneficial in searching through the product list :white_check_mark:
7. to add items to a cart
- all users were able to add items to their cart :white_check_mark:
- 3 users decided to remove their items, this was successfully completed :white_check_mark:
8. feedback when I interact with forms
- the following feedback was recieved when a user tried to create a username that existed:
`A user with that username already exists.` :white_check_mark:
- the following feedback was recieved when a user tried to create a password:
`This password is too common.` :white_check_mark:
- the following feedback was recieved when a user tried to create a numeric password:
`This password is entirely numeric.` :white_check_mark:
9. a clear terms and conditions page
- all users located the terms and conditions page in the footer of the website :white_check_mark:
10. to read a FAQ
- all users located the FAQ page in the footer of the website :white_check_mark:
11. to purchase a product with a credit card
- all users were successfully able to checkout using a credit card (demo details by Stripe) :white_check_mark:
12. an overview of an order I just placed
- after all user purchased a product, they received an order summary containing details of their order
13. to find information about past orders I have made :white_check_mark:
- on the user profile page, all users found orders they made with an order summary, date, time and order number :white_check_mark:

## Bugs

#### Crispy field import invalid

When I tried to render the checkout page, I was receiving an error `as_crispy_field got passed an invalid or inexistent field`. After checking Slack, I came across another student [Slack post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1595278374343500) who had a similar error. After double checking my form and the view for my form, it appeared I had spelled address incorrectly, hence the error. I corrected this spelling mistake and the form worked.

#### Received unknown parameter

When I was trying to submit my form, I got a notification below my Stripe payment input that said `Received unknown parameter: payment_method_data[billing_details][address][county]`. After investingating the [Stripe documentation in reference to the error](https://stripe.com/docs/api/errors?__hstc=150021993.0a66484947bfb3c9909d36929bef61f2.1473724800071.1473724800073.1473724800074.2&__hssc=150021993.1.1473724800074&__hsfp=1773666937) it appeared that my form was incorrectly referencing county instead of state as per the code in the elements.js file for handling the Stripe form. After fixing this, the payment could be created and submitted.

#### No email showing in terminal

After setting up a confirmation email for users when the purchase an order, the order confirmation would not print in the terminal during testing. I was receiving the error `django.core.mail.message.BadHeaderError: Header values can't contain newlines (got '  \nOrder E4826FA59CF94B84BC8145FAC7156FFA confirmed' for header 'Subject')` in the terminal when I made a test purchase. This solution on [Stack Overflow](https://stackoverflow.com/questions/55903845/badheadererror-with-python-emails-package-how-to-fix) helped me identify that the issue was a spacing error. After fixing this, the confirmation email was visible in the terminal.