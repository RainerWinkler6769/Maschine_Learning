CREATE TABLE IF NOT EXISTS hello_log (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message VARCHAR(255) NOT NULL
);

INSERT INTO hello_log (message) VALUES ('Hallo Welt aus MySQL');
