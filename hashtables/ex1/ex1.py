#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

  
    # Inserts limit and lists of weights into hash table
    for item in range(length):
        hash_table_insert(ht, weights[item], item)
    
    # Finds two items whose sum of weights equals the weight limit
    for item in range(length):
        # Subtracts the value of the index from limit   
        the_key = limit-weights[item]
        # Retrieves index from hash table using the_key as the key
        test = hash_table_retrieve(ht, the_key)
        
        if test:
            if test > item:
                #print([test, item])
                return([test, item])

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# Testing

# weights_1 = [9]
# answer_1 = get_indices_of_item_weights(weights_1, 1, 9)

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# weights = [ 4, 6, 10, 15, 16 ]
# # #, length = 5, limit = 21
# print(get_indices_of_item_weights(weights, 5, 21))