#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


# Write a function reconstruct_trip to reconstruct your trip from your mass of flight tickets. Each ticket is represented as class Ticket
class Ticket:
    def __init__(self, source, destination):
        # Represents the starting airport
        self.source = source
        # Represents the next airport
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # Add destination to table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    
    # Goes through the mulitple destinations
    for trip in range(length):
        # Adds NONE if trip has no destination
        if trip <= 0:
            start = "NONE"
        else:
            # Deletes index before and goes to next destination
            start = route[trip-1]

        # Retrives route from hash table
        route[trip] = hash_table_retrieve(hashtable, start)
    
    # Return route without "NONE"
    return route[:-1]
    
            
# TESTING
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]
        
# print(reconstruct_trip(tickets, 3))