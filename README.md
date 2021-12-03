# FlaskApplication
Basic  flask application for managing users


![github-small](https://user-images.githubusercontent.com/32481242/144520537-cdeb67f0-f68b-4021-b937-bd1cdcca1052.png)


# STACK INFORMATION 
The app is written in Python on top of the Flask micro-framework. The Front-End was written in Html, Php and Flask Boostrap. SQlite was implemented as the database of choice, in conjunction with the SQLAlchemy ORM to simplify CRUD operations.

# LIST OF FEATURES 
The following are the main high-level features available through the app

* Users can register and login 
* Users can modifie his own informations
* Users can display other users informations 

# How to use use this repo
* Fork this repo and rename it 
* Read "Instructions for development" below (modify as necessary for your app)

# Instructions for development

Clone the repository:


```
git clone https://github.com/DORGAA/FlaskApplication.git
```

In your terminal go to the app folder /app and set Environment variable configs as :

 * SECRET_KEY 
 * SQLALCHEMY_DATABASE_URI
 * SQLALCHEMY_TRACK_MODIFICATIONS 
 
```
export CONFIGURATION_SETUP="config.DevConfig"
```

```
export CONFIGURATION_SETUP="config.DevConfig"
```
set application secret key: 

```
export SECRET_KEY="Chosse a secret key"
```
run app: 

```
flask run 
```
