class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf")] * (amount+1)
        arr[0] = 0

        for coin in coins:
            for currAmt in range(coin, amount+1):
                arr[currAmt] = min(arr[currAmt], arr[currAmt - coin] +1)

        return arr[-1] if arr[-1]!=float("inf") else -1