class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort in descending order
        happiness.sort(reverse = True)

        total_happiness_sum = 0
        turns = 0

        # Calculate the maximum happiness sum
        for i in range(k):
            # Adjust happiness and ensure it's not negative
            total_happiness_sum += max(happiness[i] - turns, 0)

            # Increment turns for the next iteration
            turns += 1

        return total_happiness_sum
        
        # below exceeds time limit
        ans = 0
        happiness.sort()

        while k > 0 and happiness:
            ans += happiness.pop()
            happiness = [x - 1 for x in happiness if x > 0]
            k -= 1

        return ans