class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_subsequence(sub):
            target = sub * k
            it = iter(s)
            return all(c in it for c in target)
        counts = collections.Counter(s)
        hot_chars = sorted([char for char, count in counts.items() if count >= k], reverse=True)
        ans = ""
        queue = collections.deque([""])
        while queue:
            curr = queue.popleft()
            for char in hot_chars:
                nxt = curr + char
                if is_subsequence(nxt):
                    if len(nxt) > len(ans) or (
                        len(nxt) == len(ans) and nxt > ans
                    ):
                        ans = nxt
                    queue.append(nxt)

        return ans


        