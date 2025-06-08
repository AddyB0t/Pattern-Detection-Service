# Pattern Detection Service

A FastAPI-based service that detects various patterns in uploaded files, including PAN numbers, contact numbers, driving license numbers, and registration numbers.

## Features

- File upload and pattern detection
- RESTful API endpoints
- PostgreSQL database integration
- Pattern detection for:
  - PAN numbers
  - Contact numbers
  - Driving license numbers
  - Registration numbers

## Prerequisites

- Python 3.7+
- PostgreSQL database

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

## Running the Application

Start the server:
```bash
python main.py
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

- `GET /`: Welcome message
- `POST /api/upload`: Upload a file for pattern detection

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://127.0.0.1:8000/docs`
- ReDoc documentation: `http://127.0.0.1:8000/redoc`

## Project Structure

```
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
├── functioncaller/     # Core functionality
│   ├── Function_router.py  # API routes
│   ├── database.py     # Database configuration
│   └── model.py        # Database models
└── venv/               # Virtual environment
```

## Dependencies

- FastAPI 0.104.1
- Uvicorn 0.24.0
- Python-multipart 0.0.6
- Asyncpg 0.29.0
- Python-dotenv 1.0.0
- Psycopg2-binary 2.9.7

## License

[Add your license here]

## Contributing

[Add contribution guidelines here] 