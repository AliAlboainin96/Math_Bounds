import os
import time

def cls():
    os.system('Cls ' if os.name =='nt' else 'clear')
def hold():
    time.sleep(999999)
    input()


def main():
    cls()
    main_num = float(input("Enter Main Number: "))

    max_acc = float(input("\nEnter Accuracy: "))

    max_err = max_acc / 2

    main_ub = main_num + max_err
    main_lb = main_num - max_err
    
    main_ux = round(main_ub, 2)
    main_lx = round(main_lb, 2)

    print("\nUpper Bound: {0} \n\nLower Bound: {1}".format(main_ux,main_lx))

    print("\nInquality: \n{0} ≤ n < {1}\n\n\n".format(main_lx,main_ux))

    main_min = main_num - 1
    main_max = main_num + 1

    num_line = ("●","ᴏ")

    print("                ",num_line[0],"--------------------------------",num_line[1])
    print("     .——————————————————————————————————————————————————————————————.")
    print(" ",main_min,"         ",main_lx,"             ",main_num,"            ",main_ux,"            ",main_max)
        


    hold()

def sf_func():

     cls()

     number_input = float(input("Enter Number: "))
     scale_factor = int(input("Enter S.F: "))


     number = round(number_input,scale_factor)
     print(number)

user_input = input("1)Inquality\n2)S.F\n\n")

if user_input == '1':
   main()
     

elif user_input == '2':
    sf_func()
 

            