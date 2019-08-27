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
At the top level of this repository, execute: `flask run`

### Testing the application
At the top level of this repository, execute: `python tests.py`. This will run all the unit tests for this flask app.