#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    cache = {}
    tickets_table = {}

    # build dictionary from tickets array
    for k, v in enumerate(tickets):
        tickets_table[k] = v

    # find starting flight
    for k, t in enumerate(tickets):
        if t.source == "NONE":
            cache[t.source] = t.destination

    # build cache with connecting flights info
    i = 0
    while len(cache) < length - 1:

        # special case when i reaches end of tickets_table
        if i == length:
            i = 0

        # find next flight based on last destination in cache
        if tickets_table[i].source in cache.values():
            cache[tickets_table[i].source] = tickets_table[i].destination
            i += 1
        
        # increment through tickets_table
        else: i += 1

    results = list(cache.values())
    results.append("NONE")

    return results

tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE" ),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))
