# Portfolio Project

In this project, you will build a portfolio website using plain HTML and CSS (Bootstrap 5).  
This project can be ongoing and you can add to it as you progress through the course.  At the end, you could have a nice personal website showcasing your portfolio, links to your social media and github accounts and a good documentation and proof of your journey and skills as a programmer.

# Setup

1. Clone or Download this repository to you local machine. It contains some sample images that you can use, as well as a screenshot of the site you'll be building.  Grab what you need then delete the repo from your local machine. No need to keep it.

<!---1. Create a repository using Github Classrooom. (You will be provided with the link).  This is where you will build your portfolio. **You should also fork the repository so you have a copy for yourself**. Later, we can transfer ownership to you.-->

# Building the Site

Remember, you can modify your site however you feel. You can choose your own colors, or use standard ones. 
The website does not have to work (links, buttons etc). It just has to look good with HTML and CSS You can come back later and modify them with functionality.

## Getting Started
1. Create a root folder for your project called "profile", or whatever you like, wherever you like, even the desktop is fine.
1. Copy the images folder into your new root folder. All the image files you need are available from the Setup step above. You can download more images as needed.
1. In the root folder, create two new files, index.html and main.css. 

## Setting up the Template

1. Choose a font for your site. You can find some good ones using the google fonts api.  Raleway is a nice one for this site, but you can choose any you like. You can include them in your css using:
    ```css
    @import url('https://fonts.googleapis.com/css?family=Raleway');
    
    html,h1,h2,h3,h4,h5,h6,a{
        font-family: "Raleway";
    }
    ```
1. Reset your template (google how if you don't know). 
1. Add the required parts to make it a proper HTML page.
Add semantic tags for the navbar, header, and multiple profile sections. 

## Navbar

1. Use the navbar provided by Bootstrap. Modify it for your needs.
* **Note** the navbar has class "fixed-top" which gives it an fixed position at the top of the page.

## Header

1. Set the header background-image. 
1. Make the background-attachment fixed so we can overlay things on top of it.
1. Make the background-size cover the whole div.
1. Set background-position to center
1. When writing on the header, remember to give the text an absolute position.
* **Note** The header should take 100% of the screen size. Remember how to do that in pure CSS?

### Overlay

1. You can make an overlay by placing `<div id="overlay"></div>` directly inside your header.
1. You can style similarly to https://www.w3schools.com/howto/howto_css_overlay.asp. Try make it white to fade out the background image.

## The Sections

1. Space them nicely
1. Kepp things responsive by using the Bootstrap grid.
1. For the *Blog* section, use Bootstrap4 "Cards". They are prebuilt elements ready to use."
1. For the *Contact* section, use a form and the Bootstrap form controls.
1. You can add social media icons using one of Bootstraps recommended Icon Sets.

# ! Important !

1. Work hard!
1. Focus!
1. Help eachother!
1. Work in pairs to solve problems and figure things out. It's a great way to learn!
1. Ask for help! But first, give a few different solutions a good try.
1. Enjoy!




