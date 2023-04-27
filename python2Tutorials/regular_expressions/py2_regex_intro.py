#!/usr/bin/env python
from __future__ import print_function


def main():
    """ This is an introduction to Regular Expressions


    """

    # Conceptual demonstration of string matching (substring)
    phrase = "Drink up me hardies, yo ho!"
    if "hardies" in phrase:
        print("Jack Sparrow said \"{}\"".format(phrase))
    print()
    print()

    # Programmatic example of string matching process
    # NOTE: the actual process is typically done character by character, but I want to make the example simple
    sub = "hardies"
    for i in range(0,len(phrase)):
        segment = phrase[i:len(sub) + i]
        if sub == segment:
            print("Match for \"{}\" started at [{}]".format(segment, str(i)))
            break
        else:
            print("[{}] doesn't match!".format(segment))
    print()

    """
        For posterity, here is a way to do this character by character which is closer to how
        matching algorithms work (although probably using a formal tree as opposed to the for loop I 
        created. That being said, I do use tree-like logic to short circuit the loops)
        
        i and j are created outside the loop so that we can manage the counters conditionally. 
        j_str is just a vulgar shortcut to memoization. This is a place to store our successful hits
        
        The outer loop is the phrase. This makes sense because we are comparing the inner loop to each 
        iteration of the outer loop. 
        
        The inner loop is the substring. 
        
        If the value at the current index of the inner loop matches the value at the current index of the
        outer loop, then we add the value to the storage container, and then we increment the value of the 
        outer loop
            - this allows us to short circuit the iteration of the outer loop.
        
        If it doesn't match, then we reset the counters, clear our storage container and then bail out of the loop, 
        because we'll need to start over. 
        
        Finally, outside of the inner loop, we evaluate the length of the substring against the length of 
        the storage container. if they match, we are done. 
        
        # If you want to see the iterative nature of the matching, uncomment the commented out lines  
            
    """
    i = 0
    j = 0
    j_str = ""
    for i in range(i, len(phrase)):
        for j in range(j, len(sub)):
            # print("Phrase: {}".format(phrase[i]), end=" ")
            # print("Sub Index: {}".format(j), end=" ")
            # print("Sub Value: {}".format(sub[j]), end=" ")
            if phrase[i] == sub[j]:
                j_str += sub[j]
                print("Result: {}".format(j_str))
                i += 1
            else:
                # print()
                j_str = ""
                j = 0
                break
        if len(j_str) == len(sub):
            break


if __name__ == '__main__':
    main()
