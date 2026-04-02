class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        output = []
        q = collections.deque()

        while r < len(nums):
            # we pop all elements smaller than nums[r]
            # because while nums[r] is in window and greater
            # than all other elements in the window then obviously
            # it will always be the max

            while q and nums[r] > nums[q[-1]]:
                q.pop()

            # we add r to queue:
            q.append(r)

            # if our current left index is greater than the left index
            # stored as the max we need to remove the stored elements
            # as they are no longer in the window
            while l > q[0]:
                q.popleft()

            # if we have a window of length k lets update the output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output