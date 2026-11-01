CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(150) NOT NULL,
    price NUMERIC(12,2) NOT NULL
);

INSERT INTO books (title, author, price)
VALUES
('Dac Nhan Tam', 'Dale Carnegie', 85000),
('Nha Gia Kim', 'Paulo Coelho', 79000);
