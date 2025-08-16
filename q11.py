n = int(input("Enter the number : "))
end = int(n ** 0.5)

for i in range(2, end + 1):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
    
