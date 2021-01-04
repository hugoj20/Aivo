# Flask API Restfull Aivo Challenge
Api build in Flask with Python 3.8.5 Using a SQLite database

## Installation 

Get the code with git
```bash
git clone https://github.com/hugoj20/Aivo.git
cd Aivo
cp .env.template.txt .env
```
## Choose a method
### With Docker Compose

run the following commands

```bash
docker-compose build
```

After the image is created, run the aplication.

```bash
docker-compose up
```

### With venv
Create and activate the virtual env
```bash
python3 -m venv .env
source .env/bin/activate
```

Install the required dependecies

```bash
pip install -r requirements.txt
```

Run the aplicacion
```bash
flask run 
```

## Usage
After the aplication is ready we need to load the dataset

### Initialization
```bash
curl -X POST "http://localhost:5000/api/v1/preload_data/"
```

### API Enpoints
Return the dataset of indicators
- GET http://localhost:5000/api/v1/satisfaction/
    - Example : 
    ```bash
    curl -X GET "http://localhost:5000/api/v1/satisfaction/"
    ```

Returns countries with their index value, greater than the input value using the life satisfaction indicator 
- GET http://localhost:5000/api/v1/satisfaction/filter/<string:value>
    - Example : curl -X GET 
    ```bash
    curl -X GET  "http://localhost:5000/api/v1/satisfaction/filter/2"
    ```

Returns countries with their index value, greater than the input value specifying the indicator code  
- GET http://localhost:5000/api/v1/satisfaction/filter/<string:value>/<string:indicator>
    - Example : 
    ```bash
    curl -X GET "http://localhost:5000/api/v1/satisfaction/filter/3/CG_SENG"
    ```


Returns all the possible indicators with his respective code
- GET http://localhost:5000/api/v1/satisfaction/unique/
    - Example: 
    ```bash
    curl -X GET "http://localhost:5000/api/v1/satisfaction/unique/"
    ```

