from results import generate_dataframe, rename_columns_ai4m
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

def generate_parking_dataframe():
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
        cameras_per_gateway=0,
        partner_params=PartnerParams(
            num_partners=0, max_locations=10, months_between_partners=1
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, months_between_location=3
        ),
        pricing_params=PricingParams(
            location_license_fee=25000, gateway_license_fee=0, camera_license_fee=0
        ),
    )


    # Advanced Model Parameters
    advanced_model_params: ModelParams = ModelParams(
        months=MONTHS,
        gateways_per_location=20,
        cameras_per_gateway=0,
        partner_params=PartnerParams(
            num_partners=0, max_locations=20, months_between_partners=2
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, months_between_location=3
        ),
        pricing_params=PricingParams(
            location_license_fee=27500, gateway_license_fee=0, camera_license_fee=0
        ),
    )


    # Enterprise Model Parameters
    enterprise_model_params: ModelParams = ModelParams(
        months=MONTHS,
        gateways_per_location=30,
        cameras_per_gateway=0,
        partner_params=PartnerParams(
            num_partners=20, max_locations=100, months_between_partners=3
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, months_between_location=1
        ),
        pricing_params=PricingParams(
            location_license_fee=30000, gateway_license_fee=0, camera_license_fee=0
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

    return generate_dataframe(
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
