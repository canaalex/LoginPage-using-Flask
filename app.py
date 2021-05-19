from flask import Flask, render_template,request
import pymongo
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)


def connect():
    client = pymongo.MongoClient('mongodb+srv://cana:canarocks@canary.cmhw8.mongodb.net/twitter?retryWrites=true&w=majority')  
    client = client.twitter
    client = client.users
    return client


db=connect()


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/sign' , methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        print(request.form , flush = True)
        user = {
                    
                    "name": request.form.get('name'),
                    "email": request.form.get('email'),
                    "password": request.form.get('password')
                }     
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        if db.find_one({ "email": user['email'] }):
            error='Email already exist'
            print(error)
            return  render_template('home.html' , error = error) 
        else:
            db.insert_one(user)
            return render_template('dashboard.html')
          # Encrypt the password
        
    

        # here
        

@app.route('/login' , methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        print(request.form , flush = True)
        user = {

                    "email": request.form.get('email'),
                    "password": request.form.get('password')
                }     
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        user = db.find_one({"email": request.form.get('email')})

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return render_template('dashboard.html')
        else:    
            loginerror='Invalid login credentials'
            return  render_template('home.html' , error2 = loginerror) 
        
    
    
        
    

        # here    


@app.route('/signin')
def signin():
  return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True , host='0.0.0.0')