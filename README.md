# cloudprojects
# SQL Server Database Connection Demo

This repository demonstrates how to connect to an SQL Server database using the `pypyodbc` library, fetch data, and display it in a pandas DataFrame.

# Project Setup Instructions

## Dependencies
- **pypyodbc**: Used to connect to the SQL Server.
- **pandas**: Used for data manipulation and presentation.

## Setup Steps

### 1. Clone the repository
Using Git:

```bash
git clone https://github.com/yourusername/repository-name.git
```
### 2. Create a virtual environment (optional but recommended)
Run this in Windows:
```python -m venv myenv
myenv\Scripts\activate
```
### 3. Install dependencies
Once the virtual environment is activated, install the required dependencies from the requirements.txt file:
```pip install -r requirements.txt```

### 4. Configure your credentials
The script requires your SQL Server database username and password. Open the credentials.py file and add your credentials:
```python
credentials.py
username = 'your_username'
password = 'your_password'
```
Replace 'your_username' and 'your_password' with your actual SQL Server credentials.

### 5. Run the demo script
Run the demo script to connect to the SQL Server database and retrieve data:
```python demo.py
```
The script will execute a query to retrieve the ProductId and Name columns from the SalesLT.Product table and display the result in a pandas DataFrame.