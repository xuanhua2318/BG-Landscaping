def main():
    def convertAcct2String (letter):
        account_type = None
        if (letter == "P"):
            account_type = "Preferred"
        elif (letter == "R"):
            account_type = "Regular"
        elif (letter == "N"):
            account_type = "New"
        return account_type
    
    def getBushCost (account_type, num_Bushes):
        each_bush_cost = 10
        sale_for_new = 0.2
        bush_cost = each_bush_cost * num_Bushes
        
        if (account_type == "New"):
            bush_cost = bush_cost - (bush_cost*sale_for_new)
        elif (account_type == "Preferred" and num_Bushes >= 5):
            bush_cost = bush_cost - 5*each_bush_cost
        elif (account_type == "Preferred" and num_Bushes < 5):
            bush_cost = bush_cost - num_Bushes * each_bush_cost
        return bush_cost
    
    
    def getFlowerBedCost (bed_width, bed_length):
        cost_per_foot = 2
        area = bed_length * bed_width
        area_cost = area * cost_per_foot
        return area_cost
    
    def getFertilCost (fertile_area):
        cost_per_bag = 11
        area_per_bag = 5000
        num_bag_need = fertile_area / area_per_bag
        if (fertile_area % area_per_bag != 0):
            num_bag_need = int(num_bag_need)
            num_bag_need += 1
        fertile_cost = num_bag_need * cost_per_bag
        return fertile_cost
         
    letter = input("Please enter your account type: P-Preferred, R-Regular, N-New: ")
    num_Bushes = int(input("Please enter number of bushes: "))
    bed_width = int(input("Please enter bed width: "))
    bed_length = int(input("Please enter bed length: "))
    fertile_area = int(input("Please enter fertile area: "))
    
    account_type = convertAcct2String (letter)
    bush_cost = getBushCost (account_type, num_Bushes)
    flower_bed_cost = getFlowerBedCost(bed_width, bed_length)
    fertile_cost = getFertilCost (fertile_area)
    final_cost = bush_cost + flower_bed_cost + fertile_cost
    
    
    print (f"{'='*9}Falcon Landing{'='*9}")
    print (f"Account Type: { account_type}")
    print (f"{'Bush cost':<20}${bush_cost:>10.2f}" )
    print (f"{'Flower Bed Cost':<20}${flower_bed_cost:>10.2f}")
    print (f"{'Fertilizer Cost':<20}${fertile_cost:>10.2f}")
    print (f"{'Final Cost':<20}${final_cost:>10.2f}")
    print (f"{'='*31}")
    
main()