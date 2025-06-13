for i in range(1,21):
    print(i)
for i in range(1,21):
    if i % 2 == 0 :
        print(i)
for i in range(1,11):
    if i != 5:
        print(i)
        continue


for i in range(1,11):
    if i == 7:
        break
    print(i)


secret_number = 7
while True:
    number=int(input("guess the number 1-10 : "))
    if number == secret_number:
        print(f"you got it , well done it's number {number}")
        break
    else:
        continue     

