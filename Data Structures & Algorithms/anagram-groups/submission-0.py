class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupHash = defaultdict(list)

        for s in strs:
            count = [0] * 26 #counter for each letter in the alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
            groupHash[tuple(count)].append(s)
        return list(groupHash.values())

        