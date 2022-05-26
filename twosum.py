from matplotlib.font_manager import json_load


arr = [1,3,5,6,11,23]
sum = 9

def twosum(arr,sum):
    for i in arr:
        for j in arr:
            if(i+j == sum):
                print(i,j)


twosum(arr,sum)