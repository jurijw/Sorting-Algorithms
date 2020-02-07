class Heap:
    def __init__(self, heap_list=None):
        if heap_list == None:
            self.heap_list = []

    # Helper methods for navigating the heap
    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    @staticmethod
    def get_right_child_index(parent_index):
        return 2 * parent_index + 2

    @staticmethod
    def get_parent_index(child_index):
        if child_index % 2 == 0:
            return (child_index // 2) - 1
        return (child_index - 1) // 2
