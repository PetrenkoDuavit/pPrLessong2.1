# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#homeworck 2.1-------------------------

number = int(input("Enter number:"))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number % 100 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)

#homeworck 2.2-------------------------

number = int(input("Enter number:"))
n1 = number // 10000
n2 = number // 1000 %10
n3 = number // 100 % 10
n4 = number % 100 // 10
n5 = number % 10
print(n5*10000+n4*1000+n3*100+n2*10+n1)