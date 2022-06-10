#1 way
result = lambda a, b: a * b

string = input()
number = int(input())
print(result(string, number))

#2 way
string = input()
counter = int(input())

result = string * counter
print(result)

#3 way
def result(a, b):
    return a * b


string = input()
counter = int(input())
print(result(string, counter))
