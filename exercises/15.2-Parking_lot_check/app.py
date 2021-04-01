parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(park_state):
    state = {
        "total_slots": 0,
        "available_slots": 0,
        "occupied_slots": 0
      }

    for i in range(0,len(park_state)):
        for j in range(0,len(park_state)):
            if park_state[i][j] == 2:
                state["available_slots"] += 1 
                state["total_slots"] += 1
            elif park_state[i][j] == 1:
                state["occupied_slots"] += 1
                state["total_slots"] += 1
    return state

result = get_parking_lot(parking_state)
print(result)