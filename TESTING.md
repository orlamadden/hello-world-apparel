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