2025.02.12

***Project Title: Example - ETL Using CRM Data***<br>

# Project overview:

#### Extract customer data from CRM:
- transform it by cleaning and aggregating
- load it into a data warehouse for reporting
#### Scenario
A company uses HubSpot CRM to manage customer interactions. They want to analyze:

- Total sales per customer
- Customer retention rates
- Geographical distribution of customers
-------------------------
### 0. Create a basic CRM System - Using FLask and PostgreSQL
(**CRM** - Customer Relationship Management)

1. **Design the Database Schema** for storing customers' data<br> Options to store and manage data:
    - **Temporary** in-memory storage (python list/dictionary)<br>
      --> if you just want to test the API without storing data
    - **Permanently** storing customer data in a database<br>
      (PostgreSQL, SQLite, MySQL)
2. **Build the backend API** to add, update and retrieve data<br> - **Flask**
3. **Enable Data Extraction** via API or csv export

(Possible future improvement: Creating a Web UI to interact with the CRM)

### 1. Extract - Get Data from CRM
**OLTP** (Online Transaction Processing) system defines the source in most ETL workflows. **CRMs** are an example for OLTP.


CRMs provide data mostly through APIs or Database Connections.

### 2. Transform - Clean and Aggregate Data
- Remove inactive customers
- Convert sales into yearly totals
- Aggregate sales by country

### 3. Load - Store Data in a Data Warehouse
**OLAP** (Online Analytical Processing) system defines the destination in most ETL workflows.


Loading the cleaned data into an OLAP.

-------------------------

## Setup Instructions

Follow these steps to set up and run the CRM API locally on your machine.

### 1. Prerequisites
Make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Flask
- Pandas
- Requests
- (Optional) [Git](https://git-scm.com/) if you want to clone the repository

### 2. Install project dependencies:
After cloning the project, install all required Python packages with:

```bash<br>pip install -r requirements.txt

## Available Endpoints

- `/`  
  Returns a welcome message.

- `/customers`  
  Returns sample customer data in JSON format.

## How to use:

### 1. Run the app:

```bash<br>python crm_api.py