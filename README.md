# Aphrodite FsatAPI Scaffold

[English](README.md) | [简体中文](README-zh.md)

Aphrodite is a template project based on [Fastapi-skeleton](https://github.com/kaxiluo/fastapi-skeleton) to help developers get started quickly and gain a deep understanding of the framework's usage process. The project provides comprehensive sample code and configuration, covering common development scenarios for easy learning and practice. In addition, Aphrodite also includes container deployment templates, making the project easy to deploy and manage in a modern cloud environment, helping developers to efficiently build and release applications.

## Tech Stack

| Technology                                             | Description                                                                                                 |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [APScheduler](https://github.com/agronholm/APScheduer) | Scheduled task scheduling framework in Python, supporting background job scheduling                         |
| [FastAPI](https://fastapi.tiangolo.com/)               | High-performance web framework, supporting asynchronous operations and fast API construction                |
| [JOSE](https://github.com/python-jose/jose)            | Python library for processing JSON Web Tokens (JWT)                                                         |
| [Loguru](https://github.com/Delgan/loguru)             | Simplified Python logging library, providing easy-to-use logging and formatting support                     |
| [Peewee](http://docs.peewee-orm.com/en/latest/)        | Concise Python ORM framework, supporting multiple database operations                                       |
| [Starlette](https://www.starlette.io/)                 | A high-performance framework for building web applications, the core part of FastAPI                        |
| [Uvicorn](https://www.uvicorn.org/)                    | A high-performance ASGI server that supports running asynchronous Python applications                       |
| [psycopg2](https://github.com/psycopg/psycopg2)        | A PostgreSQL database adapter that supports Python and PostgreSQL connections                               |
| [Passlib](https://passlib.readthedocs.io/en/stable/)   | A password encryption library that supports multiple hash algorithms and encryption methods                 |
| [Pydantic](https://pydantic-docs.helpmanual.io/)       | A data validation and parsing library that performs validation and parsing based on Python type annotations |
| [Python-JOSE](https://github.com/mpdavis/python-jose)  | A library for generating and parsing JSON Web Tokens (JWT) that supports encryption                         |
| [Redis-py](https://github.com/andymccurdy/redis-py)    | Python client library for connecting and operating Redis databases                                          |

## Features

- **User authentication and authorization**: Provides basic user login and permission authorization functions.

- **Distributed lock**: Distributed lock based on Redis to ensure resource security in a distributed environment.

- **Middleware support**: Built-in commonly used middleware, including authentication, request logs, cross-domain processing, etc.

- **Unified output format**: Provides a simple and easy-to-use API Result unified output method, standardizes the API response format, and improves interface consistency.

- **API modular design**: Supports modular API design, which is easy to expand and maintain.

- **Swagger document integration**: Automatically generates API documents for front-end development and testing.

## Structure

```
.
├── app/ # Application core code
├── bin/ # Executable script
├── bootsrap/ # Bootstrap file
├── database/ # Database related
├── deploy/ # Deployment related files
├── docs/ # Project documentation
├── routes/ # Routing files
├── storage/ # File storage
├── tests/ # Test files
└── README.md # Project description
```

## Run Local

```bash
# 1. Clone the project code base
git clone https://github.com/lniche/aphrodite-py.git
cd aphrodite-py

# 2. Configuration file
cd config
mv .env.example .env

# 3. Add dependencies
# Make sure you have installed the python environment, it is recommended to use conda
pip install -r requirements.txt

# 4. Initialize the database
database/init.sql

# 5. Start the service
uvicorn main:app
```

## Repo Activity

![Alt](https://repobeats.axiom.co/api/embed/57c3b523ffb088038484a6b3883890a2615b3fa5.svg "Repobeats analytics image")

## Contribution

If you have any suggestions or ideas, please create an Issue or submit a Pull Request directly.

1. Fork this repository.
2. Create a new branch: git checkout -b feature/your-feature
3. Commit your changes: git commit -m 'Add new feature'
4. Push to your branch: git push origin feature/your-feature
5. Submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

Special thanks to all contributors and supporters, your help is essential to us!
