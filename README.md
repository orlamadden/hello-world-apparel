# Hello World Apparel

Hello World Apparel is the final project built for grading for the Code Institute. It is an ecommerce store that combines front-end and back-end frameworks.

---

## Table of Contents
1. [**UX**](#ux)
    - [**Project purpose**](#project-purpose)
    - [**Business goals**](#business-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Recommendations for future implementation**](#recommendations-for-future-implementation)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Bugs**](#bugs)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

### Project purpose

Hello World Apparel was built as the final milestone project for the Code Institute Full Stack Web Development diploma. It is an ecommerce platform that was built to sell high-quality apparel and products to the developer community. The website primarily sells t-shirts, mugs, pins and masks. 

### Business Goals

The business goals of Hello World Apparel is:
- provide top quality products to all its customers
- to engage with its shoppers via social media channels
- build brand awareness through social media
- have more than 500 monthly active users on the website
- generate sales through a simple to use checkout platform


### User Stories

As a user of the site I want and/or expect:

- to browse products on the website
- to view details about a product I like on the website
- to create an account
- to view ratings on a product to aid in my decision making
- to contact the company with a question
- to use a search box to find something specific
- to add items to a cart
- feedback when I interact with forms
- a clear terms and conditions page
- to read a FAQ
- to purchase a product with a credit card
- to login using my social media account (nice to have, will try)
- an order summary of an order I just submitted
- to find information about past orders I have made

### Wireframes

I used Balsamiq to complete my wireframes as part of the design and planning process for Hello World Apparel. Balsamiq was used because of it's simplicity and its efficiency in creating designs using its pre-built components. I made minor changes throughout the development stage of the project, so my website looks slightly different than the wireframes based on user feedback as part of the iterative design process. The core concept of the website is still there.

Each link below contains a desktop, tablet and mobile view for each of the respective areas of Hello World Apparel:

- Landing page
- Product listings page
- Register page
- Login page
- Single product detail page
- Shopping cart page
- Checkout page

### Design

It was important to keep the design simple for Hello World Apaprel. Some ecommerce websites can overwhelm users with various colours, buttons and links which can make it hard for users to focus on searching for products and making a purchase. Hello World Apparel is minimalistic in design with a focus on a good user experience to help users find items they are looking for and have a seamless checkout experience.

#### Font

The font of choice for this project is Gothic A1 from Google fonts. I chose this font as it is simple and characteristc. The font is clean and gives off a sense of fun for Hello World Apparel as it sells humerous products.

#### Colour

For this project, I kept design and color to a minimum so users could focus on the core functionality of the website. The primary colours of the website is orange, white, black and light grey. Orange is used in moderation, primarily for bringing important information to attention, or used as the primary call to action on a page. The light colours of white and grey help the orange to stand out so user's notice it.

![https://res.cloudinary.com/orla2020/image/upload/v1600609779/ms4/ms4-palette_h7zshy.png](https://res.cloudinary.com/orla2020/image/upload/v1600609779/ms4/ms4-palette_h7zshy.png)

#### Images

The product images used across the website have been created by me in Photoshop. Aside from programming, a hobby of mine is creating pop culture t-shirt designs, and these are some designs that I have sold over the years. 

##### back to [top](#table-of-contents)

---

## Features

This section will outline all the features of Hello World Apparel implemented by page.

### Current Features

### All pages

#### Top navbar

- The top most navbar contains the search functionality of the website. The brand logo in the top left always redirects users back to the home page. 
- A user who is currently logged out can access the registration page or log in page through the user icon. 
- A logged in user can access their profile or log out through the user icon.
- The checkout icon displays a pricing summary of the user's current order in their cart.

#### Main navbar

- The main navbar contains a dropdown filter for navigating quickly though Hello World Apparel.
- Included in the main navigation is access to:
   - All products: navigates to all products in the Hello World Apparel store
   - Most popular: navigates to the most popular products in the Hello World store (based on sales)
   - Office kits: navigates to an apparel bundle
   - On sale: navigates to items that are on sale

### Home page

#### Best sellers

- The best sellers list on the home page are product listings that are marked as featured by the site admin
- The featured option is a boolean value that is in the Product model

### Sign up page

#### Registration Form

- A user who is not logged in can create a new account using the register page. 
- The registration requires an email address, email confirmation, a username (which must be unique), a password and password conformation fields.
- The form was created using Django Crispy Forms.

#### Registration using Facebook

- A user has the option to register for an account with Hello World Apparel using their Facebook credentials. This was implemented using django-allauth.
- The user will be redirected to Facebook to input their Facebook email information.
- Once they complete this step, they will need to verify their email address.
- Upon verification, they can access Hello World Apparel using their Facebook details.

### Login page

#### Log in form

- A user who is registered can log in using their username and password.
- The form was created using Django Crispy Forms.

#### Login using Facebook

- A user can log in using their Facebook credentials once they have completed the socail registration process in the previous section.

### Product listings page

#### Sort products

- The product listings page includes the option to sort its results by:
   - Price - low to high
   - Price - high to low
   - popular

#### Category filter

- On the left side of the product listings page are a list of categories that match all products in Hello World Apparel
- Users can filter by t-shirts or masks, for example.

#### Products list

- Products in the shop are displayed as thumbnail images with the product title and price displayed underneath each thumbnail.
- When users click on a product card, they are taken to the details page of the selected product.
- If a super user is logged in, they have easy access to edit or delete a product.

#### Pagination

- Pagination was implemented using Paginator.
- A maximum of 12 products is displayed per page.

### Product details page

#### Listing details

- Each product detail page features an image of the product on sale.
Sometimes a group photo is included as well to show off more mice from the same collection.
- The product title, price and description are all clearly visible on the product listing page to the right of the image.
- There are certain products, such as t-shirts, that require sizing information. If applicable, there is a size dropdown selector to allow users to choose their size.
- A numeric input selector allows the user to select the quantity of a product they wish to purchase. The minimum product quantity a user can purchase is 1, with the maximum being 99.
- Users can add a product to their cart by clicking the "Add to cart" button or continue shopping by clicking the "Keep shopping" button.

#### Toast notification

- When a user selects a product, they are notified of their selection through a success toast message.
- They are then given the option to continue shopping or view their cart.

### User profile page

#### Billing details

- The users profile page can only be accessed by a logged in user. 
- The account page contains the user's billing information that they can edit and update. This billing information will automatically be included in the checkout process to save time for the user.
- An order summary is visibile if user's have made a purchase in Hello World Apparel. This will contain:
   - Order number
   - Date an item was purchased
   - Item(s) purchased
   - Order total

#### Toast notification

- When a user updates their billing information they are notified of this change through a success toast message.

---

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
- [Python](https://www.python.org/about/)

### Libraries, Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Gunicorn](https://gunicorn.org/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [boto3](https://pypi.org/project/boto3/)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
- [flake8](https://pypi.org/project/flake8/)
- [Stripe](https://stripe.com/ie)
- [PostgreSQL](https://www.postgresql.org/)

### Tools

- [Gitpod](https://www.gitpod.io/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [AWS S3](https://aws.amazon.com/)
- [Balsamiq](https://balsamiq.com/)
- [Git](https://git-scm.com/about)
- [GitHub](https://github.com/)

--------

For educational purposes only.
