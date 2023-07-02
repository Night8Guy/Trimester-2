-- creates the table unique_id with the following requirements:
-- id INT with the default value of 1 and unique
-- name VARCHAR(256)
CREATE TABLE unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);