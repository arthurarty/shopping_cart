[![Maintainability](https://api.codeclimate.com/v1/badges/7c4f2a9909e8be9651a9/maintainability)](https://codeclimate.com/github/arthurarty/shopping_cart/maintainability)

# shopping_cart
A shopping cart api designed in Python. The aim of this repo was to create a database wrapper using plain SQL and named tuples. Design patterns implemented include the singleton design pattern. Abstract Base Classes are used to create the DB interface. (SOLID principles.)

## How to set up.
- Create a postgres database.
- Clone the repo.
- Ensure you are on the dev branch.
- Create a `.env` file from the `.env_example`.
- Run command `python create_tables.py`. This runs the code in the file `create_tables.py` which creates the necessary tables for the application to work.

## Run application
- Run the command `python run.py`.

#### Expected output
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-482-972
 ```

- Use postman to interact with application.

Project Overview
--------------------------------
|Endpoint |Functionality |Note |
|---------|:------------:|:---:|
|POST /auth/signup|Register a user| |
|POST /auth/login |Login a user | |

## Built With

* `FLask` : [Flask](http://flask.pocoo.org/) is a micro web framework written in Python.
* `abc` : [abc](https://docs.python.org/3/library/abc.html) This module provides the infrastructure for defining abstract base classes (ABCs) in Python.

## Authors

* **Nangai Arthur** - [Linkedin](www.linkedin.com/in/arthur-nangai)
