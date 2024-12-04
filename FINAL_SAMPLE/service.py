# An extremely minimal microservice.

# You must have Flask installed to run this service.

from flask import Flask

# This defines the main Flask object.
app = Flask(__name__)

# This decorator tells Flask to call the function when the user visits the URL "/hello". By default it responds to GET requests.
# You can include an HTTP method as well for other verbs, like this: @app.route('/hello', methods=['POST'])
@app.route('/hello')
def hello():
    # This is the simplest way to return a response. Flask will determine the correct content-type.
    # The second return parameter is the HTTP status code. 200 means "OK"; a few other common
    # examples are 404 (Not Found), 500 (Internal Server Error), 401 (Unauthorized), and 403 (Forbidden).
    return 'Hello, World!', 200

if __name__ == '__main__':
    app.run()
