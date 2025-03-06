from flask import Flask, jsonify

class CRMAPI:
    def __init__(self):
        # Creates an instance of a Flask web application. This is the main app that will handle incoming requests.
        self.app = Flask(__name__)
        self.setup_routes()

    # Test route
    def setup_routes(self):
        # Route decorator. It says, “When someone visits the home page / using a GET request, run the following function.”
        @self.app.route('/', methods=['GET'])

        # This will run when someone visits the / route. It sends back a JSON response that says "Welcome to the CRM API!".
        def home():
            return jsonify({"message": "Welcome to the CRM API!"})

    # Runs the app (in debug mode) to start the Flask web server on your local machine (usually at http://127.0.0.1:5000)
    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    crm_api = CRMAPI()
    crm_api.run()
