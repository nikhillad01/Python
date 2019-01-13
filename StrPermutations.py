"""******************************************************************************
* Purpose: String Permutations
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""


def permutation(lst):
    """This method is used to find str permutations
    :return: string permutations """
    if len(lst) == 0:                   # If lst is empty then there are no permutations
        return []

    if len(lst) == 1:
        return [lst]
    l = []                              # empty list that will store current permutation

    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]     # Extract lst[i] or m from the list.
                                        # remaining list
       for p in permutation(remLst):    # Generating all permutations where m is first element
           l.append([m] + p)
    return l




if __name__=="__main__":
    data = list(input("Enter string"))  # Input string and convert to list
    for p in permutation(data):     # calling permutation method to find permutations with each chars.
        print (p)
