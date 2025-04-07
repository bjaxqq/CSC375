import bisect

class PointManager:
    def __init__(self):
        self.points = {}
        self.x_sorted = []
        self.y_sorted = []
        self.z_sorted = []
        self.x_set = set()
        self.y_set = set()
        self.z_set = set()

    def insert(self, label, x, y, z):
        if label in self.points:
            old_x, old_y, old_z = self.points[label]
            self._remove_from_sorted(self.x_sorted, old_x, self.x_set)
            self._remove_from_sorted(self.y_sorted, old_y, self.y_set)
            self._remove_from_sorted(self.z_sorted, old_z, self.z_set)
            print(f"UPDATED {label}")
        else:
            print(f"ADDED {label}")
        
        self.points[label] = (x, y, z)
        self._add_to_sorted(self.x_sorted, x, self.x_set)
        self._add_to_sorted(self.y_sorted, y, self.y_set)
        self._add_to_sorted(self.z_sorted, z, self.z_set)

    def delete(self, label):
        if label not in self.points:
            print("POINT DOES NOT EXIST")
            return
        
        x, y, z = self.points.pop(label)
        self._remove_from_sorted(self.x_sorted, x, self.x_set)
        self._remove_from_sorted(self.y_sorted, y, self.y_set)
        self._remove_from_sorted(self.z_sorted, z, self.z_set)
        print(f"DELETED {label}")

    def bbx(self):
        if not self.points:
            print(0)
            return
        x_len = self.x_sorted[-1] - self.x_sorted[0]
        y_len = self.y_sorted[-1] - self.y_sorted[0]
        z_len = self.z_sorted[-1] - self.z_sorted[0]
        print(x_len * y_len * z_len)

    def _add_to_sorted(self, arr, val, val_set):
        if val not in val_set:
            bisect.insort(arr, val)
            val_set.add(val)

    def _remove_from_sorted(self, arr, val, val_set):
        if val in val_set:
            index = bisect.bisect_left(arr, val)
            if index < len(arr) and arr[index] == val:
                arr.pop(index)
            val_set.discard(val)

def main():
    manager = PointManager()
    n = int(input())
    for _ in range(n):
        command = input().strip().split()
        if command[0] == "INSERT":
            manager.insert(command[1], int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "DELETE":
            manager.delete(command[1])
        elif command[0] == "BBX":
            manager.bbx()

if __name__ == "__main__":
    main()