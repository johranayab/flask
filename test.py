# Import the Flask class from the flask module
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and bind it to a function
@app.route('/')
def home():
    return "Hello, Flask! This is your first route. i am johra "

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
