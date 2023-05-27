#SHORT EXPLANATION


 Informatii generale

    Categorie: Web
    Judetul: București
    Surse: [GITHUB](https://github.com/M1na19/AICatan-For-some-reason-/tree/main)
    Homepage: http://ramami.go.ro

Descriere

    Play Catan Against Carlos este un joc distractiv si complex in care inteligenta umana este pusa cap la cap cu inteligenta artificiala.

Tehnologii

Frontend

    Bootstrap si w3.css libraries
    Axius is the API that is making the connection with the python server

How it works?

     We have a node.js server with a mongoose database, a game that is connected with an api to the ai that is run on another python server, plus the algorithms that are   used to train the ai.

Backend

    Ejs files and Js files
    Node.js Express server 
    Mongoose database
    Flask for the Python Server
    (full list of libraries in the documentation)

Serverless

    Node.js Server
    Flask Server

Cerinte sistem

    Internet, browser modern

Realizatori

    Boanta Mihai 
    Sirghe Matei

Impartirea Lucrului
    
    Matei Sirghe a lucrat la UI, Serverul node.js, database si evaluator
    Mihai Boanta a lucrat la API, Serverul flask, AI si logica jocului

#DOCUMENTATION AND EXPLANATION

    https://docs.google.com/document/d/1hQ-L3MCxd1eD-uKnd1WcKTyZc07qfhOSoCZ8NMabZ5s/edit?usp=sharing

#MATERIALE CU DREPTURI DE AUTOR CARE NU NE APARTIN

    IMAGINI{'images/background.png','images/bricktile.png','images/desert.png','images/graintile.png','images/hexagon.png','images/oretile.png','images/player.png','images/rolling_dice.gif','images/spotlight.png','images/woodtile.png','images/wooltile.png',}
  
    LINKURI{https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.1/axios.min.js https://i.imgur.com/Ry82F9J.png https://i.imgur.com/DhyH1Xt.png https://i.imgur.com/KaIgpCc.png https://i.imgur.com/cIVhMQv.png https://i.imgur.com/ikUPxHo.png https://i.imgur.com/O23yKZR.png https://i.imgur.com/mbxoOLf.png https://i.imgur.com/H9KBWNy.png https://i.imgur.com/amAWx6q.png https://i.imgur.com/jldnqDd.png https://i.imgur.com/l9yIY2E.png https://i.imgur.com/KILdl8B.png https://i.imgur.com/CEl8Sij.png https://i.imgur.com/amAWx6q.png https://i.imgur.com/jldnqDd.png https://i.imgur.com/l9yIY2E.png https://i.imgur.com/KILdl8B.png https://i.imgur.com/CEl8Sij.png }

# STEPS TO FOLLOW TO SETUP THE PROJECT
# HOW TO RUN THE PYTHON SERVER
Step 1: Install Flask
Make sure you have Flask installed on your machine. You can use pip, the package installer for Python, to install Flask. Open a command prompt or terminal and run the following command:

    pip install flask
    pip install flask_cors
    pip install numpy

Step 2: Setup Flask
 
 FOR WINDOWS:
    
    set FLASK_APP=controller.py
    
FOR LINUX:

    export FLASK_APP=controller.py
    
#WARNING

FOR WINDOWS:

    pickleLocation=os.path.abspath("..")+"//fullBackend//storage//state.pickle"

FOR LINUX:

    pickleLocation=os.path.abspath("..")+"/fullBackend/storage/state.pickle"

(In vscode use just on dot)

Step 2: Start the Server
Open a command prompt or terminal, navigate to the directory where your app.py file is located, and run the following command:

    flask run

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
