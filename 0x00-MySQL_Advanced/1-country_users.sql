-- Creates a new table user
CREATE TABLE IF NOT EXISTS users (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
	country ENUM('US', 'CO', 'TN')
);
