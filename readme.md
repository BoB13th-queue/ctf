# CTF Project

CTF Projet


## Quick Start
If you have docker compose installed
```sh
docker compose up -d
```

If only docker is installed
```sh
docker build -t ctf_back .
docker run -p 8000:8000 ctf_back
```

## requirements

if you don't have a miniconda(or anaconda), you can install it on this url.
https://docs.anaconda.com/free/miniconda/index.html

```sh
conda create -n secure_coding python=3.9
conda activate secure_coding
pip install -r requirements.txt
```

or

```sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Run


```sh
uvicorn fastapi_app:app --reload
```

or 

```sh
python fastapi_app.py
```


## Structure
```sh
CTF Projet
├── readme.md
├── main.py
├── dockerfile
├── ctf.db
├── requirements.txt
├── core
│   └── config.py
├── database
│   ├── database.py
│   └── models.py
├── service
│   ├── __init__.py
│   ├── auth
│   │   ├── crud.py
│   │   ├── route.py
│   │   └── schema.py
│   ├── note
│   │   ├── crud.py
│   │   ├── route.py
│   │   └── schema.py
│   └── user
│       ├── crud.py
│       ├── route.py
│       └── schema.py
├── tests
└── utils
    ├── oauth.py
    └── passHash.py
```

`readme.md`: It contains information about the project and how to implement it.
`main.py`: This is the file to run the project.
`dockerfile`: This is a file for running the project in a Docker environment.
`ctf.db`: This is the file where information related to the project is stored.
`requirements.txt`: A file for managing the project's dependencies.
`core`: There are files related to project settings.
`database`: There are files related to the settings of the database.
`service`: There are documents related to the service API.
    - `crud`: These are documents related to database operations.
    - `schema`: Defines the input and output format of the API.
    - `route`: There are endpoints and implementations of the API.
`tests`: These are the files for testing.
`utils`:  There are other things that are required to implement the project.