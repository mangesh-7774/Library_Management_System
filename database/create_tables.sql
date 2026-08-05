USE library_db;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    publisher VARCHAR(100),
    total_quantity INT NOT NULL,
    available_quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender ENUM('Male','Female','Other'),
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    address VARCHAR(255),
    membership_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,

    book_id INT NOT NULL,
    member_id INT NOT NULL,

    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,

    status ENUM('Issued','Returned') DEFAULT 'Issued',

    FOREIGN KEY (book_id)
        REFERENCES books(book_id)
        ON UPDATE CASCADE,

    FOREIGN KEY (member_id)
        REFERENCES members(member_id)
        ON UPDATE CASCADE
);