class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_res = ""

        for i in strs:
            encode_res += str(len(i))
            encode_res += '#'
            encode_res += i
        return encode_res

    def decode(self, s: str) -> List[str]:
        decode_res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decode_res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decode_res
            
