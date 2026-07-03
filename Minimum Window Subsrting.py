class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target = Counter(t)
        window = {}
        have, need = 0, len(target)
        res, reslen = [-1, -1], float("inf")
        left = 0
        for right in range (len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in target and window[c] == target[c]:
                have +=1
            while have == need:
                if (right - left + 1) < reslen:
                    res = [left, right] 
                    reslen = right - left + 1
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""

        
        
