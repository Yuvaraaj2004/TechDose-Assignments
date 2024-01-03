class Solution:
    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        inter.sort()
        print(inter)

        def dp(ind=0, end=-1):
            # print(ind,end)
            if ind == len(inter):
                return -float('inf')
            elif end != -1 and end < inter[ind][0]:
                return -float('inf')
            else:
                dp(ind+1)
                while ind+1 < len(inter) and inter[ind+1][1] < inter[ind][1]:
                    # print(ind,inter[ind+1])
                    inter.pop(ind+1)
                if dp(ind+1, inter[ind][1]) >= inter[ind][1]:
                    inter[ind][1] = inter.pop(ind+1)[1]
                return inter[ind][1]
        dp()
        return inter
