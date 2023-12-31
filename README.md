# Workout Builder Flask Application

Flask application prototype for running predefined workout circuits.
The user first selects one of four circuit types from the home page.
The user is routed to the selected workout page and is provided a form to enter the required information.
Upon clicking the submit button, the workout is saved in the mongodb database. 
The user must be authenticated to use the app. 
If they do not have an account, they can access the registration form by clicking on the Register link in the navigation bar.
Once they register, they must login to access their home page in which they are given access to the application. 
This is a current prototype version of that app. Some features are written but do not function at this time.
These features will be completed and connected to the rest of the application in future releases. 

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

