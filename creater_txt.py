


for i in range(200):
	print("hey there", i)
	file = open("Drivers_License_" + str(i+1) + ".txt", "w")
	file.write("Last Name:\n")
	file.write("First Name:\n")
	file.write("Address:\n")
	file.write("Sex:\n")
	file.write("Height:\n")
	file.write("Weight:\n")
	file.write("Eye color:\n")
	file.write("Hair Color:\n")
	file.write("DOB:\n")
	file.write("Donor Status:")
	file.close()

	 
