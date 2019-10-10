import sftp


def readCredentials():
	with open("credentials.txt", "r") as f:
		for count, line in enumerate(f):
			# print("Line {}: {}".format(count, line))
			newLine = line.split(",")
			# print(newLine)
			host = newLine[0]
			username = newLine[1]
			password = newLine[2].rstrip()
			sftp.upload(host,username,password)


