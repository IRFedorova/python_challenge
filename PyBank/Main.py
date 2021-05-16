#dependancies
import csv

# Files to load and output
file_to_load = "resources/budget_data_1.csv"
file_to_output = "analysis/budget_analysis_1.csv"

# set initial variables
total_months = 0
prev_revenue = 0
month_of_change= []
revenue_change_list = []
greatest_increase  = [ "", 0 ]
greatest_decrease  = [ "", 9999999999 ]
total_revenue = 0

#Read the csv and convert it into a list of dictionaries
with open (file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        
        #Track the totals
        total_months = total_months + 1 
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # track the revenue change
        revenue_change = int(row ["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        
        month_of_change.append(row["Date"])
        revenue_change_list.append(revenue_change)
                
        #Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        #Calculate the greatest decrease 
        if ( revenue_change < greatest_decrease [1] ):
            greatest_decrease[0] = row ["Date"]
            greatest_decrease[1] = revenue_change

#Calculate Average Revenue Change
revenue_avg = round((sum (revenue_change_list ) / len (revenue_change_list)),2)
        
#Create Output Summary
output = (
        f"\nFinancial Analysis\n"
        f"...........................................\n"
        f"Total Months: {total_months}\n"
        f"Total Revenue: ${total_revenue}\n"
        f"Average Revenue Change: {revenue_avg}\n"
        f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
        f"...........................................\n"
        )

#print the output
print(output)

#Export the result to txt file
with open (file_to_output, "w") as txt_file:
            txt_file.write(output)