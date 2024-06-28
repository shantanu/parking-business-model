from results import generate_dataframe
from model_params import *
from costs import get_costs
import numpy as np
import pandas as pd
from valuation import get_cash_flow, format_money, get_yearly_valuation


from itertools import accumulate


MONTHS: int = 60
FIXED_COST: int = 230000
SALES_COMMISSION: float = 0.25
DISCOUNT_RATE: float = 0.10


# Parking Operator Model Parameters
parking_operator_model_params: ModelParams = ModelParams(
    months=MONTHS,
    location_model_params=GrowthModelParams(
        first_six_months_locations=0,
        next_six_months_locations=0,
        total_locations=0,
    ),
    pricing_params=PricingParams(
        location_license_fee=0, gateway_license_fee=0, camera_license_fee=0
    ),
    gateways_per_location=15,
    cameras_per_gateway=30,
)

cost_params: CostParams = CostParams(cost_per_month=FIXED_COST)

sales_params: SalesParams = SalesParams(commission_rate=SALES_COMMISSION)

valuation_params: ValuationParams = ValuationParams(
    years=MONTHS // 12, discount_rate=DISCOUNT_RATE
)

generate_dataframe(
    {"Parking Operator": parking_operator_model_params},
    cost_params,
    sales_params,
    valuation_params,
    "Smart Parking Operator",
    "Operator_Business_model_output.csv",
)


# Starter Model Parameters
starter_model_params: ModelParams = ModelParams(
    months=MONTHS,
    gateways_per_location=10,
    cameras_per_gateway=10,
    partner_params=PartnerParams(
        num_partners=50, max_locations=10, months_between_partners=1
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3, months_between_location=3
    ),
    pricing_params=PricingParams(
        location_license_fee=0, gateway_license_fee=1500, camera_license_fee=0
    ),
)


# Advanced Model Parameters
advanced_model_params: ModelParams = ModelParams(
    months=MONTHS,
    gateways_per_location=15,
    cameras_per_gateway=20,
    partner_params=PartnerParams(
        num_partners=30, max_locations=20, months_between_partners=2
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3, months_between_location=3
    ),
    pricing_params=PricingParams(
        location_license_fee=0, gateway_license_fee=1500, camera_license_fee=0
    ),
)


# Enterprise Model Parameters
enterprise_model_params: ModelParams = ModelParams(
    months=MONTHS,
    gateways_per_location=20,
    cameras_per_gateway=30,
    partner_params=PartnerParams(
        num_partners=20, max_locations=30, months_between_partners=1
    ),
    location_model_params=LinearModelParams(
        first_month_of_location=3, months_between_location=3
    ),
    pricing_params=PricingParams(
        location_license_fee=0, gateway_license_fee=1500, camera_license_fee=0
    ),
)

generate_dataframe(
    {
        "Starter": starter_model_params,
        "Advanced": advanced_model_params,
        "Enterprise": enterprise_model_params,
    },
    cost_params,
    sales_params,
    valuation_params,
    "Smart Parking Partner",
    "Partner_Business_model_output.csv",
)

smart_parking_df = generate_dataframe(
    {
        "Starter": starter_model_params,
        "Advanced": advanced_model_params,
        "Enterprise": enterprise_model_params,
        "Operator": parking_operator_model_params,
    },
    cost_params,
    sales_params,
    valuation_params,
    "Smart Parking Combined",
    "Combined_Business_model_output.csv",
)


ai4m_cost_params: CostParams = CostParams(cost_per_month=200000)


ai4m_model_params: ModelParams = ModelParams(
    months=MONTHS,
    location_model_params=GrowthModelParams(
        first_six_months_locations=0,
        next_six_months_locations=0,
        total_locations=750,
    ),
    pricing_params=PricingParams(
        location_license_fee=15000, gateway_license_fee=0, camera_license_fee=0
    ),
    gateways_per_location=0,
    cameras_per_gateway=0,
)

ai4m_df = generate_dataframe(
    {
        "AI4M": ai4m_model_params,
    },
    ai4m_cost_params,
    sales_params,
    valuation_params,
    "AI4M",
    "AI4M_model_output.csv",
)

acx_monthly_revenue = (
    smart_parking_df["Sales Commission Per Month"]
    + ai4m_df["Sales Commission Per Month"]
)
print(acx_monthly_revenue)

acx_cumulative_revenue = (
    smart_parking_df["Total Cumulative Sales Commission"]
    + ai4m_df["Total Cumulative Sales Commission"]
)
print(acx_cumulative_revenue)

acx_cost_params: CostParams = CostParams(cost_per_month=89500)
acx_cost_per_month = get_costs(acx_cost_params, MONTHS)
print("ACX COST PER MONTH", acx_cost_per_month)

acx_cumulative_costs = list(accumulate(acx_cost_per_month))
print("ACX CUMULATIVE COSTS", acx_cumulative_costs)

acx_cumulative_cash_flows = np.subtract(acx_cumulative_revenue, acx_cumulative_costs)
print("ACX CUMULATIVE CASH FLOWS: ", acx_cumulative_cash_flows)


