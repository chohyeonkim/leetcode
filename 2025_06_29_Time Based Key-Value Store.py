
class TimeMap:

    def __init__(self):
        # prev_timestamp <= timestamp
        self.user_map = {} # key user.name value (timestamp value) # stric  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.user_map:
            self.user_map[key] = []

        self.user_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.user_map:
            return ""

        time_value_arr = self.user_map[key]

        res = self.find_timestamp(time_value_arr, timestamp)
        return res

    def find_timestamp(self, arr:list[tuple[int,str]], target:int) -> str:

        if len(arr) == 0:
            return ""

        left = 0
        right = len(arr) - 1

        while left <= right:
            
            mid = (left + right) // 2
            compare = arr[mid][0]

            if compare == target:
                return arr[mid][1]

            if compare > target:
                right = mid - 1

            else:
                left = mid + 1

        print("target", target)
        print("left", left)
        print("right", right)

        if arr[right][0] > target:
            return ""

        return arr[right][1]





