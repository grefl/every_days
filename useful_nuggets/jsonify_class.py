import json

# your class, just using Node as an example
class Node:

    def __init__(self, value):

        self.value = value 
        self.next  = None




head = Node(1)
head.next = Node(2)

print(json.dumps(head, default=vars))
