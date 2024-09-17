def swap_case(s):
    a = s.swapcase() #swapcase is builtin function perhaps
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  