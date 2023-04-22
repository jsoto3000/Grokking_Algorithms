from collections import deque

# function to define who is a seller
# if name ends with an 'm' then seller
def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
# "you" is mapped to an array
# so graph "you" will provide an array of all the neighbors of "you"
# "you" is the queue containing the people to check
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]

# anuj, peggy, thom, and jonny do not have any neighbors
# they have graphs mapped to them, but they have no mappings
# directed graph - relationship is only one way
# anuj is mapped to bob, but bob is not mapped anuj
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# function to find a seller
# algorithm will run until a seller is found or the queue becomes empty (no seller)
# will follow each edge (connection)
# run time for search of entire network is at least O(number of edges)
# uses queue to track searched items where adding one item takes constant time: O(1)
# breadth-first search takes O(V + E)
# V for number of vertices; and E for number of Edges
def search(name):
    # create a new queue
    search_queue = deque()
    # adds all neighbors to search queue
    search_queue += [name]
    # this is how you keep track of which people you've searched before.
    searched = set()
    '''
    Python also includes a data type for sets. 
    A set is an unordered collection with no duplicate elements. 
    Basic uses include membership testing and eliminating duplicate entries. 
    Set objects also support mathematical operations:
    like union, intersection, difference, and symmetric difference.
    Curly braces or the set() function can be used to create sets. 
    Note: to create an empty set you have to use set(), 
    not {}; the latter creates an empty dictionary.
    '''
    while search_queue: # while the queue is not empty
        # pop first person off the queue
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person in searched:
            continue
        # check if person is a seller
        if person_is_seller(person):
            print(person + " is a mango seller!") # yes! person is a seller
            return True

        else:
            # adds all of this person's neighbors to the search queue
            search_queue += graph[person]
            # marks this person as searched
            searched.add(person)
    return False # if you reach here that means no one in queue was a seller

search("you")