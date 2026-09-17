class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        output = 0
        while k > 0:
            gifts.sort(reverse = True)
            gifts[0] = int(gifts[0] ** 0.5)
            k-=1

        return sum(gifts)

        