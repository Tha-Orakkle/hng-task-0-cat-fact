# TASK ZERO - HNG INTERNSHIP

A simple API service that returns simple data that contains user data 
and a random cat fact that is retreived from a third party service `https://catfact.ninja/fact`.

## Installation
* Clone the repo
```bash
git clone https://github.com/Tha-Orakkle/hng-task-0-cat-fact
cd hng-task-0-cat-fact
```
* Create and activate virtual env
```bash
python3 -m venv venv
source venv/bin/activate # Linux/MacOs
venv\bin\activate.bat # Windows
```
* Install dependencies
```bash
pip install -r requirements.txt
```
* set environmnet variables

Add the following variables to your `.env` file
```bash
SECRET_KEY='your_secret_key'
DEBUG=True
```
* Run server
```bash
python manage.py runserver
``` 

## Tests
To run tests on the program. 
```bash
pytest 
```

## Response
* 200 Response
```json
{
  "status": "success",
  "user": {
    "email": "<your email>",
    "name": "<your full name>",
    "stack": "<your backend stack>"
  },
  "timestamp": "<current UTC time in ISO 8601 format>",
  "fact": "<random cat fact from Cat Facts API>"
}
```
* 429 Response 
```json
{
    "error": "Too many requests."
}
```

## API Documentation
Visit `http://127.0.0.1/` for documentation.


## Author
username: tha_orakkle <br>
email: adegbiranayinoluwa.paul@yahoo.com


## License 
