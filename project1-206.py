# test!

import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import collections


def getData(file):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()

	#empty list for dictionary objects
	dictList = []

	#loop through lines and create dictionary objects
	for line in lines:
		dictObject = {}

		#split at ',' and get values
		values = line.split(",")
		# using a single trailing underscore so as
		# not to run into complications using 'class'
		first_ = values[0]
		last_ = values[1]
		email_ = values[2]
		class_ = values[3]
		removeNewLines = values[4].split("\n")
		dob_ = removeNewLines[0]

		dictObject["First"] = first_
		dictObject["Last"] = last_
		dictObject["Email"] = email_
		dictObject["Class"] = class_
		dictObject["DOB"] = dob_
		dictList.append(dictObject)

	dictList.pop(0)
	print(dictList)
	return dictList

def mySort(data,col):
	sortedList = sorted(data, key=lambda k: k[col])
	toReturn = sortedList[0].get("First") + " " + sortedList[0].get("Last")
	return toReturn


def classSizes(data):
	i = 0
	seniors = 0
	juniors = 0
	sophomores = 0
	freshmen = 0
	while i < len(data):
		if data[i].get("Class") == 'Senior':
			seniors = seniors + 1
		elif data[i].get("Class") == 'Junior':
			juniors = juniors + 1
		elif data[i].get("Class") == 'Sophomore':
			sophomores = sophomores + 1
		elif data[i].get("Class") == 'Freshman':
			freshmen = freshmen + 1
		i = i + 1
	seniorTuple = ('Senior', seniors)
	list = []
	list.append(seniorTuple)
	juniorTuple = ('Junior', juniors)
	list.append(juniorTuple)
	sophomoreTuple = ('Sophomore', sophomores)
	list.append(sophomoreTuple)
	freshmenTuple = ('Freshman', freshmen)
	list.append(freshmenTuple)

	sortedList = sorted(list, key=lambda k: k[1], reverse=True)
	return sortedList

def findMonth(a):
	list = []
	i = 0
	while i < len(a):
		dateComponents = (a[i].get('DOB')).split("/")
		month = dateComponents[0]
		list.append(month)
		i = i + 1
	count = collections.Counter(list)
	return int(count.most_common(1)[0][0])

def mySortPrint(a,col,fileName):
	inFile = open(fileName, "w")
	sortedList = sorted(a, key=lambda k: k[col])
	i = 0
	while i < len(sortedList):
		toWrite = sortedList[i].get("First") + "," + sortedList[i].get("Last") + "," + sortedList[i].get("Email") + "\n"
		inFile.write(toWrite)
		i = i + 1
	inFile.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
