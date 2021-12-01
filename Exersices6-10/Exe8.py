# define a function to merge lists into one
def Merge(given_list):
    # considering a blank list
    result = []
    for item in given_list:
        result.extend(item)
    # sort items for final show
    print(sorted(result))

# calling function
Merge([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])
