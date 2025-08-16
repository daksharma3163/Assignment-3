def every_nth_char(s, n):    
    for i in range(0,len(s),n+1):
        print(s[i],end='')

string = input("Enter the text: ")
n = int(input("Enter the step: "))
every_nth_char(string, n)
