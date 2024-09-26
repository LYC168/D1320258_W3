n= int(input("請輸入一個三位數："))

h=n//100
t=(n//10)%10
o=n%10

t=h+t+o

print('每位數字的總和：',t)