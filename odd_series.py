
a = int(input("Enter integer a: "))

if a <= 0:
    print("Error: Please enter a positive integer.") 
else:

    if a % 2 == 0:
        count = a - 1
    else:
        count = a

    series = []
    for i in range(count):
        
        num = 2 * i + 1
        series.append(str(num))


print(", ".join(series))