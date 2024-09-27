from flask import Flask
app=Flask(__name__)

@app.route ('/home')
def home():
    return "Hello World"

@app.route ('/about')
def about():
    return "Welcome to about page"

@app.route('/goodbye')
def goodbye():
    return "Goodbye"
app.run(debug=True)

