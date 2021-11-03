def hello_world():
    print("hello world")

# hello_world()

def add_nums(num1,num2):
    return num1 + num2

# print(add_nums(1,2))

def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

print(is_prime(7))