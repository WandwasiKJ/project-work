# calculating the area of a rectangle
def calc_area_rect():
    L = 8
    W = 4
    A = L*W
    print(f"the area of the rectangle is {A}")

calc_area_rect()


def calc_area_rect(len_rec, width_rec):
     L = 8
     W = 4
     A = L*W
     return A

Area_rect=calc_area_rect(10,3) #pass parameters

print(f"the area of the rectangle is {Area_rect}")

def cal_comp_pay ( hours,rate):
     H= hours
     R= rate 
     P= H*R
     return P

comp_pay= cal_comp_pay(45,10)

print(f"the company pay is {comp_pay}")