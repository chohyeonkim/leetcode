class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot_array = [0] * length
        self.snap_array_map = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # print(snapshot_array)
        self.snapshot_array[index] = val
        arr = self.snap_array_map[index]
        if arr and arr[-1][0] == self.snap_id:
            arr[-1] = (self.snap_id, val)
        else:
            self.snap_array_map[index].append((self.snap_id, val))  # (0,5)

    def snap(self) -> int:
        current_id = self.snap_id
        self.snap_id += 1
        return current_id

    def get(self, index: int, snap_id: int) -> int:
        binray_arr = self.snap_array_map[index]
        # print(binray_arr)

        left = 0
        right = len(binray_arr) - 1
        res = 0

        while left <= right:
            mid = (left + right) // 2

            s_id, val = binray_arr[mid]

            if s_id == snap_id:
                return val

            elif s_id < snap_id:
                res = val
                left = mid + 1

            else:
                right = mid - 1

        return res
