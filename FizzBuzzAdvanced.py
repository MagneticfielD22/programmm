def fizz_buzz(n,x,y):

    if n%x==0 and n%y==0:
        answer="FizzBuzz"
    elif n%x==0:
        answer="Fizz"
    elif n%y==0:
        answer="Buzz"
    else:
        answer=str(n)

    return answer

n=int(input())
x=int(input())
y=int(input())
number=fizz_buzz(n,x,y)
print(number)