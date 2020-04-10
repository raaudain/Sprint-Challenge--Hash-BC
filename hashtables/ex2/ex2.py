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

    # The ticket for your first flight has a destination with a source of NONE
    
    # And the ticket for your final flight has a source with a destination of NONE.
    
    # Add destination to table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        
    for trip in len(length):
        # If flight is more than zero,
        # subtract one flight from trip
        if trip > 0:
            # One less flight
            flight = route[trip-1]
        else:
            flight = "NONE"

        hash_table_retrieve(hashtable, flight)
        
    return route[:-1]
            

