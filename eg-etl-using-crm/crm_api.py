from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

class CRMAPI:
    def __init__(self):
        # Creates an instance of a Flask web application. This is the main app that will handle incoming requests.
        self.app = Flask(__name__)

        # Database connection configuration
        self.db_config = {
            'host': 'localhost',
            'database': 'crm_db',
            'user': 'postgres',          # Replace with your PostgreSQL username
            'password': 'postgres',      # Replace with your PostgreSQL password
            'port': 5432
        }

        # Set up all routes when the app starts
        self.setup_routes()


    def get_customers_from_db(self):
        """
        Connects to PostgreSQL and retrieves all customers from the 'customers' table.
        """
        try:
            # Establish the database connection
            connection = psycopg2.connect(**self.db_config)
            
            # Use DictCursor to get results as dictionaries (for easy JSON conversion)
            cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            # Execute SQL query to get all customer records
            cursor.execute("SELECT * FROM customers;")
            
            # Fetch all rows from the result
            customers = cursor.fetchall()
            
            # Close cursor and connection to avoid leaks
            cursor.close()
            connection.close()
            
            # Convert rows from psycopg2 objects to Python dictionaries
            return [dict(customer) for customer in customers]

        except Exception as e:
            # Log any database connection or query errors
            print(f"Database error: {e}")
            return []

    def setup_routes(self):
        """
        Define the available API routes/endpoints.
        """

        # Home route (/) that returns a simple welcome message
        @self.app.route('/', methods=['GET'])
        def home():
            return jsonify({"message": "Welcome to the CRM API!"})

        # /customers route that fetches data from the PostgreSQL database
        @self.app.route('/customers', methods=['GET'])
        def get_customers():
            customers = self.get_customers_from_db()
            
            if customers:
                # Return the customer list as JSON if data exists
                return jsonify(customers)
            else:
                # Return an error if no data is found or an error occurred
                return jsonify({"error": "No customer data found or database error occurred."}), 500

    def run(self):
        # Runs the app (in debug mode) to start the Flask web server on your local machine (usually at http://127.0.0.1:5000)
        self.app.run(debug=True)

if __name__ == '__main__':
    # Create an instance of the CRMAPI class and start the server
    crm_api = CRMAPI()
    crm_api.run()
