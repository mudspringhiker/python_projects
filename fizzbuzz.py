import sys


def main():
    header()
    try:
        limit = int(sys.argv[1])
    except:
        limit = int(input("Up to what number do you want to count to? "))
    for i in range(1, limit+1):
        fizzbuzz(i)
    print("Goodbye!")


def header():
    print("------------------------")
    print("      FIZZBUZZ")
    print("------------------------")
    print()


def fizzbuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    

if __name__ == "__main__":
    main()
