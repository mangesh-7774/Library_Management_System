USE library_db;

INSERT INTO users (username, password)
VALUES
('admin', 'admin123');

INSERT INTO books
(title, author, category, publisher, total_quantity, available_quantity)
VALUES
('Python Programming', 'Reema Thareja', 'Programming', 'Oxford', 10, 10),

('Java: The Complete Reference', 'Herbert Schildt', 'Programming', 'McGraw Hill', 8, 8),

('Database System Concepts', 'Abraham Silberschatz', 'Database', 'McGraw Hill', 6, 6),

('Operating System Concepts', 'Abraham Silberschatz', 'Operating System', 'Wiley', 5, 5),

('Computer Networks', 'Andrew S. Tanenbaum', 'Networking', 'Pearson', 7, 7);


INSERT INTO members
(name, gender, phone, email, address, membership_date)
VALUES
('Mangesh Bhalerao', 'Male', '1111111111',
'bhaleraom737@gmail.com',
'Nanded, Maharashtra',
CURRENT_DATE),

('Rahul Patil', 'Male', '2222222222',
'rahul@gmail.com',
'Pune, Maharashtra',
CURRENT_DATE),

('Yogesh Sharma', 'Female', '3333333333',
'priya@gmail.com',
'Mumbai, Maharashtra',
CURRENT_DATE);

INSERT INTO issued_books
(book_id, member_id, issue_date, due_date, return_date, status)
VALUES
(
1,
1,
CURRENT_DATE,
DATE_ADD(CURRENT_DATE, INTERVAL 15 DAY),
NULL,
'Issued'
);