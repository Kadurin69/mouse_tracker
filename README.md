# mouse_tracker

## Installation
1. Clone repository.
2. `cd` into it.
3. Make sure you have python venv installed and run `python3 -m venv venv`, to setup your virtual environment.
4. To start your virtual environment you can run `source venv/bin/activate`. 
5. The *requirements.txt* file contains the required dependencies to run the django app. Running `pip install -r requirements.txt` will install the packages.
6. After installing the required packages you can run `python3 manage.py migrate` to apply all migrations.
7. To start the server run `daphne -b 0.0.0.0 -p 8000 tracker.asgi:application`, and in your browser enter 127.0.0.1:8000.

*Sidenote: If you want to at any point deactivate the environment, you can run `deactivate` in the terminal.
