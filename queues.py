"""ITECC04 Laboratory 4, Part D: the circular queue and the deque.

This part is on your own. No guided walkthrough, and the tests are the only
feedback you get, exactly as in the coding quiz.

WHY CIRCULAR. A queue over a plain list, dequeuing with pop(0), shifts every
remaining element one place left. That is O(n) for an operation that should
be O(1). Moving the FRONT INDEX forward instead of moving the data is the
whole idea, and the modulo operator is what makes the index wrap back to 0
when it runs off the end.

The queue holds a fixed number of slots. It does not grow.
"""


class CircularQueue:

    def __init__(self, capacity):
        """Step 1. A list of `capacity` Nones, a front index, and a count.

        Raise ValueError if capacity is less than 1.

        Keep a COUNT, not a rear index alone. With only front and rear you
        cannot tell a full queue from an empty one: both give front == rear.
        A count answers both questions with no ambiguity.
        """
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._items = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._count = 0

    def enqueue(self, item):
        """Step 2. Add at the rear. Raise OverflowError when full.

        You are not storing a rear index, so compute it:
            rear = (front + count) % capacity
        Write the item there, then increase the count.
        """
        if self.is_full():
            raise OverflowError("enqueue on full queue")
        rear = (self._front + self._count) % self._capacity
        self._items[rear] = item
        self._count += 1

    def dequeue(self):
        """Step 3. Remove and return the front item. IndexError when empty.

        Read the item at front, clear that slot to None so nothing stale is
        left behind, advance front with modulo, decrease the count, return.
                """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._count -= 1
        return item

    def peek(self):
        """Step 4. Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._items[self._front]

    def is_empty(self):
        """Step 5. True when the count is 0."""
        return self._count == 0

    def is_full(self):
        """Step 6. True when the count has reached the capacity."""
        return self._count == self._capacity

    def size(self):
        """Step 7. Return the count."""
        return self._count

    def slots(self):
        """Written for you. Returns a copy of the raw list.

        For inspecting wraparound during the demonstration. Not part of the
        ADT, and your other methods must never call it.
        """
        return list(self._items)


class Deque:
    """A queue you may add to and remove from at both ends."""

    def __init__(self):
        """Step 8. Create the empty list."""
        self._items = []

    def add_front(self, item):
        """Step 9. Insert at position 0."""
        self._items.insert(0, item)

    def add_rear(self, item):
        """Step 10. Append at the end."""
        self._items.append(item)

    def remove_front(self):
        """Step 11. Remove and return index 0. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove from front of empty deque")
        return self._items.pop(0)

    def remove_rear(self):
        """Step 12. Remove and return the last item. IndexError when empty."""
        if self.is_empty():
            raise IndexError("remove from rear of empty deque")
        return self._items.pop()

    def is_empty(self):
        """Step 13. True when there is nothing in the deque."""
        return len(self._items) == 0

    def size(self):
        """Step 14. Return how many items are held."""
        return len(self._items)


def is_palindrome(text):
    """Step 15. True when text reads the same both ways.

    Ignore anything that is not a letter, and ignore case. Load the letters
    into a Deque, then compare front against rear until one or zero letters
    remain. A word of odd length ends with one letter in the middle, which
    always matches itself, so stop while size is greater than 1.
    """
    d = Deque()
    for char in text:
        if char.isalpha():
            d.add_rear(char.lower())
    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
    return True
