# Tea House API
 
A simple FastAPI application for managing a tea collection with CRUD operations.

## Features

- **Get all teas**: Retrieve the complete list of teas
- **Add tea**: Add a new tea to the collection
- **Update tea**: Update tea information by ID
- **Delete tea**: Remove a tea from the collection
- **Welcome endpoint**: A simple root endpoint

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- **GET** `/` - Welcome message
- **GET** `/teas` - Get all teas
- **POST** `/teas` - Add a new tea
- **PUT** `/teas/{tea_id}` - Update a tea by ID
- **DELETE** `/teas/{tea_id}` - Delete a tea by ID

## Tea Model

```json
{
  "id": 1,
  "name": "Green Tea",
  "origin": "China"
}
```

## Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
