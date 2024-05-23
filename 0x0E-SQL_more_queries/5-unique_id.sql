-- creates the table unique_id on your MySQL server.
-- constraints (id(INT) def = 1) (name(VARCHAR(256))
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
