class Book:
    def __init__(self, book_id, title, author, category, publisher,
                 total_quantity, available_quantity):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.publisher = publisher
        self.total_quantity = total_quantity
        self.available_quantity = available_quantity

    def __str__(self):
        return (
            f"\nBook ID            : {self.book_id}\n"
            f"Title              : {self.title}\n"
            f"Author             : {self.author}\n"
            f"Category           : {self.category}\n"
            f"Publisher          : {self.publisher}\n"
            f"Total Quantity     : {self.total_quantity}\n"
            f"Available Quantity : {self.available_quantity}"
        )