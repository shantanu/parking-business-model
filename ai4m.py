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

cost_params: CostParams = CostParams(cost_per_month=FIXED_COST)

sales_params: SalesParams = SalesParams(commission_rate=SALES_COMMISSION)

valuation_params: ValuationParams = ValuationParams(
    years=MONTHS // 12, discount_rate=DISCOUNT_RATE
)


def generate_ai4m_dataframe():
    # Small Model Parameters
    small_model_params: ModelParams = ModelParams(
        months=MONTHS,
        gateways_per_location=10, # skus per location
        cameras_per_gateway=0, # irrelevant
        partner_params=PartnerParams(
            num_partners=0, # num_companies
            max_locations=10, # production lines
            months_between_partners=1 # months between companies
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, # first month to new production line
            months_between_location=3 # months between production line
        ),
        pricing_params=PricingParams(
            location_license_fee=25000, # per production line fee
            gateway_license_fee=0, # sku license fee
            camera_license_fee=0 # not used
        ),
    )


    # Large Model Parameters
    large_model_params: ModelParams = ModelParams(
        months=MONTHS,
        gateways_per_location=20, # skus per location
        cameras_per_gateway=0, # irrelevant
        partner_params=PartnerParams(
            num_partners=0, # num_companies
            max_locations=20, # production lines
            months_between_partners=2 # months between companies
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, # first month to new production line
            months_between_location=3 # months between production line
        ),
        pricing_params=PricingParams(
            location_license_fee=27500,  # per production line fee
            gateway_license_fee=0, # sku license fee
            camera_license_fee=0 # not used
        ),
    )


    # Enterprise Model Parameters
    enterprise_model_params: ModelParams = ModelParams(
        months=MONTHS,
        gateways_per_location=30, # skus per location
        cameras_per_gateway=0, # irrelevant
        partner_params=PartnerParams(
            num_partners=20, # num_companies
            max_locations=100, # production lines
            months_between_partners=3 # months between companies
        ),
        location_model_params=LinearModelParams(
            first_month_of_location=3, # first month to new production line
            months_between_location=1 # months between production line
        ),
        pricing_params=PricingParams(
            location_license_fee=30000,  # per production line fee
            gateway_license_fee=0, # sku license fee
            camera_license_fee=0 # not used
        ),
    )

    return generate_dataframe(
        {
            "Small": small_model_params,
            "Large": large_model_params,
            "Enterprise": enterprise_model_params,
        },
        cost_params,
        sales_params,
        valuation_params,
        "AI4M",
        "AI4Manufacturing_model_output.csv",
        rename_columns=True
    )
