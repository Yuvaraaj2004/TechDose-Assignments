class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        a, res = 0, []
        for i in range(len(encoded)+2):
            a ^= i
            if i < len(encoded)+1 and i % 2 == 1:
                a ^= encoded[i]

        res.append(a)
        for i in range(len(encoded)):

            res.append(res[-1] ^ encoded[i])
        return res
