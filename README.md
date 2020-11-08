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

#### **Lighthouse desktop**
![lighthouse desktop](https://github.com/djacura/game-hq/raw/master/assets/testing/lighthouse-desktop.jpg "lighthouse desktop")
#### **Lighthouse mobile**
![lighthouse mobile](https://github.com/djacura/game-hq/raw/master/assets/testing/lighthouse-mobile.jpg "lighthouse mobile")

The only issue really here was the size of the images used on the site it was making it load slower, this is something I still need to change to make the site run faster and optimise it.

## Manual Testing

For the manual testing of the site I went on User stories and also had a few friends and family test and feed back results as below:

| Test | Expected | Passed |
| :------------- |:-------------| :-----:|
| User loads the main page of site | Page displays without error and reviews can be viewed | &#9745; |
| User can see the main page with reviews listed in order of star rating | Page displays and reviews are listed ion correct order | &#9745; |
| The User registers for account | Page loads and correctly allows user to create account | &#9745; |
| User loads the profile page of the site | Page displays without error and their reviews can be viewed | &#9745; |
| The User selects the view review button | The correct review is then displayed correctly | &#9745; |
| The User selects the add a star button | The star is added and the count goes up by one | &#9745; |
| The User clicks on the search amazon button | a new tab is created with the amazon webiste and searches correct game name | &#9745; |
| The User clicks on the new review link at the top  | The correct page and form is loaded to create a new review | &#9745; |
| The User clicks on Add review button on new review page | The flash message is shown and the review is added to the database | &#9745; |
| The User clicks on edit review button on the review page | The edit review page and form is correctly loaded with fields populated | &#9745; |
| The User clicks on Delete review | The modal pops up to confirm they want to delete review and review is then deleted | &#9745; |
| The User Clicks on Delete Account | The modal pops up to confirm they want to delete their account and reviews and then the account is deleted along will all reviews from that user | &#9745; |
| The User searches for a game on the main page | if search matches criteria then games are shown if not error message shown | &#9745; |
| The User enters wrong information in forms  | The validation should not allow user to input wrong text and if they missed a field | &#9745; |
| The User tried to edit or delete another users review | Users cannot see edit or delete buttons for reviews not their own | &#9745; |
| The user clicks on navigation links in top bar | the links all work | &#9745; |
| The User clicks on nav links in bottom bar | the links all work | &#9745; |
| Used Website works on multiple browsers | Used Chrome, Edge and Firefox browsers | &#9745; |
| The admin User can manage genres | The admin user was only one to be able to manage genres | &#9745; |
| The admin User can edit and delete reviews | The admin user was able to edit and delete other reviews | &#9745; |
| The User clicks on the reset buttion on search bar | this resets search and shows all games | &#9745; |
| The User clicks on Login | User taken to login screen and can login without error | &#9745; |
| The User enters incorrect login details | displays Flash message showing that the details are incorrect | &#9745; |
| The User clicks on Logout | The User is successfully logged out of the session and site | &#9745; |
| The User clicks on home or the Logo | They User is directed back to the main page | &#9745; |

---

## **Coding**

This section I wanted to talk about some of the code I used specific to this site and some of the bugs I encountered while making the site.

## Sorting the reviews

To make the reviews sort the reviews by stars I used the following code which I then used in the profile page as well. this allowed me to sort the reviews descending in order of how many upvotes the reviews have recieved. 

~~~
games = list(mongo.db.games.find().sort('upvote', pymongo.DESCENDING))
~~~

## Amazon link

To make the amazon link functionality I used a search function to be able to search amazon based on the game name entered in the database.
the link is made by using a default amazon search link and then appending the name of the game on the end while removing the spaces in the name.
This then builds and amazon link and then is inputted into the form when creating a new review and then added to the database with the other info.

~~~
amazonlink = 'https://www.amazon.co.uk/s?k='
    while ' ' in game:  # this replaces the spaces in the name with +
        game = game.replace(' ', '+')
    amazonlink += game

    return amazonlink  # returns the newly built amazon link
~~~

## Bugs

One of the bugs I encountered very early on in the development stage was that I was unable to get the contents of the mongo database to be carried over into the site,
after checking alot (for about 3 days) I could figure out why the database was not coming across, eventually I resorted to student support for help with this as was hitting a wall.
The team had a look and after a while we then figures out it was that I had my Gitpod variables permanently set in settings and was using setting from a previous project.
I need to remember to check [Gitpod Settings](https://gitpod.io/settings/) when I next encounter this issue.

Another bug that I encountered was that during the midpoint review with my mentor that he couldn't see himself as the creator when he made a review the field was blank see below:

![user missing](https://github.com/djacura/game-hq/raw/master/assets/testing/reviewed-by-missing.jpg "user missing")

We thought this was because he had started his username with a number rather than a letter but I have tested this issue see below and found that not to be the case so this one is still to be looked into if this issue is still
present as I have not been able to recreate this bug.

![user letter](https://github.com/djacura/game-hq/raw/master/assets/testing/reviewed-by-letter.jpg "user letter")

Also when we had our midpoint review the select genre validation of the form was not working it wasn't showing that the user hadn't selected a genre and so no warning was given why they couldn't submit the form.
This was then fixed by using the validation Jquery from the task manager miniproject.

~~~
validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});
~~~

This allowed the validation to work and the field to change to red when nothing was selected.

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