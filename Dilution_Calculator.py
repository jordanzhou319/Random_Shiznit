import time

while True:
	initial = input('Dilution equation: C1V1=C2V2:\n \nTo find C1, input "a". \nTo find V1, input "b". \nTo find C2, input "c". \nTo find V2, input "d". \nTo quit, input "q". \n\ninput: ')
	print("\n")
	
	if initial == "a":
	  v1 = float(input("Initial volume (uL): "))
	  c2 = float(input("Final concentration (uM/%): "))
	  v2 = float(input("Final volume (uL): "))

	  volume = (c2 * v2) / v1

	  msg = "Initial concentration:" + " " + str(volume) + "uM/%"
	  
	  print("\n")
	  print(msg)
	  print("\n")	  
	  
	elif initial == "b":
	  c1 = float(input("Initial concentration (uM/%): "))
	  c2 = float(input("Final concentration (uM/%): "))
	  v2 = float(input("Final volume (uL): "))

	  volume = (c2 * v2) / c1

	  msg = "Add" + " " + str(volume) + "uL"
	  
	  print("\n")
	  print(msg)
	  print("\n")
	  
	elif initial == "c":
	  c1 = float(input("Initial concentration (uM/%): "))
	  v1 = float(input("Initial volume (uL): "))
	  v2 = float(input("Final volume (uL): "))

	  volume = (c1 * v1) / v2

	  msg = "Final concentration:" + " " + str(volume) + "uM/%"
	  
	  print("\n")
	  print(msg)
	  print("\n")
			
	elif initial == "d":
	  c1 = float(input("Initial concentration (uM/%): "))
	  v1 = float(input("Initial volume (uL): "))
	  c2 = float(input("Final concentration (uM/%): "))

	  volume = (c1 * v1) / c2

	  msg = "Final volume:" + " " + str(volume) + "uL"
	  
	  print("\n")
	  print(msg)
	  print("\n")
	  
	elif initial == "q":
		print("Goodbye")
		time.sleep(1)
		exit()
		
	else:
	  print ("only a, b, c, d, or q are acceptable inputs")
	  print("\n")
