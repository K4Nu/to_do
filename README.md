# Task Maker App

## Description
![logo image](https://github.com/K4Nu/to_do_app/blob/main/to_do/static/images/logo.png)
Task Maker is a dynamic task management application designed to help individuals organize their projects and daily activities with deadlines efficiently.

## Features
- **Create Tasks**: Users can easily add new tasks specifying titles and detailed descriptions to manage daily activities.
- **Task Management**: Edit or delete tasks as needed. Users can modify task details, showing flexibility in task management.
- **Set Deadlines**: Users can set deadlines for tasks to ensure timely completion.
- **User Authentication**: Secure login and registration system to manage access to the user's tasks and settings.
- **Responsive Design**: A user-friendly interface that is responsive and accessible on various devices, utilizing HTML, CSS, and Bootstrap.

## Technologies Used
- **Django**
- **SQLite**
- **HTML, CSS, and Bootstrap**

## Progress
- ✅ **Register with email verification and upload profile images** 
- ✅ **Login users with verified login only** 
- ✅ **Create tasks and manage them** 
- 🔲 ****Change ORM database to PostgreSQL****
- 🔲 **AI-generated profile images based on user prompts** 
- 🔲 **AI prompt assistant to help organize tasks** 
- 🔲 **Email notifications about task deadlines** 
- 🔲 **Website deployment** 

## Installation

### Step 1: Clone the Repository
To get started with the Task Maker app, you'll first need to clone the repository to your local machine. You can do this by running the following command in your terminal:
```bash
git clone https://github.com/K4Nu/to_do_app.git
```

### Step 2: Set Up the Development Environment
After cloning the repository, switch to the directory containing the project:
```bash
cd to_do
```

### Step 3: Install dependencies
Ensure that all dependencies needed for the app are installed by running the following command in the project directory:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up a Virtual Environment
It is recommended to use a virtual environment for Python projects. This keeps your dependencies organized and separate from other projects. To create a virtual environment in the project directory, run:
```bash
python -m venv env
```
Activate the virtual environment:
**On Windows:**
```bash
env\Scripts\activate
```

**On MacOS and Linux:**
```bash
source env/bin/activate
```

###Step 5: Configure Environment Variables
Before running the application, you'll need to set up the necessary environment variables. Create a `.env` file in the root directory of the project. This file will store sensitive information such as database credentials, secret keys, and third-party API keys, keeping them secure and separate from the main codebase.
Here is an example of what the contents of the `.env` file might look like:
```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True
EMAIL_HOST_USER=email_here
EMAIL_HOST_PASSWORD=password or app password here
```

###Step 6: Run the Test Server
Now you can start the Django server by running:
```bash
python manage.py runserver
```