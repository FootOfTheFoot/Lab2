import math

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    bmi=calculate_bmi(weight=57, height=1.73)
    bmi_range(bmi)


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/math.pow(height,2)
    print(f"BMI: {bmi:.2f}")
    return bmi

def bmi_range(bmi):
    if bmi>25:
        print("Over Weight")
    elif 18.5<bmi<=25:
        print("Normal Weight")
    else:
        print("Under Weight")
    
if __name__=='__main__':
    main()