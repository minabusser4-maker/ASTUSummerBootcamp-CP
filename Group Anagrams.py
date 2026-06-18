class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(dict)
        for i in strs:
            key=''.join(sorted(i))
            if key not in my_dict:
                my_dict[key]=[]
            my_dict[key].append(i)
        return list(my_dict.values())





        
