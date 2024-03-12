class Usuario:
  def __init__(self, username, password):
      self.username = username
      self.password = password
user = Usuario("ainara", "asdfg")
print (user.username, user.password)
