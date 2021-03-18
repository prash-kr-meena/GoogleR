"""

Implement all operation in O(1)

insert(x) : insert only if that does not exit
remove(x) : remove if exists
search(x) : return if this number exists or not
getRandom() : get any random no form the datastructures


Input : are integers only



# we can do with map, and an array
# delete is tricy

use array --> delete an element with O(1) and that is the trick

so the idea is to have a index mapping for all the elements in the hashmap with the index in the array
and when it comes to the remove operation, you can just get the index of the element from the hash-set
and then you can go to that index in the array and now to delete it, you need to first swap it with the last element
        after sapping you need to also udpate the index of that last element in the hashmap also NOTE:
        and then you can remove the new_last_element from the array and also remove it from the hashmap

for random : you can get a random index in the range and then just get the value at that index and give it to the user
        No need to go to hashmap to check
"""

if __name__ == '__main__':
    pass
