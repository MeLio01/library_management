Endpoints:

User: /api/user
- /add_user : first_name, last_name, phone_no, email_id
- /delete_user : user_id
- /update_user : user_id, ...
- /user_by_id : user_id
- /user_by_name : first_name
- /issued_books_by_user : user_id
- /get_all_users

Book: /api/book
- /add_book : book_name, author, tag, total_copies
- /delete_book : book_id
- /update_book : book_id, ...
- /book_by_id : book_id
- /book_by_name : book_name
- /get_all_books

Transaction: /api/trans
- /issue_book : user_id, book_id, issue_date
- /return_book : transaction_id
- /trans_by_id : transaction_id
- /delete_trans : transaction_id