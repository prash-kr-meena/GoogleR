class MH:
    def __init__(self):
        self.array = []
        pass

    def push(self):
        pass

    def pop(self):
        pass

    # ---- private methods ----
    def _has_parent(self, i):  # i : index
        return (i - 1) / 2 >= 0

    def _has_left_child(self, i):
        return (2 * i) + 1

    def _has_right_child(self, i):
        return (2 * i) + 2

    def _get_parent(self, i):
        return self.array[(i - 1) / 2]

    def _get_left_child(self, i):
        return self.array[(2 * i) + 1]

    def _get_right_child(self, i):
        return self.array[(2 * i) + 2]


if __name__ == '__main__':
    pass
