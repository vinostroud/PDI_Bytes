import collections 


def my_queue(n=5):
    queue = collections.deque([], maxlen = n)
    return queue

'''
 a deque object is created using the collections.deque() constructor.
The deque is initialized with an empty list [] as the initial contents and the specified maximum length n.
This maximum length means that the deque will only hold a maximum of n elements. 
If new elements are added when the deque is already at its maximum capacity, the oldest elements 
will be automatically removed to maintain the maximum length.
The created deque is returned from the function.
'''


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """