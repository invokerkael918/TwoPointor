class Solution1:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):

        # write your code here
        start = 0
        end = len(A) - 1
        self.quicksort(A, start, end)

    def quicksort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start + end) // 2]
        while left <= right:
            # below 2 while loop
            # find a pair with A[left]>=A[right]

            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quicksort(A, start, right)
        self.quicksort(A, left, end)


class Solution2:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        temp = [0 for _ in range(len(A))]
        self.merge_sort(0, len(A) - 1, A, temp)

    def merge_sort(self, start, end, A, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.merge_sort(start, mid, A, temp)
        self.merge_sort(mid + 1, end, A, temp)
        self.merge(start, mid, end, A, temp)

    def merge(self, start, mid, end, A, temp):
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right];
                right += 1

            index += 1

        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1

        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1

        for index in range(start, end + 1):
            A[index] = temp[index]