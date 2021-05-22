# Read Me Template

---


## Description

This a login page to test out the Flask framework.A project for beginners.
#### Technologies

- Flask
- MongoDB
- Python

[Back To The Top](#read-me-template)

---

## How To Use

To signin just enter your name,email and it gets saved in a database.Then further you can login with the same credentials to access the dashboard.

#### Installation

pip install pymongo

pip install flask


[Back To The Top](#read-me-template)

---


## Connecting with MongoDb
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

Go to your project folder. Go to the main python file directory.

ATLAS_URI=<insert the connection string here> Save the file.
You should be able to see the message
MongoDB connection established
if it all went smooth.
  

In the terminal, run
python main.py
  
  
  
[Back To The Top](#read-me-template)

---
