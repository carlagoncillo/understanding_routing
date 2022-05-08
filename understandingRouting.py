from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# /success route returns string "Success!" on our website
@app.route('/dojo')
def dojo():
    return "Dojo!"

# use angeled brackets to add variables to your routes
@app.route('/say/<name>')
def say(name):
    return f"Hi, {str.capitalize(name)}!" # .capitalize is just to make string nice

# you can have more than one variable in your routes
@app.route('/repeat/<num>/<string>')
def repeat_hello(string, num):
    return f"Hello, {str.capitalize(string)}! "*int(num) # .capitalize is just to make string nice

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
