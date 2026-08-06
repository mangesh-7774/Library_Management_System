class Member:
    def __init__(
        self,
        member_id=None,
        name=None,
        gender=None,
        phone=None,
        email=None,
        address=None,
        membership_date=None,
    ):
        self.member_id = member_id
        self.name = name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.membership_date = membership_date

    def __str__(self):
        return (
            f"ID: {self.member_id} | Name: {self.name} | Gender: {self.gender} | "
            f"Phone: {self.phone} | Email: {self.email} | Address: {self.address} | "
            f"Joined: {self.membership_date}"
        )