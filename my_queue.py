import unittest

class MyQueue(object):

    def __init__(self, items=[]):
        '''
        Assume items is an iterable object
        :param items:
        '''
        self._items = items
        self._update_last_index()

    def _update_last_index(self):
        self._last_index = len(self._items) - 1

    def _get_last_item(self):
        return self._items[self._last_index]

    def pull(self):
        last = self._items[self._last_index]
        self._items.remove(self._get_last_item())
        self._update_last_index()
        return last

    def push(self, item):
        self._items.append(item)
        self._update_last_index()

    def count(self):
        return self._last_index + 1

    def clear(self):
        self._items = []
        self._update_last_index()

class QueueTests(unittest.TestCase):

    def test_ensure_fifo(self):
        input = 1
        q = MyQueue([input])
        result = q.pull()
        self.assertEqual(input, result)

    def test_push(self):
        q = MyQueue()
        q.push(10)
        self.assertEqual(1, q.count())

    def test_push_many(self):
        q = MyQueue()
        q.push(10)
        q.push(20)
        q.push(30)
        self.assertEqual(30, q.pull())


def main():
    # Implement a queue in an array
    unittest.main()

main()
