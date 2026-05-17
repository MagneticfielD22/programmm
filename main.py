def fizz_buzz(n):

    if n%3==0 and n%5==0:
        answer="FizzBuzz"
    elif n%3==0:
        answer="Fizz"
    elif n%5==0:
        answer="Buzz"
    else:
        answer=str(n)

    return answer

number=fizz_buzz(int(input()))
print(number)