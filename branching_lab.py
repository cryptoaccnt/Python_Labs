subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]

if  ("Geography") in subjectList:
    takingGeography = True
else:
    takingGeography = False

print(takingGeography)

average = (gpas[0] + gpas[1] + gpas[2] / 3)

if average >= 33.3:
    print("Average is higher than 3.33")
if average <= 33.2:
    print("Average is lower than 3.33")