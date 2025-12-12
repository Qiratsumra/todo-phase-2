# Quickstart: Full-Stack Todo Application

This guide provides the essential steps to set up and run the Full-Stack Todo Application locally for development.

## Prerequisites

- **Docker and Docker Compose**: Ensure you have Docker Desktop (or Docker Engine and Docker Compose CLI) installed and running on your system.
- **Git**: For cloning the repository.
- **Web Browser**: A modern web browser like Chrome, Firefox, or Edge.

## Local Setup and Execution

### 1. Clone the Repository

If you haven't already, clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Configure Environment Variables

The application uses environment variables for configuration. The backend service requires a `.env` file.

1.  Navigate to the `backend/` directory.
2.  Create a file named `.env`.
3.  Add the following required variables. For local development, you can use the example values provided.

    ```env
    # backend/.env

    # Application settings
    PROJECT_NAME="Todo App"
    API_V1_STR="/v1"

    # Security settings
    # Generate a strong secret key. You can use: openssl rand -hex 32
    SECRET_KEY=your-super-strong-32-character-secret-key
    ACCESS_TOKEN_EXPIRE_MINUTES=15
    REFRESH_TOKEN_EXPIRE_DAYS=7

    # Database settings (for connecting to the Dockerized PostgreSQL)
    DATABASE_URL="postgresql+asyncpg://postgres:mysecretpassword@db:5432/app"

    # CORS settings (for allowing the Next.js frontend in development)
    # The Next.js app will run on port 3000
    BACKEND_CORS_ORIGINS='["http://localhost:3000"]'
    ```

### 3. Build and Run with Docker Compose

The entire stack (backend, frontend, database) is orchestrated using Docker Compose.

1.  From the **root of the project directory**, run the following command to build the images and start the services in detached mode:

    ```bash
    docker-compose up --build -d
    ```

2.  **Wait for the services to start.** The initial build may take a few minutes. You can view the logs for all services to monitor their status:
    ```bash
    docker-compose logs -f
    ```
    Look for confirmation that the database is ready and the web servers (FastAPI and Next.js) have started.

### 4. Run Database Migrations

Once the database container is running, you need to apply the database schema.

1.  Open a new terminal window.
2.  Execute a command inside the running backend container to run Alembic migrations:

    ```bash
    docker-compose exec backend alembic upgrade head
    ```
    You should see output indicating that the `users` and `tasks` tables have been created.

### 5. Access the Application

- **Frontend Application**: Open your web browser and navigate to `http://localhost:3000`. You should see the login/register page of the todo application.
- **Backend API Documentation**: The auto-generated OpenAPI (Swagger) documentation is available at `http://localhost:8000/docs`.

## Development Workflow

- **Making Backend Changes**: If you modify the Python code in the `backend/` directory, the `uvicorn` server in the Docker container will automatically reload the application thanks to the volume mount.
- **Making Frontend Changes**: If you modify the code in the `frontend/` directory, the Next.js development server will automatically hot-reload the changes in your browser.
- **Stopping the Application**: To stop all running services, run the following command from the project root:
  ```bash
  docker-compose down
  ```
