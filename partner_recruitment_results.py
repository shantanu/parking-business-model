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
from export import model_output_to_dataframe

from itertools import accumulate
import pandas as pd


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
cumulative_costs = list(accumulate(cost_per_month))
print("TOTAL CUMULATIVE COSTS: ", cumulative_costs)


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
formatted_valuation = [ format_money(elem) for elem in valuation_per_year ]
print("VALUATION PER YEAR: ", formatted_valuation)


# Define the data for each DataFrame
data = {
    "Total Cumulative Costs": cumulative_costs,
    "Total License Fee Monthly (All Models)": total_license_fee_per_month_sum,
    "Total Cumulative License Fee (All Models)": total_cumulative_license_fee_all_models,
    "Sales Commission Per Month": sales_commission_per_month,
    "Total Cumulative Sales Commission": total_cumulative_sales_commission,
    "Cash Flow Per Month": cash_flow_per_month,
    "Total Cumulative Cash Flow": total_cumulative_cash_flow,
}


results_df = pd.DataFrame.from_dict(data)




# Create DataFrames
df_starter = model_output_to_dataframe(starter_model_output, "Starter")
df_advanced = model_output_to_dataframe(advanced_model_output, "Advanced")
df_enterprise = model_output_to_dataframe(enterprise_model_output, "Enterprise")

# Valuation Df

valuation_df = pd.DataFrame(formatted_valuation, columns=["Valuation Per Year"])

# Concatenate all DataFrames vertically
df_partner_business_model = pd.concat([df_starter,
                                       df_advanced,
                                       df_enterprise,
                                       results_df,
                                       valuation_df], axis=1)

# Write the concatenated DataFrame to a CSV file
df_partner_business_model.to_csv("Partner_Business_Model.csv", index=False)

print("All DataFrames have been successfully combined and written to 'Partner_Business_Model.csv'.")