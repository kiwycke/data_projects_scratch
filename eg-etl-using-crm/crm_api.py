from flask import Flask, jsonify

class CRMAPI:
    def __init__(self):
        # Creates an instance of a Flask web application. This is the main app that will handle incoming requests.
        self.app = Flask(__name__)
        self.customers = self.load_customers()
        self.setup_routes()

    def load_customers(self):
        """
        Sample customer data simulating what might come from a real CRM system.
        This data is returned by the /customers endpoint.
        """
        return [
            {
                "Customer_ID": 101,
                "Name": "Alice",
                "Country": "USA",
                "Sales": 5000,
                "Last_Purchase_Date": "2024-01-10",
                "Status": "Active"
            },
            {
                "Customer_ID": 102,
                "Name": "Bob",
                "Country": "UK",
                "Sales": 3000,
                "Last_Purchase_Date": "2023-12-15",
                "Status": "Inactive"
            },
            {
                "Customer_ID": 103,
                "Name": "Charlie",
                "Country": "USA",
                "Sales": 7000,
                "Last_Purchase_Date": "2024-02-01",
                "Status": "Active"
            }
        ]

    def setup_routes(self):
        """
        Define the available API routes/endpoints.
        """

        # Home route (/) that returns a simple welcome message
        @self.app.route('/', methods=['GET'])
        def home():
            return jsonify({"message": "Welcome to the CRM API!"})

        # /customers route that returns the sample customer data as JSON
        @self.app.route('/customers', methods=['GET'])
        def get_customers():
            return jsonify(self.customers)

    def run(self):
        # Runs the app (in debug mode) to start the Flask web server on your local machine (usually at http://127.0.0.1:5000)
        self.app.run(debug=True)

if __name__ == '__main__':
    # Create an instance of the CRMAPI class and start the server
    crm_api = CRMAPI()
    crm_api.run()
