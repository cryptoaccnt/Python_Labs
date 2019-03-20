# while (true):
    #Do this stuff

x = 0
while (x <= 25):
    print("The value of x: ", x)
    x=x+1

counter = 100
while (counter > 0):
    print(counter)
    counter = counter - 10
else:
    print("Counter is no longer greater than 0")

## Don't make endless loops!!

# For Loops

courseName = "Python for Biginners 2017"

for letter in courseName:
    print("Current Letter is ", letter)
    if (letter == " "):
        print("This is a space character")

Bands = ["Journey", "REO Speedwagon", "Foreigner", "Heart", "The Cure"]

for x in Bands:
    print("Current Band: ", x)

## Nested Loops

count = 11
x = 0

while x < count:
    y = 0
    while y < 11:
        print(y)
        y = y + 1
        if y > 10:
            print("Break")
    x = x + 1