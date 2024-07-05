from results import generate_dataframe, rename_columns_ai4m
from ai4m import generate_ai4m_dataframe
from parking import generate_parking_dataframe
from model_params import *
from costs import get_costs
import numpy as np
import pandas as pd
from valuation import get_cash_flow, format_money, get_yearly_valuation


from itertools import accumulate

MONTHS: int = 60
FIXED_COST: int = 89500
SALES_COMMISSION: float = 0.25
DISCOUNT_RATE: float = 0.10


smart_parking_df = generate_parking_dataframe()

ai4m_df = generate_ai4m_dataframe()

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

acx_cost_params: CostParams = CostParams(cost_per_month=FIXED_COST)
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

