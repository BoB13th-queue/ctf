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
├── core
│   └── oauthConfig.py
├── crud
│   ├── Auth.py
│   ├── Menu.py
│   ├── Order.py
│   ├── Users.py
│   └── __pycache__
│       └── Auth.cpython-312.pyc
├── database
│   ├── __pycache__
│   │   ├── database.cpython-312.pyc
│   │   └── models.cpython-312.pyc
│   ├── database.py
│   └── models.py
├── main.py
├── readme.md
├── routes
│   ├── Auth.py
│   ├── Menu.py
│   ├── Order.py
│   ├── Users.py
│   └── __init__.py
├── schema
│   ├── Auth.py
│   ├── Menu.py
│   ├── Normally.py
│   ├── Order.py
│   └── User.py
└── utils
    ├── oauth.py
    └── passHash.py
```