class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        result_dict = defaultdict(list)

        for string_value in strs:
            count_array = [0] * 26

            for c in string_value:
                count_array[ord(c) - ord("a")] += 1

            result_dict[tuple(count_array)].append(string_value)

        return result_dict.values()     



        
