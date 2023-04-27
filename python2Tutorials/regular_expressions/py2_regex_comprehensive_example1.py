#!/usr/bin/env python
from __future__ import print_function
from operator import itemgetter
import re


def main():
    """
        This is an example of using regular expressions to format data for the purposes of analysis,
        presentation or other uses.

        The included file (ma_pop.txt) has been made available from US Census data.

        The format of each line is:

        HEADING         MEANING                         DO WE CARE

        SUMLEV          geographic summary level        NOPE
        STATE           State FIPS code                 NOPE (this data is all from MA)
        COUNTY          County FIPS code                NOPE
        PLACE           Place FIPS code                 NOPE
        COUSUB          Minor Civil Division FIPS Code  NOPE
        CONCIT          Consolidated city FIPS Code     NOPE
        PRIMGEO_FLAG    Primitive Geography Flag        NOPE
        FUNCSTAT        Functional Status Code          YES! (See Note)
        NAME            Area Name                       YES!
        STNAME          State Name                      NOPE (this data is all from MA)
        CENSUS2010POP   4/1/2010 Population (census)    YES!
        ESTBASE2010     4/1/2010 estimation             NOPE
        POPEST2k##      7/1/20## estimation             NOPE (See Note)


        NOTE: there are two functional status codes available in this data. If you look closely to the
        data, some towns/cities are listed twice. 1 includes an A for FUNCSTAT, and another includes an F
        A FUNCSTAT of 'F' is a fictitious placeholder that was used to flesh out the schema of the data
        while actual data was not initially available. We don't want to use those entries.

        NOTE: We only care about the POPULATIONESTIMATEBASE from 2017, because our final result is
        going to rank towns/cities based on population growth between 2010 and 2017.

    """

    """
        Here is our doozie of a regex!
        
        EXPLAINED:
        
        1.) (((\d+),){7})
        
                                (This is an example of grouping (or filtering) to exclude this data
                                because we don't care about it for this particular data operation) 
        
                ((\d+),){7}     This layer of the group shows that whatever precedes {7} must occur
                                7 times.
                                 
                ((\d+),)        This is a nested group that must be followed by a comma 
                
                (\d+)           This is the innermost group that must be 1 or more numbers. (can't be 0)
                
                
        2.) A,                  This must match the capital letter 'A', followed by a comma
        
        3.) (?P<area_name>([A-Za-z ]*(?<!County)(?<!Massachusetts)))
        
                ?P<area_name>([A-Za-z ]*(?<!County)(?<!Massachusetts))
               
                                This is the outermost layer of the group, which is the name of the
                                group for later backreference. 
                                
                         
                [A-Za-z ]+(?<!County)(?<!Massachusetts)
                
                                This shows a character class that must have at least 1 of any
                                non-case specific letter or a single space, followed by 2 lookaround
                                statements
                                
                (?<!County)(?<!Massachusetts)
                
                                These are two negative look-behind statements that mean our match
                                can't contain the specified text
                                
        4.) ,Massachusetts,     This matches the word 'Massachusetts' sandwiched between two commas.
        
        5.) (?P<pop_2010>\d+)   This matches a group of 1 or more numbers, and it is named pop_2010
        
        6.) (((\d+),){8})       See #1 of this list, this works the same way, but repeats 8 times.
        
        7.) (?P<pop_2017>\d+)   See #5 of this list, this works the same way w/ the name.. pop_2017
                    
        
    """
    pattern = r"(((\d+),){7})A,(?P<area_name>([A-Za-z ]+(?<!County)(?<!Massachusetts)))," \
              r"Massachusetts,(?P<pop_2010>\d+),(((\d+),){8})(?P<pop_2017>\d+)"

    # Let's use the pattern against each line to filter out the things we don't need.
    ma_pop_list = []
    with open('ma_pop.txt', 'r') as file_handle:
        for line in file_handle:
            result = re.search(pattern, line)
            if result:

                # For each "hit", let's transform the "area_name" by removing superfluous data
                # and let's perform the pop growth calculation by subtracting 2010 from 2017.
                name = result.group("area_name").lower().replace(" town", "").replace(" city", "").title()
                pop_growth = int(result.group('pop_2017')) - int(result.group('pop_2010'))

                # append the collection as an immutable object to our list.
                ma_pop_list.append((name, pop_growth))

    """
        Let's work w/ the list to come up with our top 10
        
        We are sorting a set, just to avoid any other duplication from the table. 
        This ensures that we have unique values. 
    """
    top_ten = sorted(set(ma_pop_list), key=itemgetter(1), reverse=True)
    #for index, listing in enumerate(top_ten[0:10]):
    for index, listing in enumerate(top_ten):     # This shows entire list.
        print("{:<3}.) {:<18} Population Growth (2010-2017): {}".format(index + 1, listing[0], listing[1]))


if __name__ == '__main__':
    main()