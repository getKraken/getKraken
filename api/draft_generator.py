# Find the members of a given series, and return an array of their primary IDs
user_IDs = [1,2,3,4,5]

# Find the corresponding events of a given series, and return the primary IDs of those events
event_IDs = ['a','b','c','d','e']

# Represents a particular participant in the current Draft Round (a linked list)
# Holds value of the user's ID whose turn is associated with the node
# Holds a reference to the next participant in the draft round
class Participant:

    def __init__(self, user_ID, next=None):
        self.user_ID = user_ID
        self.next = next
# A linkedlist representation of the participants of a specific round of the draft
class DraftRound:

    def __init__(self, head=None):
        self.head = head

    def add(value):
        partcipant = Participant(value)
        if not self.head:
            self.head = partcipant
            return
        partcipant.next = self.head
        self.head = partcipant.next


def draft_generator(user_IDs, event_IDs):
    rounds = len(event_IDs) // len(user_IDs)
    remainder = len(event_IDs) % len(user_IDs)
    for i in range(1, rounds):
        round = DraftRound()
        for j in range(user_IDs-1):
        def placement_attempt():
