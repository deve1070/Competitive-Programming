class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        alice= len(piles)-1
        me=alice-1
        bob=0
        maxCoin=0
        while bob < me:
            maxCoin +=piles[me]
            alice -=2
            me =alice -1
            bob +=1
        return maxCoin

        """
        :type piles: List[int]
        :rtype: int
        """
        