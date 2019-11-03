def FirstFactorial(num):

  fact=1
  i=1
  while i <= num:
      fact = fact * i
      i=i+1
  num=fact
  return num


def fibo(n):
    fib=[]
    a,b = 0,1
    for i in range(1, n+2):
        c = a + b
        fib.append(b)
        a = b
        b = c
    print(fib)

conti = True
while conti:
    try:
        a = input("For Fibonatchi write fibo, for factorial write fact, for quit write q : ")
        if a=="fibo":
            b = int(input("Suite Fibonatchi jusqu'à quel nombres ? : "))
            print(fibo(b))
        elif a=="fact":
            b = int(input("Factoriel de quel nombres ? : "))
            print(FirstFactorial(b))
        elif a=="q":
            break
    except:
        print("On attend fibo ou fact")
    else:
        conti = True