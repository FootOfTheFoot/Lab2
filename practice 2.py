import math
import statistics as st
def main():
    temp=[]
    templist=[]
    min_max=[]
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    bmi=calculate_bmi(weight=57, height=1.73)
    bmi_range(bmi)
    display_main_menu()
    templist=get_user_input()
    print(templist)
    avg=calc_average(templist)
    print(f"Average temperature: {avg}")
    min_max=find_min_max(templist)
    print("Minimum temperature:",min_max[0],"\nMaximum temperature:",min_max[1])
    temp=sort_temperature(templist)
    print(f"Sorted temperature list: {temp}")
    median=calc_median_temperature(temp)
    print(f"Median temperature: {median:.2f}")



def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/math.pow(height,2)
    print(f"BMI: {bmi:.2f}")
    return bmi

def bmi_range(bmi):
    if bmi>25:
        print("Over Weight")
    elif 18.5<=bmi<=25:
        print("Normal Weight")
    else:
        print("Under Weight")

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    value=0
    temp=[]
    while True:
        value=float(input("Press -1 to terminate\nEnter temp:")) 
        if value==-1:
            break 
        temp.append(value)
    return temp

def calc_average(templist):
    sum=0
    for num in templist:
        sum+=num
    avg=sum/(len(templist))
    return avg
    
def find_min_max(templist):
    max=templist[0]
    min=templist[0]
    for num in templist:
        if num>max:
            max=num
        elif num<min:
            min=num
    return [min,max]

def sort_temperature(templist):
    sorted_templist = sorted(templist)
    return sorted_templist

def calc_median_temperature(sorted_templist):
    median=st.median(sorted_templist)
    return median




if __name__=='__main__':
    main()