# Hello World Apparel

Hello World Apparel is the final project built for grading for the Code Institute. It is an ecommerce store that combines front-end and back-end frameworks. The platform that was built to sell high-quality apparel and products that primarily sells t-shirts, mugs, pins, pillows and masks. The store contains designs that I myself have created and sold over the past 5 years. Eventually I would like to use this website as a starting point to flesh out and make it available to the public to buy products I have created.

To test the website's checkout functionality, use the following payment credentials:

- **Card number:** 4242 4242 4242 4242
- **Expiry date:** Any date in the future
- **CV2 number:** Any 3 digits
- **ZIP**: 42424

---

## Table of Contents
1. [**UX**](#ux)
    - [**Business goals**](#business-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Font**](#font)
        - [**Colour Scheme**](#colour-scheme)
        - [**Images**](#images)
        - [**Icons**](#icons)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Recommendations for future implementation**](#recommendations-for-future-implementation)

3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Database Models**](#database-models)

4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

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
- to contact the company
- to search for items
- to add items to a cart
- feedback when I interact with forms
- a clear terms and conditions page
- to read a FAQ
- to purchase a product with a credit card
- an overview of an order I just placed
- to find information about past orders I have made

### Wireframes

I used Balsamiq to complete my wireframes as part of the design and planning process for Hello World Apparel. Balsamiq was used because of it's simplicity and its efficiency in creating designs using its pre-built components. I made minor changes throughout the development stage of the project, so my website looks slightly different than the wireframes based on user feedback as part of the iterative design process. The core concept of the website is still there.

Each link below contains a desktop, tablet and mobile view for each of the respective areas of Hello World Apparel:

- [Landing page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Home%20page.png)
- [Product listings page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Product%20Listings%20page.png)
- [Register page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Registration%20page.png)
- [Login page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Login%20page.png)
- [Single product detail page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Single%20product%20page.png)
- [Shopping cart page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Cart%20summary%20page.png)
- [Checkout page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Checkout%20page.png)
- [Contact page](https://raw.githubusercontent.com/orlamadden/hello-world-apparel/master/wireframes/Contact%20page.png)

### Design

It was important to keep the design simple for Hello World Apaprel. Some ecommerce websites can overwhelm users with various colours, buttons and links which can make it hard for users to focus on searching for products and making a purchase. Hello World Apparel is minimalistic in design with a focus on a good user experience to help users find items they are looking for and have a seamless checkout experience.

#### Font

The font of choice for this project is Gothic A1 from Google fonts. I chose this font as it is simple and characteristc. The font is clean and gives off a sense of fun for Hello World Apparel as it sells humerous products.

#### Colour Scheme

For this project, I kept design and color to a minimum so users could focus on the core functionality of the website. The primary colours of the website is orange, white, black and light grey. Orange is used in moderation, primarily for bringing important information to attention, or used as the primary call to action on a page. The light colours of white and grey help the orange to stand out so user's notice it. The choice of colour was inspired from one of my favourite websites, [Loot Crate](https://www.lootcrate.com/).

![https://res.cloudinary.com/orla2020/image/upload/v1600609779/ms4/ms4-palette_h7zshy.png](https://res.cloudinary.com/orla2020/image/upload/v1600609779/ms4/ms4-palette_h7zshy.png)

#### Images

The product images used across the website have been created by me in Photoshop. Aside from programming, a hobby of mine is creating pop culture t-shirt designs, and the designs on Hello World Apparel are some designs that I have created and sold over the past 6 years. 

#### Icons
Fontawesome icons were used across the website to aid in displaying content and navigation.

##### back to [top](#table-of-contents)

---

## Features

This section will outline all the features of Hello World Apparel implemented by page.

### Current Features

### :page_facing_up: All pages

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

### :page_facing_up: Home page

#### Best sellers

- The best sellers list on the home page are product listings that are marked as featured by the site admin
- The featured option is a boolean value that is in the Product model

### :page_facing_up: Sign up page

#### Registration Form

- A user who is not logged in can create a new account using the register page. 
- The registration requires an email address, email confirmation, a username (which must be unique), a password and password conformation fields.
- The form was created using Django Crispy Forms.

#### Registration using Facebook

- A user has the option to register for an account with Hello World Apparel using their Facebook credentials. This was implemented using django-allauth.
- The user will be redirected to Facebook to input their Facebook email information.
- Once they complete this step, they will need to verify their email address.
- Upon verification, they can access Hello World Apparel using their Facebook details.

### :page_facing_up: Login page

#### Log in form

- A user who is registered can log in using their username and password.
- The form was created using Django Crispy Forms.

#### Login using Facebook

- A user can log in using their Facebook credentials once they have completed the socail registration process in the previous section.

### :page_facing_up: Product listings page

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

#### Delete modal 
- When the super user is logged in, they have the option to delete a product from the product listings.
- A modal displays as an extra layer of defensive design when the super user clicks delete, to make sure that they want to delete this listing from the store.

### :page_facing_up: Product details page

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

### :page_facing_up: Reviews

#### Leaving a Review
- To leave a review, a user must purchase an item.
- The review form becomes available on the product details page after the item is purchased.
- Customers who purchased the item can leave a comment and a rating.
- The review is published immediately.

#### Current reviews
- Current reviews are displayed on the left side of the product page, after the product description.

### :page_facing_up: User profile page

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

### :page_facing_up: Shopping cart

- The shopping cart page features a summary of all the items the user has added to their shopping cart.
- Each item includes an image, product name, size (if applicable) SKU, unit price and total price.
- The user has the ability to adjust the quantity in their cart. A user can also remove an item from their cart. When the quantity is updated. the subtotal will reflect the change.
- Cart total, delivery total and grand total of the user's cart are reflected in the order summary.
- A call to action button to proceed to checkout takes the user to the payment section.

#### Toast notification

- When a user adds an item to their cart, a toast notification displays with the item information.
- A user is notified of the free delivery threshold and how much more they would need to spend to get free delivery.
- A all to action to visit the checkout is displayed below the item information.

### :page_facing_up: Checkout page

#### Checkout form

- The checkout page features a form that needs to be filled out by the user.
- If this is a logged in user's first time to check out, they need to fill out their billing information.
- Details required are name, address, email address, street address, town/city, postal code, county/state/locality and country.
- I included 2 custom made secure checkout and fast shipping images on the checkout page. It helps users to feel they can trust the website.

#### Stripe

- Users can complete the checkout process by entering their card details.
- Payment is handled though the secure Stripe API.
- Once a user clicks to buy, and if successful payment is made, the user is taken to the checkout success page.

#### Checkout success

- The order confirmation page gives the customer all their order information.
- An order number is generated on checkout.
- The user is invited to continue shopping after checkout.

### :page_facing_up: About page

- The About page features a brief description about Hello World Apparel.
- The page provides a call to action button at the bottom of this page to visit the shop.

### :page_facing_up: Contact page

#### Contact form

- The contact page contains a form for the user to fill in to send to the store admin.
- Name, email address and message are all optional fields.
- An email is sent to the store admin's email address notifiying them of a new contact enquiry in the admin dashboard.
- The message can be checked by logging in to the admin area.

#### Toast notification

- When a contact form has been successfully submitted, the user is notified via toast message.

## Recommendations for future implementation

#### Reset password
- Allow users to reset their password if they forget it.

#### Additional checkout methods
- For a future update, I would like to include the ability for users to checkout via PayPal as it is a popular checkout method.

#### Discount codes
- I'd like to include a field for customers to enter discount codes that adjust the final cost of the shopping cart.

#### Two Step verification
- With cybercrime on the rise and the recent trend of many bank applications introducing two-step verification, this would be a nice extra layer of security for users when logging in.

#### Custom 404 and 500 pages
- Create and implement custom pages for HTML status codes of 404 (Page Not Found) and 500 (Internal Server Error). Given the time constraints, this was not possible to implement.

#### Pagination
- An attempt had been made at implementing pagination on the product listing page. However, there was conflict with sorting and filtering, so due to time constraints, I decided not to implement this.

#### Admin Dashboard for super user
- Under the Product Management tab, I'd like to include a dashboard that would include:
  - adding products
  - a dropdown selector of current products to open up and edit
  - a sales graph that includes the total of sales per month and the most popular product by sales

##### back to [top](#table-of-contents)
---
## Information Architecture

### Database choice

- During development in Gitpod I worked with the standard sqlite3 database which comes installed with Django out of the box.
- On deployment, the SQL database installed in Heroku is a PostgreSQL database.

### Database Models

All models were created with Django's ability to auto-assign a Primary Key (ID). 

#### User Model

The User model used for this project is the standard one provided by Django.

#### Category Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=250 | CharField
Friendly Name | friendly_name | max_length=250, null=True, blank=True | CharField

#### Product Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category
SKU | sku | max_length=254, null=True, blank=True | CharField
Name | name | max_length=254 | CharField
Description | description | blank | TextField
Has Sizes | has_sizes |blank | BooleanField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Rating | rating | max_digits=6, decimal_places=2, null=True, blank=True | DecimalField
Image URL | image_url | max_length=1024, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField
Featured | featured | default=False | BooleanField

#### Order Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to User
Full Name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
Postcode | postcode | max_length=20, null=True, blank=True | CharField
Town / City / Locality | town_or_city | max_length=40, null=False, blank=False | CharField
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address1 | max_length=80, null=False, blank=False | CharField
County | county | max_length=80, null=True, blank=True | CharField
Country | country | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Grand Total | grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Shopping Cart | original_cart | null=False, blank=False, default='' | TextField
Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

#### Order Item Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | on_delete=models.CASCADE | ForeignKey to Order
Product | product | on_delete=models.PROTECT | ForeignKey to Product
Product size | product_size | max_length=2, null=True, blank=True | CharField
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

#### Review Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Product | product | on_delete=models.CASCADE, null=True, blank=True, related_name="reviews" | ForeignKey to Product
User | user | on_delete=models.PROTECT | ForeignKey to User
Comment | comment | max_length=1000, blank=True, null=True | TextField
Rating | rating | default=1 | FloatField

#### Contact Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=200 | CharField
Comment | comment | max_length=1000, blank=True | TextField
Email | email | max_length=200 | EmailField
Contact Date | contact_date | default=datetime.now | DateTimeField
User | user_id | User, null=True, on_delete=models.CASCADE | ForeignKey to User

##### back to [top](#table-of-contents)
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

##### back to [top](#table-of-contents)
---
## Testing

The write up for Testing can be found here: [TESTING.md](https://github.com/orlamadden/hello-world-apparel/blob/master/TESTING.md)

##### back to [top](#table-of-contents)
---

## Deployment

This project was deployed on Heroku: https://hello-world-apparel.herokuapp.com/

### Running project locally

Follow the instructions below to run this project in your own Interactive Development Environment (IDE), such as VSCode or PyCharm. **Please note:** If you use PyCharm as your IDE, this process is easier with a one click installation of Django.

Make sure that the following are installed on your device (this is necessary):

- [Python 3](https://www.python.org/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

You will also need to create free accounts with the following services:

- AWS and set up an S3 bucket
- Stripe

#### Instructions

1. Save a copy of the github repository located in this repository by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

`https://github.com/orlamadden/hello-world-apparel.git`

2. To install the project's dependencies, it is recommended to create a virtual environment to prevent the dependencies from being installed globally on your system, therefore keeping it in the virtual environment.
To create a virtual environment for your project, in the Terminal, in the project's root directory, enter:

`python -m venv venv`

and then activate the created virtual environment with

`venv\Scripts\activate`

3. Install all requirements from the requirements.txt file using this command:

    `pip3 -r requirements.txt`

4. In the IDE terminal, use the following command to launch the Django project:
`python manage.py runserver`

5. In the root directory of the project, create an `env.py` file. Immediately store this file in a `.gitignore` file. This will prevent your sensitive data from being committed and pushed to GitHub.

6. In your `env.py` file, set the environment variables as follows:

```
os.environ["AWS_ACCESS_KEY_ID"] = "<your key here>"
os.environ["AWS_S3_REGION_NAME"] = "<your AWS Sregion name here>
os.environ["AWS_SECRET_ACCESS_KEY"] = "<your key here>"
os.environ["AWS_STORAGE_BUCKET_NAME"] = "<your AWS Sbucket name here>"
os.environ["SECRET_KEY"] = "<your secret key here>"
os.environ["STRIPE_PUBLIC_KEY"] = "<your key here>"
os.environ["STRIPE_SECRET_KEY"] = "<your key here>"
os.environ["STRIPE_WH_SECRET"] = "<your key here>"
```
7. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:

- `python3 manage.py createsuperuser`

8. Next, you'll need to make migrations to create the database schema (outlined above) using the commands as follows:
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

8. The application can now be run locally.

### Deploying to Heroku

Hello World Apparel was deployed to Heroku by doing the following:

1. App created on Heroku called **hello-world-apparel**
2. Added Heroku Postgres ("Hobby Dev - Free" option) under the resources tab.
3. In the Heroku dashboard Under the **Settings > Reveal Config Vars**, entered the following configuration variables:

| Key | Value |
--- | ---
SECRET_KEY | <"your key here">
STRIPE_PUBLIC_KEY | <"your key here">
STRIPE_SECRET_KEY | <"your key here">
STRIPE_WH_SECRET | <"your key here">
AWS_ACCESS_KEY_ID | <"your key here">
AWS_SECRET_ACCESS_KEY | <"your key here">
AWS_STORAGE_BUCKET_NAME | <"your bucket name here">
USE_AWS | "True"
EMAIL_HOST_PASS | <"your app password as generated by Gmail (if you use it)">
EMAIL_HOST_USER | <"your email address that is used to send emails">

4. Created a `requirements.txt` file in project so Heroku can install the required dependencies to run the app using the following command:  
`sudo pip3 freeze --local > requirements.txt`

5. Created a `Procfile` in the root project folder and entered:  
`web: gunicorn hello_world_apparel.wsgi:application`

6. Went back to Heroku and copied the value of DATABASE_URL and entered into my `env.py` file.

7. Migrated the database models to the Postgres database on Heroku by running the following commands:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

8. Created the super user as outlined in the **Running project locally** section above. 

9. Went to 'Deploy' tab on the Heroku dashboard and connected to my project's Github repository.

10. Selected 'Enable Automatic Deploys' in the 'Automatic Deployment' section and make sure that the Master Branch is selected.

11. Performed a `git push` to Github. This also pushed the project to Heroku.

12. After the build was completed, navigated to the 'Open app' button to open the project in the browser.

13. Hello World Apparel was successfully deployed.
 
### Setting up Social Login (Facebook)

Hello World Apparel has a feature for Facebook users to sign up and log in using their Facebook credentials. The following steps were taken to implement this feature.  

**Please note:** This feature was implemented after the project was deployed to Heroku. I am unsure of how this would work in a local setting. Please see the docs for more information - https://developers.facebook.com/docs/

1. Installed django-allauth using the following command:  
`pip3 install django-allauth`
2. Included the following in my `settings.py` file:  
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.facebook',
```
3. Added the following to `settings.py`:
```
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
```
4. Also added the following to `settings.py`:
```
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}
```
4. Went to Facebook for Developers via this link - https://developers.facebook.com/. 
(If you want to implement this feature and do not have a Facebook account, you will need to sign up for one [here](https://www.facebook.com/)).
5. Create a new app via the dashboard.
6. Select **For Everything Else**.
7. Gave my app a name, e.g. HelloWorldApparel, etc. Clicked **Create App**
8. Selected **Set Up** under the Facebook Login product.
9. Selected **Web**.
10. Entered website url, e.g. https://hello-world-apparel.herokuapp.com/ and click save.
11. Under **Settings > Basic**, copied the App ID and App Secret Key.
12. Logged in to website admin dashboard. 
13. Under Sites, added site domain name and display name, e.g. https://hello-world-apparel.herokuapp.com/
14. Click into **Social Accounts > Social applications** (at the very bottom of the dshboard)
15. Clicked **Add social application**
16. Under provider, selected Facebook.
17. Entered name of social account (same as app name in step 7 for consistency).
18. Input App ID into Client id (see step 11)
19. Input App Secret into Secret Key (see step 11)
20. Under sites, added the site I entered in step 13 from available sites to chosen sites.
21. Clicked save.
22. `django-allauth` comes pre-installed with templates for setting up social login, so logging in via Facebook was now available.
 
 ##### back to [top](#table-of-contents)
 ---

 ## Credits

 ### Code
 - Without the amazing videos from the Code Institute and Chris Zielinski, this project would not have been possible. While every attempt has been made to make this website my own, some elements and code may remain the same, especially setting up Stripe.
 - This course from Brad Traversy was used for assisting in creating the Contact page - https://www.udemy.com/course/python-django-dev-to-deployment/learn/lecture/12056484#overview
 - Implementing the Facebook login was done with the help of this Youtube video - https://www.youtube.com/watch?v=kp1JINkOdTw
 - Review product implementation for my product details page and circular shopping cart counter icon was sourced and amended to meet my needs from CI student's (Stevo) [Github repository](https://github.com/nemixu/Milestone4/).

 ### Media
 - Hero image mock up was downloaded from [here](https://mockupsforfree.com/down?q=Pillow%20On%20The%20Sofa%20Mockup). I used Photoshop to include my design on the pillow.
 - All product images were created by me in Phototshop.

 ### Content
 - Terms and conditions page referenced from [Asos](https://www.asos.com/terms-and-conditions/).
 - FAQ page referenced from [Teefury](https://teefury.com/apps/help-center#hc-can-i-make-a-change-to-my-order-or-cancel-it).
 - Privacy policy page referenced from Asos and Teefury (links above).
 - All other text content was written by me.

 ### Acknowledgements

Massive thanks to my family and friends for helping with testing this project, and my past projects throughout the duration of this course.

The CI Slack community have been an incredible source of inspiration and help since day 1. I look forward to staying in touch with the community when the course ends.

I would like to thank my mentor, Antonio Rodriquez for his support throughout the course.

This course has been a challenge, and I am very much looking forward to working on new projects in the future with the knowledge I have. I am sad to be finishing the course, but excited for all the possibilities that programming gives you.

 --------

For educational purposes only.
