def solution(bridge_length, weight, truck_weights):
    tic = 0
    queue = []
    total_weight = 0

    while truck_weights or queue:
        tic += 1

        if queue and tic - queue[0][1] == bridge_length:
            truck, _ = queue.pop(0)
            total_weight -= truck      

        if truck_weights and total_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            queue.append([truck, tic])
            total_weight += truck

    return tic