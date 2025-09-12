# Streamlit Todo App

A simple and intuitive web-based Todo application built with Streamlit. This app helps you manage your daily tasks, track your progress, and boost your productivity.

## Features

- **Add new todos**: Quickly add new tasks to your list.
- **Edit existing todos**: Click the "Edit" button to modify a task.
- **Delete todos**: Mark tasks as complete and remove them from your list.
- **Persistent storage**: Your todos are saved in a `todos.txt` file, so you won't lose your tasks even after closing the app.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd web_todo_app
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

To run the application, use the following command:

```bash
streamlit run web.py
```

The app will open in your default web browser.

## Project Structure

- **`web.py`**: The main Streamlit application file. It handles the user interface and event handling.
- **`functions.py`**: Contains helper functions for reading and writing todos to the `todos.txt` file.
- **`todos.txt`**: A text file where your todos are stored.
- **`site.css`**: Custom CSS for styling the application.
- **`requirements.txt`**: A list of all the Python dependencies required to run the project.

## Dependencies

The project uses the following libraries:

- altair
- attrs
- blinker
- cachetools
- certifi
- charset-normalizer
- click
- colorama
- gitdb
- GitPython
- idna
- Jinja2
- jsonschema
- jsonschema-specifications
- MarkupSafe
- narwhals
- numpy
- packaging
- pandas
- pillow
- protobuf
- pyarrow
- pydeck
- python-dateutil
- pytz
- referencing
- requests
- rpds-py
- six
- smmap
- streamlit
- tenacity
- toml
- tornado
- typing_extensions
- tzdata
- urllib3
- watchdog
