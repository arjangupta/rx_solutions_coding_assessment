### Dependencies/setup:  
1. Download and setup [anaconda](https://www.anaconda.com/distribution/) (make sure to use Python 3 version).  
2. Execute in terminal: `conda create -n rx_assessment python=3.6`
3. Execute: `conda activate rx_assessment`  
4. Execute: `conda install flask`  
5. Execute: `conda install -c conda-forge uwsgi`  

### Running the application in development mode:
At the top level of this repository, execute: 
1. `export FLASK_APP=api.py`
2. `flask run`

### Running the application in production mode:
At the top level of this repository, execute: `uwsgi --http 127.0.0.1:5000 --module app:app`