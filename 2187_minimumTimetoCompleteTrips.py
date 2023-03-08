# initialize l to 1, and r to the minimum time required to complete any task umltiplied by totalTrips.
# This is because the minimum time required to complete all tasks must be greater or equal to
# the minimum time required to complete any sigle task multipled by the number of tasks to be completed.

class Solution:
  def minimumTime(self, time: List[int], totalTrips: int) -> int:
    # Initialize the search range for minimum completion time
    l = 1
    r = min(time) * totalTrips

    # Binary search for minimum completion time
    while l < r:
      # Calculate the midpoint of the search range
      m = (l + r) // 2
      # Count the number of tasks that can be completed within m time
      if sum(m // t for t in time) >= totalTrips:
        # If enough tasks can be completed within m time, search for smaller time
        r = m
      else:
        # If not enough tasks can be completed within m time, search for larger time
        l = m + 1

    # Return the minimum completion time
    return l