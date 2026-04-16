def SortDec3(A, B, C):
    sorted_list = sorted([A, B, C], reverse=True)
    return sorted_list[0], sorted_list[1], sorted_list[2]

# Sinov
A2, B2, C2 = 3, 9, 1
A2, B2, C2 = SortDec3(A2, B2, C2)
print(f"Kamayish tartibi: {A2}, {B2}, {C2}")