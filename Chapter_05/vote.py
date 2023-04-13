# Prevent Duplicates Hash Table Use Case
# Voting Example

voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out!\n")
    else:
        voted[name] = True
        print("Let them vote!\n")

# Tom is added to Hash and allowed to vote
check_voter("Tom Sawyer")

# Huck is added to Hash and allowed to vote
check_voter("Huck Finn")

# Huck tries to vote again and is kicked out
check_voter("Huck Finn")