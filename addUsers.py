from users import Users

userlist = Users()

with open("riders.txt", "r") as my_file:
  	  fileContent = my_file.readlines()
  	  		
for name in fileContent:  	  		
	userlist.addUser(name.rstrip('\n'))

userlist.writeToFile("users.txt")
