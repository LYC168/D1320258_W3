n=int(input('輸⼊三位數字：'))
h=n//100
t=(n//10)%10
o=n%10
r=o*100+t*10+h
print('結果：',r)