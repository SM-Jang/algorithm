
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck_weights = deque(truck_weights)
    for _ in range(bridge_length):
        bridge.append(0)
    time = 0
    cur_weight = 0
    while truck_weights:
        
        time += 1
        out_weight = bridge.popleft()
        cur_weight -= out_weight

        cur = truck_weights[0]

        if cur_weight + cur <= weight:
            out_weight = truck_weights.popleft()
            bridge.append(cur)
            cur_weight += cur 
        else:
            bridge.append(0)

    return time+bridge_length