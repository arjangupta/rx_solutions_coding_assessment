## Rx Savings Solutions Backend Developer Code Challenge

### Dependencies/setup:  
1. Download and setup [anaconda](https://www.anaconda.com/distribution/) (make sure to use Python 3 version)  
2. Execute in terminal: `conda create -n rx_assessment python=3.6`
3. Execute: `conda activate rx_assessment`  
4. Execute: `conda install flask`  
5. Execute: `conda install -c conda-forge flask-testing flask-sqlalchemy flask-migrate geopy`  
6. Execute: `export FLASK_APP=api.py` (for Windows CMD: `set FLASK_APP=api.py`, for Windows PowerShell: `$env:FLASK_APP = "api.py"`)

### Database setup
1. Apply migration changes to the database using: `flask db upgrade`
2. Populate the table of pharmacies by running the script: `python populate_table_contents.py`  

### Running the application in development mode:
1. At the top level of this repository, execute: `flask run`
2. Only an HTTP POST request can be used to successfully hit the `/api` endpoint of this app. Within this request, the user must send a valid JSON string with the keys "user_latitude" and "user_longitude". If the location is valid, the server will reply with a JSON response packet containing the keys "pharmacy_name", "address", and "distance". For example, you can use a curl command as follows: `curl localhost:5000/api -d '{"user_latitude":39.333, "user_longitude":-94.55}' -H 'Content-Type: application/json' > result.txt`. This outputs the response packet to result.txt in your local directory.

### Testing the application
At the top level of this repository, execute: `python tests.py`. This will run all the unit tests for this flask app.