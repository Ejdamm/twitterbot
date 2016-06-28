from user import User
class Users(object):
	users = []
	def __init__(self):
		self.readFromFile("users.txt")
	
	def readFromFile(self, filename):
		with open(filename, "r") as my_file:
  	  		fileContent = my_file.readlines()
  	  		for name, lastID in zip(fileContent[0::2], fileContent[1::2]):
   				self.users.append(User(name.rstrip('\n'), int(lastID.rstrip('\n'))))
  	  		
	def writeToFile(self, filename):
		with open(filename, "w") as my_file:
			for user in self.users:
				my_file.write(user.name + "\n")
				my_file.write(str(user.lastID) + "\n")
				
	def addUser(self, name):
		self.users.append(User(name, 1))
