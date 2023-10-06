class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr

        mid = len(self.arr) // 2
        left = MergeSort(self.arr[:mid])
        right = MergeSort(self.arr[mid:])

        sorted_left = left.sort()
        sorted_right = right.sort()
        merged = self.merge(sorted_left, sorted_right)

        print(f"Merging: {sorted_left} and {sorted_right} => {merged}")

        return merged