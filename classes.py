# ------------------------------------------------------------------------
# Class: Task
# ------------------------------------------------------------------------
class Task:
    def __init__(self, name, rank, ext_id):
        self.name = name
        self.rank = rank
        self.external_tracking_id = ext_id

    # This is used for sorting
    def __lt__(self, other):
         # If rank is None, set it to 0
        if self.rank is None:
            self.rank = 0
        if other.rank is None:
            other.rank = 0

        return self.rank < other.rank

    def __repr__(self):
        return f"{self.name}\n\trank: {self.rank}\n\texternal-tracking-id: {self.external_tracking_id}\n"