# TEAM 5 
# JOSHUA WYATT, BENJAMIN RHEE, NATHAN BIAGIONI, ALLEN CARTER, AND JAKE FARLEY
#
# Account class serves as foundation for accounts on the system. 

class Account:

	# Variables
	username 
	password
	loggedInStatus
	numGroups : int
	groupNames : Array[]
	isAdmin : boolean

	# Constructor
	def Account(self):
		user = self.getUsername()
		password = self.getPassword()
		

	
	# Returns String representing the username connected to the account 
	# @return String representing a username
	def getUserName():
		return self.username
		

	# Used in the account creation process only
	# Sets the username of the account 
	def setUserName(userN):
		self.username = userN
		
	# Checks uniqueness of username against Account database
	def checkUserName(): 
		
	# Returns String representing the password connected to the account
	# Only used when checking for login
	# @return String representing password
	def getPassword():
		return self.password
		
	# Sets a new password for the account
	def setPassword(passW):
		self.password = passW
		
	# Logs the user into the account
	# May be wiser to put this in Player class
	def login(userN, passW):


	def displayGroup():

	# Method used to create a group entity. Requires isAdmin to be false
	def createGroup(String gName):
		if self.checkIfAdmin() = false:
			# Create the group.
		# else:
			# Throw error

	# Verifies that Account is not already an Administrator of a group
	def checkIfAdmin():
		if isAdmin = true:
			return true
		else: 
			return false

	# Sends an join request attached 
	def requestToJoin(String gName):