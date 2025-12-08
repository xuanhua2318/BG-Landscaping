def main():
    def convertAcct2String (letter):
        account_type = None
        if (letter == "P"):
            account_type = "Preferred"
        elif (letter == "R"):
            account_type = "Regular"
        elif (letter == "N"):
            account_type = "Name"
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
        if (fertile_area & area_per_bag != 0):
            num_bag_need = int(num_bag_need)
            num_bag_need += 1
        fertile_cost = num_bag_need * cost_per_bag
        return fertile_cost
         
    letter = input("P-Preferred, R-Regular, N-New ")
    num_Bushes = int(input())
    bed_width = int(input())
    bed_length = int(input())
    fertile_area = int(input())
    
    account_type = convertAcct2String (letter)
    bush_cost = getBushCost (account_type, num_Bushes)
    flower_bed_cost = getFlowerBedCost(bed_width, bed_length)
    fertile_cost = getFertilCost (fertile_area)
    final_cost = bush_cost + flower_bed_cost + fertile_cost
    
    
    print (f"{'='*5}Falcon Landing{'='*5}")
    print (f"Account Type: { account_type}")
    print (f"{'Bush cost':<15}${bush_cost:<15.2f}" )
    print (f"{'Flower Bed Cost':<15}${flower_bed_cost:<15.2f}")
    print (f"{'Fertilizer Cost':<15}${fertile_cost:<15.2f}")
    print (f"{'Final Cost':<15}${final_cost:<15.2f}")
    
main()