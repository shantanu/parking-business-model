
from results import generate_dataframe
from model_params import *


MONTHS: int = 60
FIXED_COST: int = 100000
SALES_COMMISSION: float = .25
DISCOUNT_RATE: float = .10


# Parking Operator Model Parameters
parking_operator_model_params: ModelParams = ModelParams(
    months=MONTHS,
    location_model_params=GrowthModelParams(
        first_six_months_locations=0,
        next_six_months_locations=0,
        total_locations=0,
    ),
    pricing_params=PricingParams(
        location_license_fee=350,
        gateway_license_fee=75,
        camera_license_fee=0.75
    ),
    gateways_per_location=10,
    cameras_per_gateway=30
)

cost_params: CostParams = CostParams(
    cost_per_month=100000
)

sales_params: SalesParams = SalesParams(
    commission_rate=SALES_COMMISSION
)

valuation_params: ValuationParams = ValuationParams(
    years=MONTHS//12,
    discount_rate=DISCOUNT_RATE
)

generate_dataframe(
    {
        "Parking Operator": parking_operator_model_params
    },
    cost_params,
    sales_params,
    valuation_params,
    "Operator_Business_model_output.csv"
)


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

generate_dataframe(
    {
        "Starter": starter_model_params,
        "Advanced": advanced_model_params,
        "Enterprise": enterprise_model_params
    },
    cost_params,
    sales_params,
    valuation_params,
    "Partner_Business_model_output.csv"
)

generate_dataframe(
    {
        "Starter": starter_model_params,
        "Advanced": advanced_model_params,
        "Enterprise": enterprise_model_params,
        "Operator": parking_operator_model_params
    },
    cost_params,
    sales_params,
    valuation_params,
    "Combined_Business_model_output.csv"
)