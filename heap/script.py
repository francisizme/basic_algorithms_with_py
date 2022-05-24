class MaxHeap:
    def __init__(self):
        self.__last_index = 0
        self.__list = [None]

    def get_list(self):
        return self.__list

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def add(self, value):
        self.__last_index += 1
        self.__list.append(value)
        print(f"Added {value}")
        self.heapify_up()

    def heapify_up(self):
        idx = self.__last_index
        while self.parent_idx(idx) > 0:
            child = self.__list[idx]
            parent = self.__list[self.parent_idx(idx)]
            if parent < child:
                self.__list[idx] = parent
                self.__list[self.parent_idx(idx)] = child

            print(f"Swapped {child} and {parent}")
            idx = self.parent_idx(idx)
        print("Heapify up done")
