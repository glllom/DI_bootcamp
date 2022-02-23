class Door:
    obj = 0

    @classmethod
    def instances_counter(cls):
        cls.obj += 1

    def __init__(self, locked, next=None):
        if next is None:
            self.next = []
        else:
            self.next = next
        self.id = self.obj
        self.instances_counter()
        self.locked = locked

    def can_go_to(self, other_door):
        if self == other_door:
            return True
        if self.locked or len(self.next) == 0:
            return False
        result = False
        for door in self.next:
            result = result or door.can_go_to(other_door)
        return result


d0 = Door(False)
d1 = Door(False)
d2 = Door(True)
d3 = Door(False)
d4 = Door(False)
d5 = Door(False)
d6 = Door(False)
d7 = Door(False)

d0.next = [d1, d2]
d1.next = [d3]
d5.next = [d6]
d2.next = [d4, d5]

print(d0.can_go_to(d0))
print(d0.can_go_to(d1))
print(d0.can_go_to(d2))
print(d0.can_go_to(d3))
print(d0.can_go_to(d4))
print(d0.can_go_to(d5))
print(d0.can_go_to(d6))
print(d0.can_go_to(d7))
