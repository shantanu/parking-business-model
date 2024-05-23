def get_locations(
    months,
    num_partners, 
    max_locations_per_partner, 
    months_between_partners, 
    months_between_location_for_partner, 
    first_month_of_location_for_partner,
    location_license_fee,
    gateway_license_fee,
    camera_license_fee,
    num_gateways_per_location,
    num_cameras_per_gateway
   ):
    
    new_locations = [0]*months
    new_partners = [0]*months
    location_license_fees = [0]*months
    gateway_license_fees = [0]*months
    cameras_license_fees = [0]*months
    cumulative_gateways = [0]*months
    cumulative_cameras = [0]*months

    for partner in range(num_partners):
        month_started = 4 + months_between_partners*partner
        if month_started >= months:
            break
        
        new_partners[month_started] += 1
        
        for new_location in range(max_locations_per_partner):
            new_location_month = month_started + first_month_of_location_for_partner + months_between_location_for_partner*new_location
            
            if new_location_month >= months:
                break
            
            new_locations[new_location_month] += 1 
            
            for m in range(new_location_month, months):
                location_license_fees[m] += location_license_fee
                gateway_license_fees[m] += gateway_license_fee * num_gateways_per_location
                cameras_license_fees[m] += camera_license_fee * num_cameras_per_gateway * num_gateways_per_location
    cumulative_partners = [0]*months
    for i in range(1, months):
        cumulative_partners[i] = cumulative_partners[i-1] + new_partners[i]
        
    cumulative_locations = [0]*months
    cumulative_location_license_fees = [0]*months
    cumulative_gateway_license_fees = [0]*months
    cumulative_cameras_license_fees = [0]*months
    for i in range(1, months):
        cumulative_locations[i] = cumulative_locations[i-1] + new_locations[i]
        cumulative_gateways[i] = cumulative_gateways[i-1] + num_gateways_per_location*new_locations[i]
        cumulative_cameras[i] = cumulative_cameras[i-1] + num_cameras_per_gateway*num_gateways_per_location*new_locations[i]
        cumulative_location_license_fees[i] = cumulative_location_license_fees[i-1] + location_license_fees[i]
        cumulative_gateway_license_fees[i] = cumulative_gateway_license_fees[i-1] + gateway_license_fees[i]
        cumulative_cameras_license_fees[i] = cumulative_cameras_license_fees[i-1] + cameras_license_fees[i]
    total_license_fee = [0]*months
    for i in range(1, months):
        total_license_fee[i] = cumulative_location_license_fees[i] + cumulative_gateway_license_fees[i] + cumulative_cameras_license_fees[i]
        
    return (
        new_partners, 
        cumulative_partners, 
        new_locations, 
        cumulative_locations, 
        cumulative_location_license_fees, 
        cumulative_gateway_license_fees,
        cumulative_cameras_license_fees,
        cumulative_gateways,
        cumulative_cameras,
        total_license_fee
    )


# Starter Model Parameters
months = 84
num_partners_starter = 50
max_locations_per_partner_starter = 10
months_between_partners_starter = 1
months_between_location_for_partner_starter = 3
first_month_of_location_for_partner_starter = 3
location_license_fee_starter = 350  # $350 per month per location for Starter Model
gateway_license_fee_starter = 75    # $75 per month per gateway for Starter Model
num_gateways_per_location_starter = 10  # 10 gateways per location for Starter Model
cameras_license_fee_starter = 0 #$0.75 per month per Cameras for Starter Model
num_cameras_per_gateway_starter = 30 # 80 cameras per gateway for Starter Model

# Call the function for the Starter Model
starter_model_output = get_locations(
    months,
    num_partners_starter, 
    max_locations_per_partner_starter, 
    months_between_partners_starter, 
    months_between_location_for_partner_starter, 
    first_month_of_location_for_partner_starter,
    location_license_fee_starter,
    gateway_license_fee_starter,
    cameras_license_fee_starter,
    num_gateways_per_location_starter,
    num_cameras_per_gateway_starter)

# Unpack the output for the Starter Model
(
    new_partners_starter, 
    cumulative_partners_starter, 
    new_locations_starter, 
    cumulative_locations_starter, 
    cumulative_location_license_fees_starter, 
    cumulative_gateway_license_fees_starter,
    cumulative_cameras_license_fees_starter,
    cumulative_gateways_starter,
    cumulative_cameras_starter,
    total_license_fee_starter,
   
) = starter_model_output


