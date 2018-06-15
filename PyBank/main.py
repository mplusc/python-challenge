import os
import csv

#CHANGE FILES WHEN ANALZYING DIFFERENT EXCEL FILES
csvpath_1 = os.path.join('raw_data','budget_data_1.csv')
output_file = os.path.join("budget_data.txt")


with open(csvpath_1,newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    
    total_months = 0
    total = 0
    month_change = []
    net_change_list = []
    prev_net = 0
    increase = ["",0]
    decrease = ["",1000000000000000]
    
    
    for row in csv_reader:
        total_months = total_months + 1
        total += int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list= net_change_list + [net_change]
        rev= sum(net_change_list) / len(net_change_list)
        month_change = month_change + [row[0]]
        
        if (net_change > increase[1]):
            increase[0] = row[0]
            increase[1] = net_change
            
        if (net_change < decrease[1]):
            decrease[0] = row[0]
            decrease[1] = net_change
           
output = (
print("------------------------------------------------"),
print("Financial Analysis"),
print("Total Months: " + str(total_months)),
print("Total Revenue: $" + str(total)),
print("Average Revenue Change: $" +str(rev)),
print("Greatest Increase in Revenue: "+ str(increase[0]) + " $" + str(increase[1])),
print("Greatest Decrease in Revenue: "+ str(decrease[0]) + " $" + str(decrease[1]))) 


with open(output_file,"w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write("------------------------------------------------"+ '\n')
    csvfile.write("Financial Analysis"+ '\n')
    csvfile.write("Total Months: " + str(total_months)+ '\n')
    csvfile.write("Total Revenue: $" + str(total)+ '\n')
    csvfile.write("Average Revenue Change: $" +str(rev)+ '\n')
    csvfile.write("Greatest Increase in Revenue: "+ str(increase[0]) + " $" + str(increase[1])+ '\n')
    csvfile.write("Greatest Decrease in Revenue: "+ str(decrease[0]) + " $" + str(decrease[1])+ '\n')


####Data File 2
csvpath_2 = os.path.join('raw_data','budget_data_2.csv')
output_file = os.path.join("budget_data.txt")


with open(csvpath_2,newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    
    total_months = 0
    total = 0
    month_change = []
    net_change_list = []
    prev_net = 0
    increase = ["",0]
    decrease = ["",1000000000000000]
    
    
    for row in csv_reader:
        total_months = total_months + 1
        total += int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list= net_change_list + [net_change]
        rev= sum(net_change_list) / len(net_change_list)
        month_change = month_change + [row[0]]
        
        if (net_change > increase[1]):
            increase[0] = row[0]
            increase[1] = net_change
            
        if (net_change < decrease[1]):
            decrease[0] = row[0]
            decrease[1] = net_change
           
output = (
print("------------------------------------------------"),
print("Financial Analysis"),
print("Total Months: " + str(total_months)),
print("Total Revenue: $" + str(total)),
print("Average Revenue Change: $" +str(rev)),
print("Greatest Increase in Revenue: "+ str(increase[0]) + " $" + str(increase[1])),
print("Greatest Decrease in Revenue: "+ str(decrease[0]) + " $" + str(decrease[1]))) 


with open(output_file,"a") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write("------------------------------------------------"+ '\n')
    csvfile.write("Financial Analysis"+ '\n')
    csvfile.write("Total Months: " + str(total_months)+ '\n')
    csvfile.write("Total Revenue: $" + str(total)+ '\n')
    csvfile.write("Average Revenue Change: $" +str(rev)+ '\n')
    csvfile.write("Greatest Increase in Revenue: "+ str(increase[0]) + " $" + str(increase[1])+ '\n')
    csvfile.write("Greatest Decrease in Revenue: "+ str(decrease[0]) + " $" + str(decrease[1])+ '\n')
    