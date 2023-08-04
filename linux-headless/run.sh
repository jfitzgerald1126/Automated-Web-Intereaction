#!/bin/bash
export APP_USERNAME=[your_username]
export APP_PASSWORD=[your_password]
export LOGIN_URL=[your_login_url]

# your script here

# e.g. for cron job
cd /[your_path_to_app_directory]/linux-headless 
python3 main.py >> [your_logging_file]