class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time = 0
        current_time = 0
        
        for arrival, time_needed in customers:
            if current_time < arrival:
                current_time = arrival
            current_time += time_needed
            # print(current_time - arrival) [3, 3, 7, 6, 4, 2]
            total_wait_time += current_time - arrival
        
        return total_wait_time / len(customers)

        # wrong
        # [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
        # expected 4.17
        # output 3.33 [3, 2, 6, 5, 3, 1]
        # cnt_customers = len(customers)
        # start = customers[0][0]
        # wait_time = []

        for i in range(cnt_customers):

            start = start + customers[i][1]
            if start > customers[i][0]:
                wait = start - customers[i][0]
                wait_time.append(wait)
            else:
                wait_time.append(customers[i][1])
            print(wait_time)

        # return sum(wait_time) / cnt_customers

        # Sol 2
        # cnt_customers = len(customers)
        # current_time = 0
        # total_wait_time = 0

        # for i in range(cnt_customers):
        #     arrival = customers[i][0]
        #     time_needed = customers[i][1]

        #     if current_time < arrival:
        #         current_time = arrival
        #     current_time += time_needed
        #     total_wait_time += current_time - arrival

        # return total_wait_time / cnt_customers