#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #find two items whose sum of weights equals the weight limit
    #Your function will return an instance of an Answer tuple that has the following form: (zero, one)

    for index, key in weights:
        hash_table_insert(ht, key, index)
        
    # The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index.
    for 
    
        

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

