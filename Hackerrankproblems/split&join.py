def split_and_join(line):
    string_splitted = line.split() 
    result = "-".join(string_splitted)   #['this', 'is', 'a', 'string']
    return result 
    return string_splitted
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
