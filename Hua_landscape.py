# -------------------------------------------------------------------------------
# File Name:    Hua_landscape.py
# Course:       CS 1010 1001
# Class time:   Monday-Wednesday 4:00pm - 5:00pm
#
# Purpose:      The program calculates the cost of landscaping services from input data,
#               such as account type, number of bushes, flower bed dimensions, and lawn square footage.
#
# Author:       Xuan Hua
#
# Due Date:     12/08/2025
# -------------------------------------------------------------------------------

def convertAcct2String(letter): # a function converts account type letter to meaning string
    account_type = None # define the account_type variable as None
    if (letter == "P"):
        account_type = "Preferred"
    elif (letter == "R"):
        account_type = "Regular"
    elif (letter == "N"):
        account_type = "New"
    return account_type

def getBushCost(account_type, num_Bushes): # a function calculates the bush cost based on account type and number of bushes
    each_bush_cost = 10
    sale_for_new = 0.2
    bush_cost = each_bush_cost * num_Bushes

    if (account_type == "New"): # applies discount for new account type
        bush_cost = bush_cost - (bush_cost*sale_for_new)
    elif (account_type == "Preferred" and num_Bushes >= 5): # applies discount for preferred account type with 5 or more bushes
        bush_cost = bush_cost - 5*each_bush_cost
    elif (account_type == "Preferred" and num_Bushes < 5): # applies discount for preferred account type with less than 5 bushes
        bush_cost = bush_cost - num_Bushes * each_bush_cost
    return bush_cost

def getFlowerBedCost (bed_length, bed_width): # a function calculates the flower bed cost based on bed dimensions
    cost_per_foot = 2
    area = bed_length * bed_width
    area_cost = area * cost_per_foot
    return area_cost
    
def getFertilCost (lawn_square_footage): # a function calculates the fertilizer cost based on lawn square footage
    cost_per_bag = 11
    area_per_bag = 5000
    num_bag_need = lawn_square_footage / area_per_bag
    if (lawn_square_footage % area_per_bag != 0): # checks if there is a remainder to round up the number of bags needed
        num_bag_need = int(num_bag_need)
        num_bag_need += 1
    fertile_cost = num_bag_need * cost_per_bag
    return fertile_cost

def main():
    # Get user inputs
    letter = input("Please enter your account type: P-Preferred, R-Regular, N-New: ")
    num_Bushes = int(input("Please enter number of bushes: "))
    bed_length = int(input("Please enter flower bed length: "))
    bed_width = int(input("Please enter flower bed width: "))
    lawn_square_footage = int(input("Please enter lawn square footage: "))
    
    # Calculate the costs by calling the functions
    account_type = convertAcct2String (letter)
    bush_cost = getBushCost (account_type, num_Bushes)
    flower_bed_cost = getFlowerBedCost(bed_length, bed_width)
    fertile_cost = getFertilCost (lawn_square_footage)
    final_cost = bush_cost + flower_bed_cost + fertile_cost
    
    # Display the cost summary
    print (f"{'='*9}Falcon Landing{'='*9}")
    print (f"Account Type: { account_type}")
    print (f"{'Bush cost':<20}${bush_cost:>10.2f}" )
    print (f"{'Flower Bed Cost':<20}${flower_bed_cost:>10.2f}")
    print (f"{'Fertilizer Cost':<20}${fertile_cost:>10.2f}")
    print (f"{'Final Cost':<20}${final_cost:>10.2f}")
    print (f"{'='*31}")
    
main()