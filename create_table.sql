-- script that creates tables in database
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    PRIMARY KEY (id)
):