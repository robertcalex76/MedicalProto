# CMS Data App Frontend

This is the frontend part of the CMS Data App, built using React. It provides a user interface to interact with the CMS nursing home data served by the backend API.

## Getting Started

To get started with the frontend, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd cms-data-app/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then, run the following command to install the necessary packages:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server with:
   ```bash
   npm start
   ```
   This will launch the application in your default web browser at `http://localhost:3000`.

## Project Structure

- **public/index.html**: The main HTML file for the React application.
- **src/App.js**: The main component that sets up routing and includes other components.
- **src/components/Table.js**: A component that displays a searchable table of nursing home facilities.
- **src/pages/Home.js**: The home page component that may include the table and filters for searching nursing homes.
- **src/index.js**: The entry point for the React application.

## Features

- Searchable table of nursing home facilities.
- Filters for state, rating, number of beds, and ownership type.

## API Integration

The frontend communicates with the backend API to fetch and display CMS nursing home data. Ensure the backend is running and accessible for the frontend to function correctly.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.