# Advanced Model Parameters
num_partners_advanced = 40
max_locations_per_partner_advanced = 40
months_between_partners_advanced = 2
months_between_location_for_partner_advanced = 3
first_month_of_location_for_partner_advanced = 3
location_license_fee_advanced = 200  # $200 per month per location for Advanced Model
gateway_license_fee_advanced = 50    # $50 per month per gateway for Advanced Model
num_gateways_per_location_advanced = 12  # 15 gateways per location for Advanced Model
cameras_license_fee_advanced = 0 #$0.75 per month per Cameras for Starter Model
num_cameras_per_gateway_advanced = 50 # 80 cameras per gateway for Starter Model

# Call the function for the Advanced Model
advanced_model_output = get_locations(
    months,
    num_partners_advanced, 
    max_locations_per_partner_advanced,
    months_between_partners_advanced, 
    months_between_location_for_partner_advanced, 
    first_month_of_location_for_partner_advanced,
    location_license_fee_advanced,
    gateway_license_fee_advanced,
    cameras_license_fee_advanced,
    num_gateways_per_location_advanced,
    num_cameras_per_gateway_advanced)

# Unpack the output for the Advanced Model
(
    new_partners_advanced, 
    cumulative_partners_advanced, 
    new_locations_advanced, 
    cumulative_locations_advanced, 
    cumulative_location_license_fees_advanced, 
    cumulative_gateway_license_fees_advanced,
    cumulative_cameras_license_fees_advanced,
    cumulative_gateways_advanced,
    cumulative_cameras_advanced,
    total_license_fee_advanced
) = advanced_model_output



# Enterprise Model Parameters
num_partners_enterprise = 10
max_locations_per_partner_enterprise = 75
months_between_partners_enterprise = 1
months_between_location_for_partner_enterprise = 2
first_month_of_location_for_partner_enterprise = 3
location_license_fee_enterprise = 100  # $100 per month per location for Enterprise Model
gateway_license_fee_enterprise = 25    # $25 per month per gateway for Enterprise Model
num_gateways_per_location_enterprise = 20  # 20 gateways per location for Enterprise Model
cameras_license_fee_enterprise = 0 #$0.75 per month per Cameras for Starter Model
num_cameras_per_gateway_enterprise = 80 # 80 cameras per gateway for Starter Model

# Call the function for the Enterprise Model
enterprise_model_output = get_locations(
    months,
    num_partners_enterprise, 
    max_locations_per_partner_enterprise, 
    months_between_partners_enterprise, 
    months_between_location_for_partner_enterprise, 
    first_month_of_location_for_partner_enterprise,
    location_license_fee_enterprise,
    gateway_license_fee_enterprise,
    cameras_license_fee_enterprise,
    num_gateways_per_location_enterprise,
    num_cameras_per_gateway_enterprise)

# Unpack the output for the Enterprise Model
(
    new_partners_enterprise, 
    cumulative_partners_enterprise, 
    new_locations_enterprise, 
    cumulative_locations_enterprise, 
    cumulative_location_license_fees_enterprise, 
    cumulative_gateway_license_fees_enterprise,
    cumulative_cameras_license_fees_enterprise,
    cumulative_gateways_enterprise,
    cumulative_cameras_enterprise,
    total_license_fee_enterprise
) = enterprise_model_output


cost_per_month = 150000
cumulative_costs = [0]*months

for i in range(1, months):
    cumulative_costs[i] = cost_per_month + cumulative_costs[i-1]
print("TOTAL CUMULATIVE COSTS: ", cumulative_costs)


total_license_fee_per_month_sum_all_models = [0] * months
for i in range(months):
    total_license_fee_per_month_sum_all_models[i] = \
        total_license_fee_starter[i] \
        + total_license_fee_advanced[i] \
        + total_license_fee_enterprise[i]

print("TOTAL LICENSE FEE MONTHLY ALL MODELS: ", total_license_fee_per_month_sum_all_models)

total_cumulative_license_fee_all_models = [0] * months
for i in range(1, months):
    total_cumulative_license_fee_all_models[i] = total_license_fee_per_month_sum_all_models[i] + total_license_fee_per_month_sum_all_models[i-1]
print("TOTAL CUMULATIVE LICENSE FEE ALL MODELS: ", total_cumulative_license_fee_all_models)



sales_commission_rate = 0.15
sales_commission_per_month = [0]*months

for i in range(1, months):
    sales_commission_per_month[i] = total_license_fee_per_month_sum_all_models[i] * sales_commission_rate
    
print("SALES COMMISSION PER MONTH: ", sales_commission_per_month)

