[1]: https://www.python.org/
[2]: https://fastapi.tiangolo.com/

## How was it made?

This is a [Python][1] project created manually.

## Why was it made?

The objective of this repository is to learn and practice [FastAPI][2] and some of its features.

## Getting Started

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run the development server:

```bash
python -m uvicorn main:app --reload
```

### See the result

Open [http://localhost:8000/docs](http://localhost:8000/docs) with your browser to interact with the API.

Besides the auto-generated documentation, the API can be used through the _requests_ folder. You'll only need to install the **REST Client** extension at your IDE.

### How does it work?

The application consists of a **CRUD** of _ToDo_ list.

It uses **OAuth2** (authentication and authorization), **Hashing** (to work with passwords) and **JWT** (Json Web Tokens).

At the "_utils/db.py_" file there are two users already. Their password is _123456_.

You must create a `.env` file on the root directory with the following variables:

- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES

_SECRET_KEY_ can be generated through the command:

```bash
openssl rand -base64 32
```

For the _ALGORITHM_, you can use **HS256**.

And for _ACCESS_TOKEN_EXPIRE_MINUTES_, you can choose any integer between 5 and 15, for this is the interval suggested for an **Access Token**.
