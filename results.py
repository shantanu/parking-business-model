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


def generate_dataframe(params: dict[str, ModelParams], 
                       cost_params: CostParams,
                       sales_params: SalesParams, 
                       valuation_params: ValuationParams,
                       output_path: str):
    MONTHS = list(params.values())[0].months
    model_outputs = {name: get_locations(params) for name, params in params.items()}

    print("===================")
    print()


    for name, output in model_outputs.items():
        print_model_output(name, output)

    print("===================")
    print()

    cumulative_locations = [
        sum(x) for x in zip(
            *(model_output.cumulative_locations for model_output in model_outputs.values())
        )
    ]

    cost_per_month = get_costs(cost_params, MONTHS)
    cumulative_costs = list(accumulate(cost_per_month))
    print("TOTAL CUMULATIVE COSTS: ", cumulative_costs)


    total_license_fee_per_month_sum = [
        sum(x) for x in zip(
            *(model_output.total_license_fee for model_output in model_outputs.values())
    )]
    print("TOTAL LICENSE FEE MONTHLY ALL MODELS: ", total_license_fee_per_month_sum)

    total_cumulative_license_fee_all_models = list(accumulate(total_license_fee_per_month_sum))
    print("TOTAL CUMULATIVE LICENSE FEE ALL MODELS: ", total_cumulative_license_fee_all_models)

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




    valuation_per_year = get_yearly_valuation(valuation_params, total_cumulative_cash_flow)
    formatted_valuation = [ format_money(elem) for elem in valuation_per_year ]
    print("VALUATION PER YEAR: ", formatted_valuation)

    annual_revenue = [
        total_cumulative_license_fee_all_models[i*12-1]
        for i in range(1, MONTHS//12+1)
    ]

    monthly_recurring_revenue = [
        total_license_fee_per_month_sum[i*12-1]
        for i in range(1, MONTHS//12+1)
    ]

    yearly_locations = [
        cumulative_locations[i*12-1]
        for i in range(1, MONTHS//12+1)
    ]


    # Define the data for each DataFrame
    data = {
        "Total Cumulative Locations": cumulative_locations,
        "Total Cumulative Costs": cumulative_costs,
        "Total License Fee Monthly (All Models)": total_license_fee_per_month_sum,
        "Total Cumulative License Fee (All Models)": total_cumulative_license_fee_all_models,
        "Sales Commission Per Month": sales_commission_per_month,
        "Total Cumulative Sales Commission": total_cumulative_sales_commission,
        "Cash Flow Per Month": cash_flow_per_month,
        "Total Cumulative Cash Flow": total_cumulative_cash_flow,
    }


    monthly_results_df = pd.DataFrame.from_dict(data)




    # Create DataFrames
    dataframes = [
        model_output_to_dataframe(output, name) for name, output in model_outputs.items()
    ]

    # Yearly Results
    yearly_results = {
        "Annual Revenue": annual_revenue,
        "Monthly Recurring Revenue": monthly_recurring_revenue,
        "Yearly Locations": yearly_locations,
        "Valuation Per Year": formatted_valuation
    }

    yearly_df = pd.DataFrame.from_dict(yearly_results)


    dataframes.extend([monthly_results_df, yearly_df])

    # Concatenate all DataFrames vertically
    df_partner_business_model = pd.concat(dataframes, axis=1)

    # Write the concatenated DataFrame to a CSV file
    df_partner_business_model.to_csv(output_path, index=False)

    print(f"All DataFrames have been successfully combined and written to {output_path}.")