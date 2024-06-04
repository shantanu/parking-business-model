from model_params import *

from model import (
    get_locations,
    print_model_output
)

from costs import (
    get_costs
)
from sales import get_sales_commission
from valuation import get_cash_flow, format_money, get_yearly_valuation

from itertools import accumulate


MONTHS: int = 60
FIXED_COST: int = 100000
SALES_COMMISSION: float = .25
DISCOUNT_RATE: float = .10


# Parking Operator Model Parameters
parking_operator_model_params: ModelParams = ModelParams(
    months=MONTHS,
    location_model_params=GrowthModelParams(
        first_six_months_locations=5,
        next_six_months_locations=12,
        total_locations=2500,
    ),
    pricing_params=PricingParams(
        location_license_fee=350,
        gateway_license_fee=75,
        camera_license_fee=0.75
    ),
    gateways_per_location=10,
    cameras_per_gateway=30
)

# Call the function for the Parking Operator Model
parking_operator_model_output = get_locations(parking_operator_model_params)

# Starter Model Parameters
starter_model_params: ModelParams = ModelParams(
    months = MONTHS,
    gateways_per_location = 5,
    cameras_per_gateway = 30,
    partner_params=PartnerParams(
        num_partners=5,
        max_locations=10,
        months_between_partners=1
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3,
        months_between_location=5
    ),
    pricing_params=PricingParams(
        location_license_fee = 500,
        gateway_license_fee = 100,
        camera_license_fee = 0
    )
)

starter_model_output = get_locations(starter_model_params)

# Advanced Model Parameters
advanced_model_params: ModelParams = ModelParams(
    months = MONTHS,
    gateways_per_location = 10,
    cameras_per_gateway = 70,
    partner_params=PartnerParams(
        num_partners=10,
        max_locations=25,
        months_between_partners=2
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3,
        months_between_location=3
    ),
    pricing_params=PricingParams(
        location_license_fee = 350,
        gateway_license_fee = 75,
        camera_license_fee = 0
    )
)

advanced_model_output = get_locations(advanced_model_params)

# Enterprise Model Parameters
enterprise_model_params: ModelParams = ModelParams(
    months = MONTHS,
    gateways_per_location = 15,
    cameras_per_gateway = 100,
    partner_params=PartnerParams(
        num_partners=5,
        max_locations=40,
        months_between_partners=1
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3,
        months_between_location=3
    ),
    pricing_params=PricingParams(
        location_license_fee = 200,
        gateway_license_fee = 50,
        camera_license_fee = 0
    )
)

enterprise_model_output = get_locations(enterprise_model_params)



print("===================")
print()




print_model_output("PARKING OPERATOR", parking_operator_model_output)

print_model_output("STARTER", starter_model_output)

print_model_output("ADVANCED", advanced_model_output)

print_model_output("ENTERPRISE", enterprise_model_output)


print("===================")
print()

cost_params: CostParams = CostParams(
    cost_per_month=100000
)

cost_per_month = get_costs(cost_params, MONTHS)
cumulative_costs = accumulate(cost_per_month)
print("TOTAL CUMULATIVE COSTS: ", list(cumulative_costs))


total_license_fee_per_month_sum = [
    sum(x) for x in zip(
        starter_model_output.total_license_fee,
        advanced_model_output.total_license_fee,
        enterprise_model_output.total_license_fee
)]
print("TOTAL LICENSE FEE MONTHLY ALL MODELS: ", total_license_fee_per_month_sum)

total_cumulative_license_fee_all_models = list(accumulate(total_license_fee_per_month_sum))
print("TOTAL CUMULATIVE LICENSE FEE ALL MODELS: ", total_cumulative_license_fee_all_models)




sales_params: SalesParams = SalesParams(
    commission_rate=SALES_COMMISSION
)

sales_commission_per_month = get_sales_commission(sales_params, total_license_fee_per_month_sum)
print("SALES COMMISSION PER MONTH: ", sales_commission_per_month)

total_cumulative_sales_commission = list(accumulate(sales_commission_per_month))
print("TOTAL CUMULATIVE SALES COMMISSION: ", total_cumulative_sales_commission)



cash_flow_per_month = [
    get_cash_flow(fee, commission, cost) for fee, commission, cost 
        in zip(
            total_license_fee_per_month_sum,
            sales_commission_per_month,
            cost_per_month
        )
]

print("CASH FLOW PER MONTH: ", cash_flow_per_month)


total_cumulative_cash_flow = list(accumulate(cash_flow_per_month))   
print("TOTAL CUMULATIVE CASH FLOW : ", total_cumulative_cash_flow)




valuation_params: ValuationParams = ValuationParams(
    years=MONTHS//12,
    discount_rate=DISCOUNT_RATE
)

valuation_per_year = get_yearly_valuation(valuation_params, total_cumulative_cash_flow)

print("VALUATION PER YEAR: ", [ format_money(elem) for elem in valuation_per_year ])






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
"""
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
"""
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