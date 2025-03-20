from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import sqlite3

app = Flask(__name__)
CORS(app)

# MySQL Configurations
employee_db_config = {
    'host': 'Suryansh',
    'user': 'root',
    'password': 'root',
    'database': 'employee_db'
}

# postgresql config

# projects_db_config = {
#     'host': 'localhost',
#     'user': 'postgres',
#     'password': 'guptavarun132',
#     'database': 'Emplayee_EB',
# }

# SQLite Configuration
# sqlite_db_path = './databases/sqlite/tasks.db'

# API to insert data into employees database
@app.route('/add-employee', methods=['POST'])
def add_employee():
    data = request.json
    employee_id = data['employee_id']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone = data['phone']
    department_id = data['department_id']
    job_title = data['job_title']  # Corrected this line
    salary = data['salary']
    hire_date = data['hire_date']

    try:
        connection = mysql.connector.connect(**employee_db_config)
        cursor = connection.cursor()
        query = "INSERT INTO employees (employee_id, first_name, last_name, email, phone, department_id, job_title, salary, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (employee_id, first_name, last_name, email, phone, department_id, job_title, salary, hire_date))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Employee added to employees database"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch aggregated data from all databases
@app.route('/aggregate-data', methods=['GET'])
def aggregate_data():
    try:
        # Fetch data from employees database
        employees_connection = mysql.connector.connect(**employee_db_config)
        employees_cursor = employees_connection.cursor()
        employees_cursor.execute("SELECT * FROM employees")
        employees = employees_cursor.fetchall()
        employees_cursor.close()
        employees_connection.close()

        # # Fetch data from projects database
        # projects_connection = mysql.connector.connect(**projects_db_config)
        # projects_cursor = projects_connection.cursor()
        # projects_cursor.execute("SELECT * FROM projects")
        # projects = projects_cursor.fetchall()
        # projects_cursor.close()
        # projects_connection.close()

        # # Fetch data from tasks database (SQLite)
        # sqlite_connection = sqlite3.connect(sqlite_db_path)
        # sqlite_cursor = sqlite_connection.cursor()
        # sqlite_cursor.execute("SELECT * FROM tasks")
        # tasks = sqlite_cursor.fetchall()
        # sqlite_cursor.close()
        # sqlite_connection.close()

        return jsonify({
            "employees": employees,
            # "projects": projects,
            # "tasks": tasks
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Root route for testing
@app.route('/')
def home():
    return "Welcome to the Unified Data Aggregation System!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)