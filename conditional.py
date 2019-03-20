age = 22
citizen = "True"
if age > 21:
    print ("You are legally allowed to purchase alcohol")
    print ("...All establishments are open to you legally")
if age < 21:
    print ("You are NOT legally allowed to purchase alcohol")
    print ("...Mind minimum age requirements")
if (age > 18 and citizen == "True"):
    print ("You are eligible to vote")
    print ("...Please register at the Provost Marshall's Office")

print("\n")


grade = 92

if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print ("Grade:", letterGrade)