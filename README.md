# TodoApp

TodoApp is a simple web application for managing a task list. It allows users to add, delete, and update tasks.

## Technologies Used

- Frontend: Vue.js v3 with Composition API.
- Backend: FastAPI (Python) with PostgreSQL as the database.

## Prerequisites

Before getting started, make sure you have the following requirements installed:

- Node.js: [https://nodejs.org](https://nodejs.org)
- Python: [https://www.python.org](https://www.python.org)
- PostgreSQL: [https://www.postgresql.org](https://www.postgresql.org)

## Backend Setup

1. Create a database in PostgreSQL for the application. You can use the `pgAdmin` tool or any other PostgreSQL administration interface.
2. Open the `backend/main.py` file and update the database connection details in the `db_connection` variable.
3. Run the following command in the terminal to install the backend dependencies:

   ```shell
   pip install -r backend/requirements.txt

4. Start the backend server by executing the following command:

   ```shell
   uvicorn main:app --reload

The backend server will be available at `http://localhost:8000`.

## Frontend configuration

1. Open the file `frontend/src/api/index.ts` and updates the API base URL in the `baseURL` constant with the address of the backend server (`http://localhost:8080` por defecto).
2. Run the following command in the terminal to install the frontend dependencies:

   ```shell
   npm install

3. Start the frontend development server by executing the following command:

   ```shell
   npm run serve

The frontend development server will be available at `http://localhost:8080`.

## Use of the Application

Access the application in your browser at `http://localhost:8080`. You will see the list of existing tasks and will be able to add new tasks, delete tasks and update tasks.
