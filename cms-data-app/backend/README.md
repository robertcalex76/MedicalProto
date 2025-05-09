# CMS Data App Backend

This document provides an overview of the backend setup for the CMS Data App, which is designed to pull, clean, and serve CMS nursing home data through a FastAPI application.

## Project Structure

The backend is organized as follows:

```
backend/
├── app/
│   ├── main.py          # Entry point for the FastAPI application
│   ├── api/             # Contains API-related code
│   │   ├── __init__.py  # Marks the directory as a package
│   │   └── endpoints.py  # Defines API endpoints for data retrieval
│   ├── db/              # Contains database-related code
│   │   ├── __init__.py  # Marks the directory as a package
│   │   └── models.py    # Defines SQLAlchemy models for the database
│   └── utils/           # Contains utility functions
│       └── data_ingestion.py  # Functions for data ingestion
├── requirements.txt      # Lists dependencies for the backend
└── README.md             # Documentation for the backend
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd cms-data-app/backend
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Ensure you have PostgreSQL installed and running.
   - Create a database for the application.
   - Run the SQL schema from `database/schema.sql` to set up the necessary tables.

5. **Run the Application**
   ```
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage

- The API endpoints can be accessed at `http://127.0.0.1:8000/api`.
- Use the endpoints defined in `app/api/endpoints.py` to retrieve and filter CMS nursing home data.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.