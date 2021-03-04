"""
2 sum problem - variation
instead of target sum value, find closes


target = 10

[11 , 9, 2, 3, 4, 5 ]  FInd two number whose sum is the closest to the target

NOTE : that the two values with equal sum may or may not be be present

----------------

if i find exact value :  then the difference in the target will be 0
target - sum_of_values


and if don't find that equal sum
i need to minimize the difference       target - sum_of_values


Brute force : o(n2) approach, maintain

optimize :
1. map will not work here,
2. meet in the middle
        Target = 10
        dif = INTEGER_MAX_VALUE
        [11 , 9, 2, 3, 4, 5 ]  --> [ 2, 3, 4, 5 9, 11]   n lg n
        [ 2, 3, 4, 5 9, 11]    sum=13  diff=3      Record min diff
          ^              ^
        [ 2, 3, 4, 5 9, 11]    sum=11  diff=1       record this, and also the values
          ^          ^
        [ 2, 3, 4, 5 9, 11]    sum=7  diff=3       not record
          ^        ^
        [ 2, 3, 4, 5 , 9, 11]    sum=8  diff=2       not record
             ^     ^
        [ 2, 3, 4, 5 , 9, 11]    sum=9  diff=1       choose to record or not, basically overriding the earlier value
                ^   ^

        O(n log n)  approach, to closed
        if its already sorted, then its O(n)
"""
