directions = ['up','down','left','right', 'Up','Down','Left','Right',]
commands = ["dip", "move"]
commandList = []

def parseyBoi(stringyBoi):
	# for e in stringyBoi :
		splitBoi = stringyBoi.splitlines()
		for boi in splitBoi:

			words = boi.split(" ")
			for word in words:
				parseCommand(word)
				# separate = word.split("_")
				# if (separate[0] in commands):
				# 	parseCommand(separate)

def parseCommand(command):
	global commandList
	if command == "dip" or command in directions:
		if len(commandList) == 10:
			commandList = commandList[:1]
			commandList.append(command)
		else:
			commandList.append(command)
	# elif command in commands:
	# 	# (direction, distance) = parseDistance(command[1])
	# 	# if direction != "bad":
	# 		if len(commandList) == 10:
	# 			commandList = commandList[:1]
	# 			commandList.append((direction, distance))
	# 		else:
	# 			commandList.append((direction, distance))
	else:
		print ("invalid command attempted: ", command)


# def parseDistance(movement):
# 	if len(movement) < 2:
# 		return ("bad", 0)
# 	direction = "bad"
# 	firstLetter = movement[0]
# 	rest = movement[1:]
# 	if firstLetter == 'a':
# 		angle = parseAngle(rest)
# 		if angle[0] != "bad":
# 			return ('a', angle)
# 		else:
# 			return angle
# 	elif firstLetter in directions:
# 		direction = firstLetter
# 		try:
# 			float(rest)
# 			return (direction, float(rest))
# 		except ValueError:
# 			return ("bad", 0)
# 	return ("bad", 0)

# def parseAngle(angle):
# 	if "_" in angle:
# 		values = angle.split("_")
# 		try:
# 			float(values[0])
# 			float(values[1])
# 			return (float(values[0]), float(values[1]))
# 		except ValueError:
# 			return ("bad", "bad")
# 	else:
# 		return ("bad", "bad")

def executeDip():
	print ("dip executed")
	#some sort of  code to execute the dip. Have to know how this works with the arduino/raspberry pi
	return

def executeLinearMove(direction, distance):
	print ("move executed in direction: ", direction, "with distance: ", distance)
	#Same as above
	return

def executeAngularMove(direction, distance):
	print ("move executed in direction: ", direction, "with distance: ", distance)
	#Same as above
	return

testText = """fkjdfhdfhdf j sf f u
boi what the fuck did you say to me
hfdhsdfjhsdfjh l
dip move
move:a8_9"""

def mainLoop(twitchList):
	# Checks the logs from the twitch chat, using up to ten of them
	maxRange = len(twitchList)
	if len(twitchList) > 9:
		maxRange = 10
	for x in range (0,maxRange):
		parseyBoi(twitchList[x])
	print(commandList)

	#execute the first thing on the command list

