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
        f"\nMember ID       : {self.member_id}"
        f"\nName            : {self.name}"
        f"\nGender          : {self.gender}"
        f"\nPhone           : {self.phone}"
        f"\nEmail           : {self.email}"
        f"\nAddress         : {self.address}"
        f"\nMembership Date : {self.membership_date}"
    )
        