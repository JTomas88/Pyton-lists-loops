parking_state =  [
  [1,0,1,1,0,1],
  [2,0,1,1,0,1],
  [1,0,2,1,0,1],
  [1,0,1,1,0,1],
  [1,0,1,1,0,2],
  [1,0,1,1,0,1],
]
# 1 ocupado
# 2 disponible
# 0 no cuenta

# Your code here
def get_parking_lot(cochesTotales):
  state={}
  total_slots = 0
  occupied = 0
  available = 0
  notParking = 0
  
  for fila in cochesTotales:
    for hueco in fila:
       if hueco == 0:
          notParking += 1
       elif hueco == 1:
          occupied += 1
       elif hueco == 2:
          available += 1
  
  total_slots = available + occupied + notParking

  state = {
        "total_slots": total_slots,
        "available_slots": available,
        "occupied_slots": occupied
    }

  return state

print(get_parking_lot(parking_state))


# parking_state = [
#   [1,1,1],
#   [0,0,0],
#   [1,1,2]
# ]

# # Your code here
# def get_parking_lot(matrix):
#   state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}
#   for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#       if matrix[i][j] == 1:
#         state["occupied_slots"] += 1
#         state["total_slots"] += 1
#       elif matrix[i][j] == 2:
#         state["available_slots"] += 1
#         state["total_slots"] += 1
#   return state

# get_parking_lot(parking_state)
