# this function is used to combine two lists of ints.
# in first list(x), all elemnets of x which are even are used.
# in second list(y), all elemnets of y which are odd are used.
# the list of the elements is returned.
def combine(x, y):
    new_list = [] # make new list

    # loop x to find the element that is even
    for i in range(len(x)):
        if x[i] % 2 == 0:
            new_list.append(x[i]) # add the element to the new_list
    
    # loop y to find the element that is odd
    for i in range(len(y)):
        if y[i] % 2 == 1:
            new_list.append(y[i]) # add the element to the new_list

    return new_list

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(combine(a, b))
