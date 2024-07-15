class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        candidates = []

        if sum(cost) > sum(gas):
            return -1

        # for gas_available,gas_needed_for_next_station in zip(gas, cost):

        #     if gas_available > gas_needed_for_next_station:
        #         candidates.append(gas_available)
        def check(candidate):
            current_gas = gas[candidate] - cost[candidate]
            itr = candidate
            #print(f"{current_gas=} {itr=}")
            counter = 0
            while counter<len(gas) and current_gas>=0:
                itr = itr+1
                itr = itr%len(gas)
                #print(f"{itr=} {candidate=} {current_gas=}")
                current_gas = current_gas + gas[itr] - cost[itr]
                counter = counter+1

            #print(f"Gas remaning {current_gas=}")
            if current_gas>=0:
                return True,candidate
            return False,itr

        num_items = len(gas)
        item = 0
        candidates = []
        while item < num_items:
            
            gas_available = gas[item]
            gas_needed_for_next_station = cost[item]

            if gas_available >= gas_needed_for_next_station:
                status,idx = check(item)
                if status:
                    return idx
                else:
                    item=idx
        
            item+=1
        #print(candidates)
        
        return -1




        