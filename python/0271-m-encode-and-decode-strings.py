# https://leetcode.com/problems/encode-and-decode-strings/
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        if len(strs) == 1 and not len(strs[0]):
            return "tsbalwes"

        encoded = ""
        for i, s in enumerate(strs):
            if not len(s):
                encoded += "tsbalwes"
                
            for j, c in enumerate(s):
                encoded += str(ord(c))
                if j != len(s)-1:
                    encoded += "-"
            if i != len(strs)-1:
                encoded += ","

        return encoded

    def decode(self, s: str) -> List[str]:
        if not len(s):
            return []
        if s == "tsbalwes":
            return [""]

        decoded = []
        for encoded in s.split(","):
            word = ""
            if encoded != "tsbalwes":
                for asc in encoded.split("-"):
                    word += chr(int(asc))
            decoded.append(word)
        return decoded

# Runner and test cases
def test_encode_decode():
    solution = Solution()

    # Test case 1
    strs = ["hello", "world"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    # Test case 2
    strs = [""]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    # Test case 3
    strs = ["", "a", "ab", "abc"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    # Test case 4
    strs = ["123", "456", "789"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    # Test case 5
    strs = ["!@#", "$%^", "&*()"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    # Test case 6
    strs = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    assert decoded == strs

    print("All test cases passed!")

if __name__ == "__main__":
    test_encode_decode()
