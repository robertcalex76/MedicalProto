# CMS Data App

## Project Overview
The CMS Data App is a web application designed to provide access to CMS nursing home data. It allows users to search, filter, and view information about nursing home facilities across the United States.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React
- **Data Processing**: Python (pandas, requests)

## Project Structure
```
cms-data-app
├── backend
│   ├── app
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   ├── api
│   │   │   ├── __init__.py  # API package initialization
│   │   │   └── endpoints.py  # API endpoints for CMS data
│   │   ├── db
│   │   │   ├── __init__.py  # Database package initialization
│   │   │   └── models.py     # SQLAlchemy models for the database
│   │   └── utils
│   │       └── data_ingestion.py  # Functions for data ingestion
│   ├── requirements.txt      # Python dependencies for the backend
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the React app
│   ├── src
│   │   ├── App.js            # Main component of the React app
│   │   ├── components
│   │   │   └── Table.js      # Component for displaying a searchable table
│   │   ├── pages
│   │   │   └── Home.js       # Home page component
│   │   └── index.js          # Entry point for the React app
│   ├── package.json          # Dependencies and scripts for the frontend
│   └── README.md             # Documentation for the frontend
├── database
│   └── schema.sql            # SQL schema for the PostgreSQL database
└── README.md                 # Overall documentation for the project
```

## Getting Started

### Prerequisites
- Python 3.7+
- Node.js and npm
- PostgreSQL

### Installation

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd cms-data-app
   ```

2. **Set up the backend**
   - Navigate to the `backend` directory:
     ```
     cd backend
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Set up the frontend**
   - Navigate to the `frontend` directory:
     ```
     cd frontend
     ```
   - Install the required Node packages:
     ```
     npm install
     ```

4. **Set up the database**
   - Create a PostgreSQL database and run the schema:
     ```
     psql -U <username> -d <database_name> -f ../database/schema.sql
     ```

### Running the Application

1. **Start the backend**
   - In the `backend` directory, run:
     ```
     uvicorn app.main:app --reload
     ```

2. **Start the frontend**
   - In the `frontend` directory, run:
     ```
     npm start
     ```

### Usage
- Access the frontend at `http://localhost:3000`
- The backend API will be available at `http://localhost:8000`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.