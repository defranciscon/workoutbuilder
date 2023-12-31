# Workout Builder Flask Application

The application is a Python-Flask application prototype for running predefined workout circuits.
The user first selects one of four circuit types from the home page.
The user is routed to the selected workout page and is provided a form to enter the required information.
Upon clicking the submit button, the workout is saved in the mongodb database. 
The user must be authenticated to use the app. 
If they do not have an account, they can access the registration form by clicking on the Register link in the navigation bar.
Once they register, they must login to access their home page in which they are given access to the application. 
This is a current prototype version of that app. Some features are written but do not function at this time.
These features will be completed and connected to the rest of the application in future releases. 

## Technology Stack
The web app is a Python application built using the Flask web-framework and some of its useful extensions.
Flask is a Python web microframework designed to provide the minimum amount of functionality needed to create a web application.
The front-end is developed using the Bootstrap v5.3 bundle which is an open-source web browser framework that provides user interface components for creating the client-side views in the browser.
To render the views, we take advantage of the Jinja2 templates to help keep the code organized an accesssible. The Jinja2 templates are stored in the HTML files in the templates directory of the application.
The web app uses the MongoDB database for storing and retrieving data for the application.
MongoDB is a non-relational document database that provides JSON-like storage in a form known as BSON.
MongoDB allows more flexibility when dealing with modeling data and is ideal for this application. 
Two libraries are used for working with MongoDB: Pymongo and MongoEngine. 
Pymongo is a Python package for working with MongoDB and is the recommended method to work with MongoDB from Python.
Using Pymongo with our app allowed us to take advantage of MongoDB's flexible nature and enabled us to have more control of how our data is accessed and stored particularly for the the exericesa and workouts.
MongoEngine is a library is an Object-Document Mapper that is built on top of Pymongo which offers an avenue for providing some structure to the data.
MongoEngine is used with the simpler data models that don't require the same flexibility such as users and works well with the WTForms and Flask-Form libraries.

## Application Architecture 
The application's architecture is designed to be modular and easy to maintain.
The main module is held in the webapp directory which is a comprised of several respective Python modules containing its own necessary views, web forms, and modules.
It is structured using a Model View Controller architecture to enable better scalability for future modifications and easily allows for newly added features.
The idea is to create a separation of concerns by separating the logic between files and modules.
To enable this structure, we take advantage of a concept known as an Application Factory.
The main application module is responsible for creating the Flask application using the factory pattern.
An application factory is a function that creates another object. 
In our case, the application factory takes in one of the config objects from the config.py file and returns a Flask application object. 
In the current phase, we are using the DevConfig child class which inherits from the Config parent or base class.


## Login Screen
![login-screen](https://github.com/defranciscon/workoutbuilder/assets/108236585/4f1285dc-67ee-46e0-a831-e1e7bc96967d)

## Registration Screen
![register-screen](https://github.com/defranciscon/workoutbuilder/assets/108236585/d5636ece-2534-41ad-89ba-22a3af589ad6)

## Home Screen
![home-screen](https://github.com/defranciscon/workoutbuilder/assets/108236585/d46e0043-cdd6-4af3-a2c0-4eb79cde0be0)

## Home Screen - selecting a circuit type
![select-workout](https://github.com/defranciscon/workoutbuilder/assets/108236585/d5229656-cac3-4642-aef5-d2ad3974224e)

## Creating a workout using Flask forms
![create-workout](https://github.com/defranciscon/workoutbuilder/assets/108236585/6c7605a4-8eb5-4df6-bbdd-43a70131bb67)

## Saving the workout using Flask forms
![submit-workout](https://github.com/defranciscon/workoutbuilder/assets/108236585/5938b2aa-e444-4d68-82fe-153a8a84c88a)

## Storing the workout to the MongoDB database
![saved-workout-json](https://github.com/defranciscon/workoutbuilder/assets/108236585/39b95abd-871c-47f4-8759-099a910d90d8)

