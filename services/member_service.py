from database.connection import get_connection  # Adjust import based on your connection file function
from models.member import Member


class MemberService:

    @staticmethod
    def add_member(name, gender, phone, email, address, membership_date):
        connection = get_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO members (name, gender, phone, email, address, membership_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query, (name, gender, phone, email, address, membership_date)
        )
        connection.commit()
        cursor.close()
        connection.close()
        print("\n[SUCCESS] Member added successfully!")

    @staticmethod
    def get_all_members():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM members"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        members = []
        for row in rows:
            members.append(Member(**row))
        return members

    @staticmethod
    def get_member_by_id(member_id):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM members WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()

        if row:
            return Member(**row)
        return None

    @staticmethod
    def delete_member(member_id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM members WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"\n[SUCCESS] Member with ID {member_id} deleted successfully.")