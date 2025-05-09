CREATE TABLE nursing_homes (
    id SERIAL PRIMARY KEY,
    provider_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    rating DECIMAL(2, 1),
    staffing INT,
    violations INT,
    ownership_type VARCHAR(100)
);