total_cumulative_sales_commission = [0] * months
for i in range (1, months):
    total_cumulative_sales_commission[i] = sales_commission_per_month[i] + sales_commission_per_month[i-1]
print("TOTAL CUMULATIVE SALES COMMISSION: ", total_cumulative_sales_commission)



cash_flow_per_month = [0]*months

for i in range(months):
    cash_flow_per_month[i] = total_license_fee_per_month_sum_all_models[i] - sales_commission_per_month[i] - cost_per_month
print("CASH FLOW PER MONTH: ", cash_flow_per_month)


total_cumulative_cash_flow = [0] * months
total_cumulative_cash_flow[0] = cash_flow_per_month[0]
for i in range (1, months):
    total_cumulative_cash_flow[i] = cash_flow_per_month[i] + cash_flow_per_month[i-1]
    
print("TOTAL CUMULATIVE CASH FLOW : ", total_cumulative_cash_flow)






def discount(amount, rate, years):
    return (amount / ((1 + rate)**years))
    
years = months//12
valuation_per_year = [0]*years

rate = .10


    
    
for year in range(1, years+1):
    valuation_per_year[year-1] = discount(total_cumulative_cash_flow[year*12-1], rate, year)    
    

print("VALUATION PER YEAR: ", [ f'${round(elem):,}' for elem in valuation_per_year ])

print("===================")
print()

# Print the output for the Starter Model
print("STARTER MODEL OUTPUT")
print("New Partners:", new_partners_starter)
print("Cumulative Partners:", cumulative_partners_starter)
print("New Locations:", new_locations_starter)
print("Cumulative Locations:", cumulative_locations_starter)
print("Cumulative Gateways:", cumulative_gateways_starter)
print("Cumulative Cameras:", cumulative_cameras_starter)
print("Cumulative License Fees for Location:", cumulative_location_license_fees_starter)
print("Cumulative License Fees for Gateway:", cumulative_gateway_license_fees_starter)
print("Cumulative License Fees for Cameras:", cumulative_cameras_license_fees_starter)
print("Total License Fee STARTER:", total_license_fee_starter)
print()

# Print the output for the Advanced Model
print("ADVANCED MODEL OUTPUT")
print("New Partners:", new_partners_advanced)
print("Cumulative Partners:", cumulative_partners_advanced)
print("New Locations:", new_locations_advanced)
print("Cumulative Locations:", cumulative_locations_advanced)
print("Cumulative Gateways:", cumulative_gateways_advanced)
print("Cumulative Cameras:", cumulative_cameras_advanced)
print("Cumulative License Fees for Location:", cumulative_location_license_fees_advanced)
print("Cumulative License Fees for Gateway:", cumulative_gateway_license_fees_advanced)
print("Cumulative License Fees for Cameras:", cumulative_cameras_license_fees_advanced)
print("Total License Fee ADVANCED:", total_license_fee_advanced)
print()

# Print the output for the Enterprise Model
print("ENTERPRISE MODEL OUTPUT")
print("New Partners:", new_partners_enterprise)
print("Cumulative Partners:", cumulative_partners_enterprise)
print("New Locations:", new_locations_enterprise)
print("Cumulative Locations:", cumulative_locations_enterprise)
print("Cumulative Gateways:", cumulative_gateways_enterprise)
print("Cumulative Cameras:", cumulative_cameras_enterprise)
print("Cumulative License Fees for Location:", cumulative_location_license_fees_enterprise)
print("Cumulative License Fees for Gateway:", cumulative_gateway_license_fees_enterprise)
print("Cumulative License Fees for Cameras:", cumulative_cameras_license_fees_enterprise)
print("Total License Fee ENTERPRISE:", total_license_fee_enterprise)







#New code on 5/1/24
import pandas as pd

# Define the data for each DataFrame
data = {
    "Total Cumulative Costs": cumulative_costs,
    "Total License Fee Monthly (All Models)": total_license_fee_per_month_sum_all_models,
    "Total Cumulative License Fee (All Models)": total_cumulative_license_fee_all_models,
    "Sales Commission Per Month": sales_commission_per_month,
    "Total Cumulative Sales Commission": total_cumulative_sales_commission,
    "Cash Flow Per Month": cash_flow_per_month,
    "Total Cumulative Cash Flow": total_cumulative_cash_flow
}

