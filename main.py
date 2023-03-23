def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
    
print("ENTER TEMPRATURE IN Fahrenheit :")
a=input()
b=convert(a)
print("IT IS",b,"CELCIUS")
