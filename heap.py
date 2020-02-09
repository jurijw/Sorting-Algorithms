from random import randint

# Adapted from https://www.youtube.com/watch?v=t0Cq6tVNRBA


# Helper methods for navigating the heap
def get_left_child_index(parent_index):
    return 2 * parent_index + 1


def get_right_child_index(parent_index):
    return 2 * parent_index + 2


def get_parent_index(child_index):
    if child_index % 2 == 0:
        return (child_index // 2) - 1
    return (child_index - 1) // 2


class Heap:
    def __init__(self, heap_list=None):
        if heap_list == None:
            self.heap_list = []
            self.size = 0
        else:
            self.heap_list = heap_list
            self.size = len(heap_list)

    def has_left_child(self, parent_index):
        return get_left_child_index(parent_index) < self.size

    def has_right_child(self, parent_index):
        return get_right_child_index(parent_index) < self.size

    def has_parent(self, child_index):
        return get_parent_index(child_index) >= 0

    def get_left_child(self, parent_index):
        return self.heap_list[get_left_child_index(parent_index)]

    def get_right_child(self, parent_index):
        return self.heap_list[get_right_child_index(parent_index)]

    def get_parent(self, child_index):
        return self.heap_list[get_parent_index(child_index)]

    def peek(self):
        if self.size == 0:
            raise Exception("Heap is empty.")
        else:
            return self.heap_list[0]

    def heapify_up(self):
        # Get index of last element in the heap
        index = self.size - 1

        # While the heap element has a parent that is greater than itself
        while self.has_parent(index) and (self.get_parent(index) > self.heap_list[index]):
            # Swap them
            self.heap_list[index], self.heap_list[get_parent_index(
                index)] = self.heap_list[get_parent_index(index)], self.heap_list[index]
            # Set the new index to the parent index
            index = get_parent_index(index)

    def heapify_down(self):
        # Get index of root element
        index = 0

        while self.has_left_child(index):
            # Check which child (if it exists) is smaller and get that child's index
            if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = get_right_child_index(index)
            else:
                smaller_child_index = get_left_child_index(index)

            # Break out of the loop once the item is smaller than its smallest child
            if self.heap_list[index] < self.heap_list[smaller_child_index]:
                break
            else:
                # Swap it with its smaller child
                self.heap_list[index], self.heap_list[smaller_child_index] = self.heap_list[smaller_child_index], self.heap_list[index]

            # Update the index
            index = smaller_child_index

    def poll(self):
        if self.size == 0:
            raise Exception("Heap is empty.")
        else:
            # Swap the first element with the last
            self.heap_list[0] == self.heap_list[self.size - 1]
            self.heapify_down()

    def add(self, element):
        self.heap_list.append(element)
        self.size += 1
        self.heapify_up()


def main():
    # TESTING
    test_heap = Heap()

    test_heap.add(7)
    test_heap.add(5)
    test_heap.add(14)
    test_heap.add(6)
    print(test_heap.heap_list)


if __name__ == "__main__":
    main()
