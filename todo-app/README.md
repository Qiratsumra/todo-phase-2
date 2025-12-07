# Full-Stack Todo Application

**This project is currently being transformed from a simple console application into a full-stack, multi-user web application.**

The new architecture will feature a **Next.js** frontend, a **Python FastAPI** backend, and a **Neon PostgreSQL** database. The development standards, architectural principles, and workflows for this new phase are defined in the [**Project Constitution**](../.specify/memory/constitution.md).

The original console application below serves as the foundational starting point for the business logic.

---

# Todo Console Application (Legacy)

This is a simple command-line interface (CLI) application for managing your daily todo tasks.

## Features

-   Add new todo items.
-   List all existing todo items.
-   Mark todo items as complete.
-   Delete todo items.
-   Search tasks by keyword.
-   Filter tasks by status, priority, or tags.
-   Sort tasks by various criteria (e.g., due date, priority).

## Intermediate & Advanced Features

-   **Persistence:** All tasks are automatically saved to `tasks.json` and loaded on startup, ensuring your todo list is preserved across application sessions.
-   **Task Recurrence:** Define tasks that repeat daily, weekly, monthly, or yearly with specified start and end dates. The application automatically generates new instances of these tasks as their recurrence dates pass.
-   **Reminders:** Set specific date and time reminders for your tasks, and the application will notify you when a reminder is due.

## Project Structure

-   `main.py`: The entry point of the application, handling command-line argument parsing and invoking the UI logic.
-   `service.py`: Contains the core business logic for managing todo items (e.g., adding, retrieving, updating, deleting).
-   `models.py`: Defines the data structures for todo items.
-   `ui.py`: Handles the user interface aspects, such as displaying todo lists and taking user input.
-   `pyproject.toml`: Project configuration and dependencies managed by `uv` (or Poetry/PDM).
-   `uv.lock`: Lock file for dependencies, ensuring reproducible builds.

## Setup and Installation

To set up and run this application, follow these steps:

1.  **Ensure you have Python 3.x and `uv` installed.** If not, you can install `uv` via `pip`:
    ```bash
    pip install uv
    ```
    Alternatively, you can install Python from [python.org](https://www.python.org/) and `uv` from its official documentation.

2.  **Install dependencies:**
    Navigate to this `todo-app` directory and install the project dependencies using `uv`:
    ```bash
    uv sync
    ```

3.  **Activate the virtual environment (optional but recommended):**
    ```bash
    # uv automatically manages environments, but if you need to activate:
    source .venv/bin/activate # On Linux/macOS
    .venv\Scripts\activate # On Windows
    ```

## Usage

Once the setup is complete, you can run the todo application from this directory:

```bash
python main.py
```

The application will then present you with options to manage your todo list.

Example commands (actual commands may vary based on implementation in `main.py`):
```bash
python main.py add "Buy groceries"
python main.py list
python main.py complete 1
python main.py delete 2
```
Please refer to the application's help message (if available) for exact command usage:
```bash
python main.py --help
```
