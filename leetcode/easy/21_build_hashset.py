class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        #self.hashset = [ListNode(0)] * 10**4 dont do this
        # this copies the same listnode 10^4 times and it doe snot create new node everytime
        self.hashset = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.hashset)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.hashset)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        index = key % len(self.hashset)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False