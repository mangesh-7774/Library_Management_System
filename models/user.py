class User:

  def __init__(self,user_id=None,username="",password=""):
    self.user_id = user_id
    self.username = username
    self.password = password

  def __str__(self):
    return(
      f"User ID : {self.user_id}"
      f"UserName : {self.username}"
    )

