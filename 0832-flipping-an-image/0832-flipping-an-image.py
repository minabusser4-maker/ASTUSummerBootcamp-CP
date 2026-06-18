class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            left = 0
            right = len(i)- 1
            while left<=right:
                i[left],i [right]=1-i[right],1-i[left]
                left+=1
                right-=1
    
        return image
        