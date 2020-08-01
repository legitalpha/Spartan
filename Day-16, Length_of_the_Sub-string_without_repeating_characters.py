str = input("Enter a string : ")

def sub_string(str):

    a = list(str)

    ab = dict.fromkeys(a,2)
    length = len(ab)
    print("The length of the sub-string without repeating charachters is",length)

sub_string(str)