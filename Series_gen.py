a = int(input("Enter a: "))

if a <= 0:
    print("Error: Please enter a positive integer.")
else:
    result = []
    for i in range(1, a + 1):
        result.append(2 * i - 1)
    print(result)
