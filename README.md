# Assignment lap 3

## Installation & Usage

### Installation

- Clone or download the repo.
- Open terminal and navigate to folder.
- pipenv shell
- pipenv install

### Usage

- Run pipenv run dev to launch app on local host 5000.

## Changelog

### app.py
* Added db
* Installed shortuuid for generating short urls by using a pattern of url-safe characters
* Generated a secret key using python -c "import os; print(os.urandom(24).hex())" in order to save a session.
* Added url model
* Add parameters for finding the url and shortening it
* Add error handling

### form.py
* Add form details with validators

## Bugs
