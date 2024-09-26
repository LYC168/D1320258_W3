a=int(input('輸⼊係數 a：'))
b=int(input('輸⼊係數 b：'))
c=int(input('輸⼊係數 c：'))
x1=(-b+(b**2-4*a*c)**0.5)/2*a
x2=(-b-(b**2-4*a*c)**0.5)/2*a
print("⽅程式的根為：x1=%1.1f,x2=%1.1f"%(x1,x2))