# Create DataFrames
df_total_cumulative_costs = pd.DataFrame(data["Total Cumulative Costs"], columns=["Total Cumulative Costs"])
df_total_license_fee_monthly = pd.DataFrame(data["Total License Fee Monthly (All Models)"], columns=["Total License Fee Monthly (All Models)"])
df_total_cumulative_license_fee = pd.DataFrame(data["Total Cumulative License Fee (All Models)"], columns=["Total Cumulative License Fee (All Models)"])
df_sales_commission_per_month = pd.DataFrame(data["Sales Commission Per Month"], columns=["Sales Commission Per Month"])
df_total_cumulative_sales_commission = pd.DataFrame(data["Total Cumulative Sales Commission"], columns=["Total Cumulative Sales Commission"])
df_cash_flow_per_month = pd.DataFrame(data["Cash Flow Per Month"], columns=["Cash Flow Per Month"])
df_total_cumulative_cash_flow = pd.DataFrame(data["Total Cumulative Cash Flow"], columns=["Total Cumulative Cash Flow"])

# Define the data for each DataFrame
data_starter = {
    "New Partners (Starter)": new_partners_starter,
    "Cumulative Partners (Starter)": cumulative_partners_starter,
    "New Locations (Starter)": new_locations_starter,
    "Cumulative Locations (Starter)": cumulative_locations_starter,
    "Cumulative Gateways (Starter)": cumulative_gateways_starter,
    "Cumulative Cameras (Starter)": cumulative_cameras_starter,
    "Cumulative Location License Fees (Starter)": cumulative_location_license_fees_starter,
    "Cumulative Gateway License Fees (Starter)": cumulative_gateway_license_fees_starter,
    "Cumulative Cameras License Fees (Starter)": cumulative_cameras_license_fees_starter,
    "Total License Fee (Starter)": total_license_fee_starter
}

data_advanced = {
    "New Partners (Advanced)": new_partners_advanced,
    "Cumulative Partners (Advanced)": cumulative_partners_advanced,
    "New Locations (Advanced)": new_locations_advanced,
    "Cumulative Locations (Advanced)": cumulative_locations_advanced,
    "Cumulative Gateways (Advanced)": cumulative_gateways_advanced,
    "Cumulative Cameras (Advanced)": cumulative_cameras_advanced,
    "Cumulative Location License Fees (Advanced)": cumulative_location_license_fees_advanced,
    "Cumulative Gateway License Fees (Advanced)": cumulative_gateway_license_fees_advanced,
    "Cumulative Cameras License Fees (Advanced)": cumulative_cameras_license_fees_advanced,
    "Total License Fee (Advanced)": total_license_fee_advanced
}

data_enterprise = {
    "New Partners (Enterprise)": new_partners_enterprise,
    "Cumulative Partners (Enterprise)": cumulative_partners_enterprise,
    "New Locations (Enterprise)": new_locations_enterprise,
    "Cumulative Locations (Enterprise)": cumulative_locations_enterprise,
    "Cumulative Gateways (Enterprise)": cumulative_gateways_enterprise,
    "Cumulative Cameras (Enterprise)": cumulative_cameras_enterprise,
    "Cumulative Location License Fees (Enterprise)": cumulative_location_license_fees_enterprise,
    "Cumulative Gateway License Fees (Enterprise)": cumulative_gateway_license_fees_enterprise,
    "Cumulative Cameras License Fees (Enterprise)": cumulative_cameras_license_fees_enterprise,
    "Total License Fee (Enterprise)": total_license_fee_enterprise
}

# Define the data for valuation per year
valuation_data = {
    "Year": list(range(1, years+1)),
    "Valuation": valuation_per_year
}

# Round each value in the valuation_per_year list to 0 decimal places
for i in range(len(valuation_per_year)):
    valuation_per_year[i] = round(valuation_per_year[i], 0)



# Create DataFrame
df_valuation_per_year = pd.DataFrame(valuation_data)


# Create DataFrames
df_starter = pd.DataFrame(data_starter)
df_advanced = pd.DataFrame(data_advanced)
df_enterprise = pd.DataFrame(data_enterprise)

# Concatenate all DataFrames vertically
df_partner_business_model = pd.concat([df_starter,
                                       df_advanced,
                                       df_enterprise,
                                       df_total_cumulative_costs, 
                                       df_total_license_fee_monthly,
                                       df_total_cumulative_license_fee,
                                       df_sales_commission_per_month,
                                       df_total_cumulative_sales_commission,
                                       df_cash_flow_per_month,
                                       df_total_cumulative_cash_flow,
                                       df_valuation_per_year], axis=1)

# Write the concatenated DataFrame to a CSV file
df_partner_business_model.to_csv("Partner_Business_Model.csv", index=False)

print("All DataFrames have been successfully combined and written to 'Partner_Business_Model.csv'.")