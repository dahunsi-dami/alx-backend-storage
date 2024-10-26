-- creates a table users with these requirements:
-- id, integer, never, null, auto increment and primary key;
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- if table already exists, this script should not fail;
-- script can be executed on any database.
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
