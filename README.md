# Leadsbot - Local Setup and Execution Guide

## Overview

This document outlines the steps required to set up and run the Leadsbot application locally. Leadsbot is a Flask-based web application that interacts with the OpenAI API to provide a chatbot interface for a home goods website. It also stores lead information (emails and conversations) in a local SQLite database.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python 3.8+:** You can check your Python version by running `python --version` or `python3 --version` in your terminal. If you don't have it, download it from https://www.python.org/downloads/.
2.  **pip:** Python's package installer. It usually comes bundled with Python. Verify with `pip --version` or `pip3 --version`.
3.  **Virtual Environment (Recommended):** Using a virtual environment isolates project dependencies.
    - If you don't have `venv` installed, run: `python -m pip install --user virtualenv`
4.  **OpenAI API Key:** You'll need an OpenAI API key to use the chatbot functionality. Get one from https://platform.openai.com/account/api-keys.

## Setup Steps

**Extract the archive and open the folder in VScode or your code editor of choice then follow steps below**

1.  **Create a Virtual Environment:**

    - Navigate to the `Leadsbot` directory in your terminal.
    - Create a virtual environment:

      ```bash
      python3 -m venv venv
      ```

    - Activate the virtual environment:

      - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

      - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - You should see `(venv)` at the beginning of your terminal prompt, indicating the environment is active.

2.  **Install Dependencies:**

    - Install the required Python packages:

      ```bash
      pip install Flask Flask-SQLAlchemy python-dotenv openai flask-cors
      ```

3.  **Create a `.env` File:**

    - In the `Leadsbot` directory, create a file named `.env`.
    - Add your OpenAI API key to this file:

      ```
      OPENAI_API_KEY=your_actual_openai_api_key_here
      ```

      - **Important:** Replace `your_actual_openai_api_key_here` with your actual API key.
      - **Security:** Do not commit the `.env` file to version control (e.g., Git). It contains sensitive information.

## Running the Application

1.  **Navigate to the Project Directory:**

    - Ensure you're in the `Leadsbot` directory in your terminal and that your virtual environment is activated.

2.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

3.  **Access the Application:**
    - Open your web browser and go to `http://127.0.0.1:5000/`. (Note the URI in your terminal it may be different)
    - You should see the Leadsbot chat interface.

## Stopping the Application

- In your terminal, press `Ctrl+C` to stop the Flask development server.

## Troubleshooting

- **`ModuleNotFoundError`:** If you get an error like `ModuleNotFoundError: No module named 'flask'`, make sure your virtual environment is activated and that you installed the dependencies using `pip install ...` _while_ the environment was active.
- **`openai.APIConnectionError` or `openai.AuthenticationError`:** Double-check that you've correctly set your OpenAI API key in the `.env` file and that the key is valid.
- **`500 Internal Server Error`:** Check the terminal output for any error messages. These will often provide clues about what went wrong.
- **CORS error:** If you get a CORS error, make sure that the `CORS(app)` line is present in the `app.py` file.
- **Chatbot not responding:** If the chatbot is not responding, make sure that you have internet connection and that the API key is valid.

## Key Files and Folders

- **`app.py`:** The main Python file containing the Flask application code.
- **`.env`:** Stores the OpenAI API key (keep this file private).
- **`venv/`:** The virtual environment directory (created by `python3 -m venv venv`).
- **`leads.db`:** The SQLite database file (created automatically when the app runs).
- **`templates/index.html`:** The html file that contains the frontend code.

## Database

- The application uses a SQLite database (`leads.db`) to store lead information.
- The database is created automatically when the application runs for the first time.
- You can use a SQLite browser (like DB Browser for SQLite) to view the contents of the database. I just use the SQLite viewer extension in VScode. I didn't really build out the function for the email capture to do a regex and store properly but if you browse the DB you'll see the tables are set up correctly, just need to refactor that function.

## Deactivating the Virtual Environment

- When you're finished working on the project, deactivate the virtual environment:

  ```bash
  deactivate
  ```
