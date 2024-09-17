def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)




                                            #Summary of Logic:
                                            # Input a string.
                                # Input the position and the character.
                                # Replace the character at the specified position.
                                            # Output the modified string.
                # The code essentially allows easy modification of a string at a given position.