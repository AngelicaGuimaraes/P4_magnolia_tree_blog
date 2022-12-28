# Magnolia Tree Blog

![Responsive screenshot](/media/images-readme/amireponsive-blogpage.png)

# The purpose with this project

Magnolia Tree Blog is a tool that was added to my first milestone project for CI with the purpose of enriching the expirience of the users of the web site Magnolia Tree. Magnolia Tree Blog was developed as a student project for the Code Institute Full Stack Program. Magnolia Tree Blog offers users a way to share their experiences in relation to yoga and learn more about different contents from other user's posts. It also allows them to comment and like posts, as well as seeing other user's comments and likes so they can interact on conversations.

All comments and post that are created by users, need to be revewed and published by the Admin of the site, so no information that goes against the site's regulations and rules goes published unallowed.

Required technologies for this project: 

 - HTML, CSS, JavaScript, Python+Django
 - Relational database

A live version of this project can be found at this url: https://magnolia-tree.herokuapp.com/

# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Goals](#user-goals "User Goals")
  + [User Stories](#user-stories "User Stories")
    + [Site User](#site-user "Site User")
    + [Site User / Admin](#site-user-admin "Site User / Admin")
    + [Site Admin](#site-admin "Site Admin")
  + [Project Purpose](#project-purpose "Project Purpose")
  + [Design Diagram](#design-diagram "Design Diagram")
    + [Homepage](#homepage "Homepage")
    + [Classes Page](#classes-page "Classes Page")
    + [Contact Page](#contact-page "Contact Page")
  + [Site Navigation](#site-navigation "Site Navigation")
  + [Blog Navigation](#blog-navigation "Blog Navigation")
  + [Database ERD](#database-erd "Database ERD")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Sign In](#sign-in "Sign In")
    + [Signup Form](#signup-form "Signup Form")
    + [List of Posts](#list-of-posts "List of Posts")
    + [Post Details](#Post-Details "Post Details")
    + [Create Post](#create-post "Create Post")
    + [List of Categories and Sections](#list-of-categories-and-sections "List of Categories ans Sections")
    + [Add Comment](#add-comment "Add Comment")
    + [Give Like](#give-like "Give Like")
    + [Delete Post](#delete-post "Delete Post")
    + [Delete Comment](#delete-comment "Search Results")
    + [Delete Like](#delete-like "Delete Like")
    + [Site Admin Features](#site-admin-features "Site Admin Features")
    + [Approve Post](#approve-post "Approve Post")
    + [Delete Content](#delete-content "Delete Content")
  + [Features Left to be Implemented](#features-left-to-be-implemented "Features Left to be Implemented")
+ [Languages used](#languages-used "Languages used")
  + [Frameworks and libraries and tools](#frameworks-and-libraries-and-tools "Frameworks and libraries and tools")
  + [Installed packages](#installed-packages "Installed packages") 
+ [Testing](#testing "Testing")
  + [Bugs during development](#bugs-during-development "Bugs during development")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Deployment](#deployment "deployment")
+ [Content](#content "Content")
+ [Credits](#credits "Credits")

## UX

### User Demographic

This application is ment for:
 - All users who want to read about different categories of yoga.
 - All users who want to write about their own experiences in relation to yoga.
 - All users who want to comment on posts that are published on the blog page.
 - All users who want to like someone's post.
 - All site admins who want to share content with the site users.
 - All site admins who want to control what has been writen and commented.
 - All site admins who want to allow and publish what users have written or commented.

### User Goals

To have all publications and everything else related to it, stored in one place so that the users and admins can access easily whenever wanted or necessary.
To have a good overview of all posts, comments, likes and interactions.

### User Stories

The following user stories has been implemented in the project. User Stories are based on two types of users, the site user and the admin. More user stories will be implemented in future versions.

#### Site User

As a **site user** I can **view a list of posts** so that **I can select one to read**

As a **site user** I can **click on a post** so that **I can read the full text**

As a **site user** I can **register an account** so that **I can comment and like posts**

As a **site user** I can **leave comments, edit and delete comments, on a post** so that **I can be involved in the conversation**

As a **site user** I can **like or unlike a post** so that **I can interact with the content**

As a **site user** I can **create draft posts** so that **I can finish writing the content later**

As a **site user** I can **I can upload images to my posts** so that **I can make the content more attractive**

#### Site User / Admin

As a **site user/admin** I can **view the number of likes on each post** so that **I can see which one is the most popular or viral**

As a **site user/admin** I can **view comments on an individual post** so that **I can read the conversation**

#### Site Admin

As a **site admin** I can **create, read, update and delete posts** so that **I can manage my blog content**

As a **site admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**

### Project Purpose

From Code Institutes assessment guide:

In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

### Design Diagram

The idea of Magnolia Tree Blog was to follow the same design concepts as the Magnolia Tree web page.
Focusing on the data and the CRUD was the initial intention and using Bootstrap as much as possible. The initial design templates was very simple. Focus was to be able to incoorporate all the user stories in a clean, neat and functional way.

#### Homepage
![Homepage](/media/images-readme/screencapture-homepage.png)

#### Classes Page
![Classes Page](/media/images-readme/screencapture-classespage.png)

#### Contact Page
![Contact Page](/media/images-readme/screencapture-contactpage.png)

### Site Navigation

![Site navigation](/media/images-readme/sitenavigation.png)

### Blog Navigation

![Blog Navigation](/media/images-readme/blognavigation.png)

### Database ERD

![Schema](/media/images-readme/ERD.png)

[Back to top](#magnolia-tree-blog)

## Features 

Magnolia Tree Blog consists of two main features for Users:

Create an account so they can have full access as a site user
Add, delete and update their own content on the site

Site Admins main features are:

Publish posts and comments made by Users
Delete anyone's content at any time

### Existing Features

#### Sign In

![Sign in](/media/images-readme/screencapture-signin-form.png)

#### Signup Form

![Signup Form](/media/images-readme/screencapture-signup-form.png)

#### List of Posts

![List of Posts](/media/images-readme/screencapture-blogpage.png)
![List of Posts2](/media/images-readme/screencapture-postspage-2.png)

#### Post Details

![Post Details](/media/images-readme/screencapture-postdetails.png)

#### Create Post

![Create Post](/media/images-readme/screencapture-createpost.png)

#### List of Categories and Sections

![Lis of Categories and Sections](/media/images-readme/screencapture-categories-sections.png)

#### Add Comment

![Add Comment](/media/images-readme/screencapture-comment-field.png)

#### Give Like

![Give Like](/media/images-readme/screencapture-postlikes.png)

#### Site Admin Features

Site Admins can perform all the features as the Users plus publishing the posts and comments that have been written by users and are awaiting for approaval to go online.

![Approve/Delete Post](/media/images-readme/screencapture-delete-post.png)

Site Admins can also delete any content, previously approved and published, at any time.

![Delete Content](/media/images-readme/screencapture-delete-comment.png)

## Features Left to be Implemented

Following features are planned

 - Social Media Sharing
 - Related Posts
 - Featured Posts
 - Author Bio
 - Newsletter signup

[Back to top](#magnolia-tree-blog)

## Languages used

 - HTML5
 - CSS3
 - Javascript
 - Python
 - Django
 - SQL - Postgres

### Frameworks and libraries and tools

 - GitPod
 - GitHub
 - Django
 - Bootstrap
 - DrawSQL
 - Jquery

### Installed packages

 - asgiref==3.6.0
 - cloudinary==1.30.0
 - dj-database-url==1.2.0
 - dj3-cloudinary-storage==0.0.6
 - Django==3.2.16
 - gunicorn==20.1.0
 - psycopg2==2.9.5
 - pytz==2022.7
 - sqlparse==0.4.3

## Testing 

All testing in this project has been done manually during the development process, the project has not followed the principles of test driven development. Testing has for the most part followed the track of the user stories. Everytime a user story is concluded testing has occured. Each version has been tested before commited and the testing has been conducted in these steps:

 - Code validation
 - Functionality (That it actually does what it is supposed to)
 - Bug elimination
 - CRUD (On those sections when this occur)

During the development process a lot of bugs have been discovered. A portion of them are presented in the Bugs during development section.

Functionality testing has been conducted by the author of the project together with selected class mate and selected resources that are aknowledged in the Credit section.

### Bugs during development

There have been several small bugs during development. Most of them has been resolved by fixing faulty syntax but also a lot of them has been caused by logical errors. More sever bugs have been:

- All users had admin rights
  - Solution: Creating function that closes admin for non-staff users (Mentors)
- Problems in getting a proper datestamp using date-selector in create session
  - Solution: Creating a date-picker in widget.py and use widget in forms
- Problem: Not allowing users to log in with only e-mail
  - Solution: Scrapping auth user model and creating new custom user models based on BaseUserManager.
- Problem: Custom CSS not "active" on heroku
  - Solution: Set Collect Static to 0 and not use debug mode in settings.py

Andy many more smaller ones that caused different types of errors but mostly were connected to bad syntax.

### Validator Testing 

Testing with https://validator.w3.org/ shows no errors on html:

![Validator testing](image)

Testing with lighthouse gives the following results:

![Validator testing](image)

Testing and validating using pep8 validations tools:

All python code in this project is not perfect. Some are showing errors of lines that are to long, especially in settings.py and in other files that are installed as part of django. The majority of the problems are not causing errors and are not from code that I actually wrote. Therefore it's not possible to produce a clean slate of a perfect record since some of the code is not perfect but still functional.

Testing with https://jigsaw.w3.org/css-validator/ shown no errors on CSS:

![Validator testing](image)

### Unfixed Bugs

- Responsiveness is bad on smaller screens. Been trying to fix it but for some reason it is problematic.
- Notes can't be created withouth choosing student, auto fill is not working correctly
- Help modal sometimes shows up at bottom at screen, can't figure out why.

 [Back to top](#magnolia-tree-blog)

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

The project was developed using Gitpod with regular commits to Github. In order to deploy to Heroku a requirements.txt file needs to be created
and it is important that the database is created in Heroku so that the database can be migrated before actual deployment.

Before migrating the database I used the following cofigvars:

 - key: SECRET_KEY | value
 - key: PORT | value
 - key: DATABASE_URL | value

All values were provided by Heroku and I used env.py to store the values for my project and used the variables for the values in settings.py for the Database url and secret key. Heroku also needs to be set as an allowed host in settings.py (please see settings.py in this repository for details).

Migration of database can be done prior of deployment. If set up correctly your environment will use Herokus database and not local sqlite.

Before the push to GitHub a procfile needs to be created with the content: web: gunicorn blog.wsgi

After deployment push to Github the project was deployed from Heroku using the "Deploy" tab.

After those steps were taken the application was deployed at the following link: https://magnolia-tree.herokuapp.com/

## Content 

All content in the app and on the site has been produced by the author of the project.

## Credits 

### For code inspiration, design inputs, help and advice.

I have consulted numerous websites, individuals and slack channels to get support for the code. No code block is directly copied (a part from the ones stated in the comments in the code) but some generates from information I gathered from other developers and sites:

 - [W3 Schools](https://www.w3schools.com) for helping me understand Django.
 - [Code Institute](https://codeinstitute.net/) for all course material leading up to this project.
 - [Stack Overflow](https://stackoverflow.com/) for hours of searching and troubleshooting.

 All code that I have borrowed have been commented in the code.

### Acknowledgment

 - [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) My mentor at Code Institute, thank you for your support.
 - [Mats Simonsson](https://www.linkedin.com/in/mats-simonsson-2aa6874/) My dear friend and mentor. Thank you for all the patience, suggestions, advices and for spending so much time helping me with this project. You are truly the best!

 [Am I Responsive](http://ami.responsivedesign.is/) was used to create the image on top of this ReadMe