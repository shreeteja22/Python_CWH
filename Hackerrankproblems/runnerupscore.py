if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrl = list(arr)
    mx = max(arrl)
    ne = []
    for x in arrl:
        if(x<mx):
            ne.append(x)
    mx1 = max(ne)
    print(mx1)





# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# The first line contains . The second line contains an array   of  integers each separated by a space.


                                                        # Summary of Logic:
                                                        # Input a list of numbers.
                                                        # Find the maximum number.
                                                    # Create a new list excluding the maximum.
                        # Find the largest number in the new list (which will be the second highest in the original list).
                                                    # Print the second highest number.
                    # This is a straightforward approach to solving the problem of finding the second highest number in a list.