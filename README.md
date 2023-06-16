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

4. Inicia el servidor backend ejecutando el siguiente comando:

 ```shell
   uvicorn main:app --reload

El servidor backend estará disponible en `http://localhost:8000`.

## Configuración del Frontend

1. Abre el archivo `frontend/src/api/index.ts` y actualiza la URL base de la API en la constante `baseURL` con la dirección del servidor backend (`http://localhost:8000` por defecto).
2. Ejecuta el siguiente comando en la terminal para instalar las dependencias del frontend:

 ```shell
   npm install

3. Inicia el servidor de desarrollo del frontend ejecutando el siguiente comando:


 ```shell
   npm run serve

   El servidor de desarrollo del frontend estará disponible en `http://localhost:8080`.

## Uso de la Aplicación

Accede a la aplicación en tu navegador en `http://localhost:8080`. Verás la lista de tareas existentes y podrás agregar nuevas tareas, eliminar tareas y actualizar tareas.