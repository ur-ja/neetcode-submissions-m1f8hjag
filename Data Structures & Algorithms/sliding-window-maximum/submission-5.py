class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = collections.deque()
        l = r = 0

        while r < len(nums):
            # while the new elem being inserted is 
            # greater than the rightmost elem in the queue
            # remove elements 
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # now insert the new elem to the right
            dq.append(r)

            # while the leftmost element is not 
            # in the current window remove it 
            while dq[0] < l:
                dq.popleft()

            # now whatever the leftmost elem is is the max 
            # append it to the result
            if r - l + 1 == k:
                output.append(nums[dq[0]])
                l += 1
            r += 1

        return output