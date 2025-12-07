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
    
    def getBushCost (account_type, num_bushes):
        each_bush_cost = 10
        sale_for_new = 20/100
        bush_cost = each_bush_cost * num_bushes
        
        if (account_type == "New"):
            bush_cost = bush_cost - (bush_cost*sale_for_new)
        elif (account_type == "Preferred" and num_bushes >= 5):
            bush_cost = bush_cost - 5*each_bush_cost
        return bush_cost
    
    
    def getFlowerBedCost (bed_width, bed_length):
        cost_per_foot = 2
        area = bed_length * bed_width
        area_cost = area * cost_per_foot
        return area_cost
    
    def getFertilCost (fertile_area):
        cost_per_bag = 11
        area_per_bag = 5000
        area_cost = fertile_area / area_per_bag * cost_per_bag
        return area_cost
            
    letter = input("P-Preferred, R-Regular, N-New ")
    num_Bushes = int(input())
    bed_width = int(input())
    bed_length = int(input())
    fertile_area = int(input())
    
    
    
    print ("="*5, end="")
    print ("Falcon Landing", end="")
    print ("="*5, end="")
    
    
    
    
    
main()