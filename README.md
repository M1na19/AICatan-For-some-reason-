#DOCUMENTATION AND EXPLANATION
https://docs.google.com/document/d/1hQ-L3MCxd1eD-uKnd1WcKTyZc07qfhOSoCZ8NMabZ5s/edit?usp=sharing

#MATERIALE CU DREPTURI DE AUTOR CARE NU NE APARTIN
IMAGINI{'images/background.png',
  'images/bricktile.png',
  'images/desert.png',
  'images/graintile.png',
  'images/hexagon.png',
  'images/oretile.png',
  'images/player.png',
  'images/rolling_dice.gif',
  'images/spotlight.png',
  'images/woodtile.png',
  'images/wooltile.png',}

# STEPS TO FOLLOW TO SETUP THE PROJECT
# HOW TO RUN THE PYTHON SERVER
Step 1: Install Flask
Make sure you have Flask installed on your machine. You can use pip, the package installer for Python, to install Flask. Open a command prompt or terminal and run the following command:

pip install flask

Step 2: Create a Flask Application
Create a new Python file, for example, app.py, and open it in a text editor or an integrated development environment (IDE). Import the necessary Flask modules and create a Flask application instance:

python

from flask import Flask

app = Flask(__name__)

Step 3: Define Routes and Functions
Define the routes of your application and the corresponding functions that will be executed when those routes are accessed. Routes are defined using the @app.route decorator. Here's an example of a simple route:

python

@app.route('/')
def home():
    return 'Hello, World!'

Step 4: Run the Application
At the end of your app.py file, add the following code to run the Flask application:

python

if __name__ == '__main__':
    app.run()

Step 5: Start the Server
Open a command prompt or terminal, navigate to the directory where your app.py file is located, and run the following command:

python app.py

The Flask development server will start running, and you should see output indicating that the server is running on a specific address, usually http://127.0.0.1:5000/ or http://localhost:5000/.

Step 6: Access Your Flask Application
Open a web browser and enter the address http://127.0.0.1:5000/ or http://localhost:5000/. You should see the response from your Flask application, which in the example above would be "Hello, World!".

# HOW TO RUN THE HTTP SERVER WITH THE DATABASE
Steps to run the application

Step 1:To run the above code you should first have the mongoose server running

After setting up mongoDB start the server using following command

mongod

Step 2: Type the following command in terminal of your project directory

node app.js

Step 3: Open your web browser and type the following address in the URL bar

http://localhost:3000/