acx_valuation_params: ValuationParams = ValuationParams(
    years=MONTHS // 12, discount_rate=DISCOUNT_RATE
)

acx_valuation_per_year = get_yearly_valuation(
    acx_valuation_params, acx_cumulative_cash_flows
)
acx_formatted_valuation = [format_money(elem) for elem in acx_valuation_per_year]
print("VALUATION PER YEAR: ", acx_formatted_valuation)

data = {
    "ACX Monthly Revenue": acx_monthly_revenue,
    "ACX Cumulative Revenue": acx_cumulative_revenue,
    "ACX Cost Per Month": acx_cost_per_month,
    "ACX Cumulative Costs": acx_cumulative_costs,
    "ACX Cumulative Cash Flows": acx_cumulative_cash_flows,
}
acx_df = pd.DataFrame.from_dict(data)
acx_df = pd.concat([acx_df, pd.DataFrame(acx_formatted_valuation)], axis=1)

acx_df.to_csv("ACX_model_output.csv")

output_df = pd.DataFrame.from_dict(
    {
        "Smart Parking Valuation": smart_parking_df[
            "Valuation Per Year: Smart Parking Combined"
        ].iloc[:5],
        "AI4M Valuation": ai4m_df["Valuation Per Year: AI4M"].iloc[:5],
        "ACX Valuation": acx_formatted_valuation,
    }
)

print(output_df)

output_df.to_csv("all_valuations.csv")




# New AI4M model with Production lines and SKU licensing Model
#parking_operator_model_params: ModelParams = ModelParams(
#    months=MONTHS,
#    location_model_params=GrowthModelParams(
#        first_six_months_locations=0,
#        next_six_months_locations=0,
#        total_locations=0,
#    ),
#    pricing_params=PricingParams(
#        location_license_fee=0, gateway_license_fee=0, camera_license_fee=0
#    ),
#    gateways_per_location=15,
#    cameras_per_gateway=30,
#)

#cost_params: CostParams = CostParams(cost_per_month=FIXED_COST)

#sales_params: SalesParams = SalesParams(commission_rate=SALES_COMMISSION)

#valuation_params: ValuationParams = ValuationParams(
#    years=MONTHS // 12, discount_rate=DISCOUNT_RATE
#)

#generate_dataframe(
#    {"Parking Operator": parking_operator_model_params},
#    cost_params,
#    sales_params,
#    valuation_params,
#    "Smart Parking Operator",
#    "Operator_Business_model_output.csv",
#)


# Small Manufacturing Company Deployment (SMCD) Model Parameters
smcd_params: ModelParams = ModelParams(
    months=MONTHS,
    sku_per_production_line=10,
    cameras_per_production_line=10,
    smcd_params=PartnerParams(
        num_smcd=50, max_production_line=10, months_between_smcd=1
    ),
    production_line_model_params=LinearModelParams(
        first_month_of_production_line=3, months_between_production_line=3
    ),
    pricing_params=PricingParams(
        production_line_license_fee=0, per_sku_license_fee=1500, camera_license_fee=0
    ),
)


# Medium Manufacturing Company Deployment (MMCD) Model Parameters
mmcd_model_params: ModelParams = ModelParams(
    months=MONTHS,
    sku_per_production_line=15,
    cameras_per_production_line=20,
    mmcd_params=PartnerParams(
        num_mmcd=30, max_production_line=20, months_between_mmcd=2
    ),
    production_line_model_params=LinearModelParams(
        first_month_of_production_line=3, months_between_production_line=3
    ),
    pricing_params=PricingParams(
        production_line_license_fee=0, per_sku_license_fee=1500, camera_license_fee=0
    ),
)


# Large Manufacturing Company Deployment (LMCD) Model Parameters
lmcd_model_params: ModelParams = ModelParams(
    months=MONTHS,
    sku_per_production_line=20,
    cameras_per_production_line=30,
    lmcd_params=PartnerParams(
        num_lmcd=20, max_production_line=30, months_between_lmcd=1
    ),
    production_line_model_params=LinearModelParams(
        first_month_of_production_line=3, months_between_production_line=3
    ),
    pricing_params=PricingParams(
        production_line_license_fee=0, per_sku_license_fee=1500, camera_license_fee=0
    ),
)

generate_dataframe(
    {
        "Small Deployment": smcd_model_params,
        "Medium Deployment": mmcd_model_params,
        "Large Deployment": lmcd_model_params,
    },
    cost_params,
    sales_params,
    valuation_params,
    "AI for Manufacturing",
    "AI_Company_model_output.csv",
)

#manufacturing_company_df = generate_dataframe(
#    {
#        "Small Deployment": smcd_model_params,
#        "Medium Deployment": mmcd_model_params,
#        "Large Deployment": lmcd_model_params,
#    },
#    cost_params,
#    sales_params,
#    valuation_params,
#    "Smart Parking Combined",
#    "Combined_Business_model_output.csv",