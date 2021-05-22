
Requirements



pip install pymongo

pip install flask



Connectinf with MongoDb



Creating Database (in MongoDB Atlas)
Go to the MongoDB Atlas site and log in.
Create a new project, name it as you like (eg. Kenobi).
Create a new cluster. For that, click on "Build a Cluster".
Choose a path of your choice (there's a free plan also).
Select a cloud provider and region (eg. Google Cloud, and Mumbai).
It would take a few minutes to create the cluster.

Once it's created, click on "Connect".
On the screen that follows, click on "Add your current IP address" for the section "Whitelist your connection IP address". Under that, in the "Create a MongoDB User" section, add a username and password, and note it down. Then, click on "Choose a connection method".
On the "Choose a connection method" tab, select "Connect your application"and copy the connection string that proceeds it.

Go to your project folder. Go to the Server directory.
cd Server
Inside there, create a new file and name it '.env', or run in the terminal
touch .env
Open the .env file in a text editor you prefer and copy
ATLAS_URI=<insert the connection string here> Save the file.

In the terminal, run
nodemon server.js
If nodemon is not installed, run
node server.js
You should be able to see the message
MongoDB connection established
if it all went smooth.
  
To run this project
  
  python main.py
