#run the file with command line argument: "python3 matthew_hotchkiss_hw1.py"
#insert a year, and you're good


def main():
	n="-1"
	v=-1
	while v<0:
			n=input("Please insert a year to check if it's a leap year: ")
			try:
				v=int(n)
			except ValueError:
				print("That's not even a number!")
	if v%4==0:
		if v%100==0:
				if v%400==0:
						print(f"{v} is a leap year")
				else:
						print(f"{v} is not a leap year")
		else:
			print(f"{v} is a leap year")
	else:
		print(f"{v} is not a leap year")
main()
