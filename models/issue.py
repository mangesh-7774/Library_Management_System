class Issue:

    def __init__(self, issue_id, book_id, member_id,
                 issue_date, due_date, return_date, status):

        self.issue_id = issue_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status

    def __str__(self):
        return (
            f"\nIssue ID     : {self.issue_id}\n"
            f"Book ID      : {self.book_id}\n"
            f"Member ID    : {self.member_id}\n"
            f"Issue Date   : {self.issue_date}\n"
            f"Due Date     : {self.due_date}\n"
            f"Return Date  : {self.return_date}\n"
            f"Status       : {self.status}"
        )