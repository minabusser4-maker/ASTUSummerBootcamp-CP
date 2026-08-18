class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count, n =  0, len(colors)
        for i in range(n):
            j = (i + 1) % n
            k = (i + 2) % n
            if colors[i] != colors[j] and colors[j] != colors[k]:
                count += 1
        return count
        
