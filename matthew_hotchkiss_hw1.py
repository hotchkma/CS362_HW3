#run the file with command line argument: "python3 matthew_hotchkiss_hw1.py"
#insert a year, and you're good


def main():
	n=input("Please insert a year to check if it's a leap year: ")
	n=int(n)
	if n%4==0:
		if n%100==0:
				if n%400==0:
						print(f"{n} is a leap year")
				else:
						print(f"{n} is not a leap year")
		else:
			print(f"{n} is a leap year")
	else:
		print(f"{n} is not a leap year")
main()
