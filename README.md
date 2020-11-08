![mock ups image](https://github.com/djacura/game-hq/raw/master/assets/mock-ups-image.jpg "Mock-ups Image")

# Game HQ

This is my Game HQ Webiste, that I have created using HTML, CSS, Javascript and Python code using Flask and Mongo DB and then deployed on Heroku. 
This website is intended for for users to be able to view game reviews from different people, and then be able to register and then login and add, edit and then delete reviews of their own, then if they like another persons review they can then give that review a star.

# Table of Contents

table of contents here!

# UX

### **Project Goals**

The Aim of my project was to be able to create a site where user could go and look at game reviews and then be able to read them and then if they feel that game was for them
they could then go and buy that game and play it and if they like that review give it a star, now I also wanted them to be able to create a profile where they could then add their own reviews and then add, edit and delete 
their reviews, then I wanted to be able to create a way you could see the top reviews based on how many stars they had recieved from other users.
I also wanted a way for the user to be able to go to amazon to buy that game that could be later used for Monetization for each successful referal.

### User Goals

* To be able to view reviews and give them a star.
* To be able to register an account and then login.
* To then be able to add, edit and remove a review.
* To be able to remove their account and the reviews as well.
* To then be able to go to amazon and find that game to buy. 

### User Stories

1. As a User I want to be able to see reviews, so I can make a decision on wether I like the game.
2. As a User I want to be able to like the review, so I can let the User know I like the review.
3. As a User I want to be able to create a Profile, So I can create my own Reviews.
4. As a User I want to be able Add, Edit and delete Reviews, So that I can make adjustment or fix errors.
5. As a User I want to be able to Remove my account and reviews, So that they are now longer available.
6. As a User I want to be able to go and find that game on amazon, So I can then buy it and play it.
7. As an Admin User I want to able to Edit and delete reviews, So I can moderate the site.
8. As an Admin User I want to be able to Add, edit and remove Genres, So I can make changes to the Genres.
9. As a Site Owner I want to able to see top reviews, So I can see whats popular,
10. As a Site Owner I want to be able to send people to amazon, So that I can make money of sales.


### **Design Choices**

Most of the design of my website came from inspiration from other Game review webistes such as [Gamespot](https://www.Gamespot.com) and from Game retail site [Game](htts://www.Game.co.uk)
These sites helped with the information that I was going to need and the layout of my website.

### layout

The Layout of the site was using a Grid formation and cards and forms taken from the [Materialize](https://materializecss.com/) webiste, this webiste was designed heavily off the back of the task manager mini project, that was done just before this milestone project,
As I feel this had the perfect base layout for creating my review website.

### Fonts

The fonts that I decided to use was "Roboto Slab" and "Montserrat" these were taken from pairings found using [Google fonts website](https://fonts.google.com/) that I took from inspiration from the Game website. And using a default "Sans serif" font.

### Colours

The Colours were found from the same place and was used from the Game webiste as well, the colours used were a close comparison from this website so rather than using black and purple, I used a dark grey colour and a green font.

### Icons

The Icons used on this site were taken from the website [Font Awesome](https://fontawesome.com/)

### WireFrames

The wireframes were created using the Balsamiq application, you can view my PDF of the wireframes that were created at the beggining of this project and I havent modified them based on what the final output of the website looks like. 
[Download Wireframes Here](https://github.com/djacura/game-hq/raw/master/assets/wireframes-for-game-hq.pdf)


# **Features**

### Existing Features

* Users can view reviews and give them a star.
* Users can create their own profile and view, add, edit and delete their reviews.
* Uses can remove their own profiles and with it all their reviews as well.
* Users can use the search function to find a review they are looking for.
* Users can click on the amazon search button to find the game on amazon.

### Features Left to Implement

I hope to be able to incorprate some of the features in the future to this site.

* To be able to Add a review to an existing review.
* To be able to change / reset the account password.
* To stop users adding multiple stars to reviews.
* To Then stop a User adding multiple stars to their own reviews.

# **Technologies Used**

This Project Uses HTML, CSS, Javascript, Python, Flask and MongoDB Technologies.

* [Python](https://www.python.org/) was used to create the application, routes and functions.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) was used to create the templates.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) was used for the database.
* [Jquery](https://jquery.com/) was used for the side nav, forms and select Javascript.
* [Materialize](https://materializecss.com/) was used for the grid system and layout of the website.
* HTML5 and CSS3 was used for the website structure.
* [Github](https://github.com/) was used to store the code in a repository and then [Gitpod](https://www.gitpod.io/) was used to write the code.
* [Heroku](https://www.heroku.com/) was used to deploy the site to the internet.

The project used a database from MongoDB atlas and 3 collections were made in the database for this project:

**Users Collection:**
~~~
{
    "_id":"",
    "username":"",
    "password":""
}
~~~
**genre Collection:**
~~~
{
    "_id":"",
    "genre_name":""
}
~~~
**games Collection:**
~~~
{
    "_id":"",
    "game_name":"",
    "game_developer":" ",
    "game_description":".",
    "genre_name":"",
    "game_review":"",
    "game_image":"",
    "created_by":"",
    "upvote":"",
    "amazon_link":""
}
~~~

# **Testing**

With testing the site I did a mix of automated testing from validation testing sites and manual testing of the site from user stories and had real world users test the site as well.

## Automated Testing

For the Automated testing I used the following sites to check the validation of the code i was using and everything tests all okay.

* [HTML validator](https://validator.w3.org/)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [Javascript validator](https://jshint.com/)
* [Python validator](http://pep8online.com/)
* [Dev tools lighthouse](https://developers.google.com/web/tools/lighthouse)

With dev tools lighthouse see attached screenshot of results

![lighthouse desktop](https://github.com/djacura/game-hq/raw/master/assets/testing/lighthouse-desktop.jpg "lighthouse desktop")
![lighthouse mobile](https://github.com/djacura/game-hq/raw/master/assets/testing/lighthouse-mobile.jpg "lighthouse mobile")

## Manual Testing

For the manual testing of the site I went on User stories and also had a few friends and family test and feed back results as below:

| Test | Expected |Passed |
| :------------- |:-------------| :-----:|
| User loads the landing page of site | Page displays without error and reviews can be viewed | &#9745; |
| User loads the homepage of the site | Reviews are displayed by upvote bite like value in descending order | &#9745; |
| User selects the 'review' button of a particular review on homepage | Review page displays without error and the correct review can be viewed | &#9745; |
| User selects the 'review' button of a particular review on homepage whilst not logged in | Review page displays without error and the correct review can be viewed and the 'edit and 'delete' buttons are not visible | &#9745; |
| User clicks on the upvote bite like on a review page | bite like should increase by 1 | &#9745; |
| User clicks on amazon link on a review page | amazon site should load and show a link to the book if it exists in amazon based on the book title | &#9745; |
| User clicks on delete button on review page when logged in | delete modal should pop up with warning and confirm / cancel buttons | &#9745; |
| User clicks on confirm delete button on review page delete modal when logged in | review is removed from the db and confirmation message displayed | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User logs in | Nav items change from ***login***, ***register*** and ***about*** to ***my profile***, ***my reviews***, ***about*** and ***log out*** | &#9745; |
| User selects ***Register*** from top nav | Register form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Register Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** but enters different values in ***password*** and ***confirm password*** fields| Form does not submit and shows error message to user that passwords must match | &#9745; |
| User enters correct ***username*** and ***password*** and ***confirm password*** fields match| Forms submits, landing page is loaded with message confirming successful registration | &#9745; |
| User selects ***log In*** from top nav | ***log in*** form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Log in Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** and enters correct values in ***password*** field of log in form| form submits and logs customer in and message is displayed to show successful log in | &#9745; |
| User enters correct **username** but enters the wrong values in ***password*** field of log in form| Form does not submit and shows error message to user that password is incorrect | &#9745; |
| User enters incorrect **username** | Form does not submit and shows error message to user that the user does not exist and shows a link to register | &#9745; |
| User tries to **edit** / **delete** a review that they havent created under their username | User is messaged that they can't delete / edit reviews they do not own | &#9745; |
| User **edits** a **review** they own| All edits are submitted successfully once they pass form validation and can be seen when review loads | &#9745; |
| User selects to **delete** a **review** they do not own| user gets warning message informing that they cant delete someone else review | &#9745; |
| User selects to **confirm delete** on delete modal| review is removed from list of reviews and user message| &#9745; |
| User selects to **cancel delete** on delete modal| review is not removed from list of reviews and user return to review page| &#9745; |
| User selects to **delete profile**| delete profile modal pops up with warning| &#9745; |
| User selects to **cancel delete profile** on modal| user is returned to profile without any removals| &#9745; |
| User selects **confirms to delete profile**| profile and all associated reviews are removed, user seesion is removed and user is sent back to index| &#9745; |
---
## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### code

- any code used not mine

### Acknowledgements

- I received inspiration for this project from X