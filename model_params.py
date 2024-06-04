from dataclasses import dataclass
from typing import Optional

@dataclass
class LinearModelParams():
    first_month_of_location: int
    months_between_location: int

@dataclass
class GrowthModelParams():
    first_six_months_locations: int
    next_six_months_locations: int
    total_locations: int

@dataclass
class PricingParams():
    location_license_fee: float
    gateway_license_fee: float
    camera_license_fee: float


@dataclass
class PartnerParams():
    num_partners: int
    max_locations: int
    months_between_partners: int


@dataclass
class ModelParams():
    months: int
    gateways_per_location: int
    cameras_per_gateway: int
    pricing_params: PricingParams
    location_model_params: LinearModelParams | GrowthModelParams
    partner_params: Optional[PartnerParams] = None
    

@dataclass
class ModelOutput():
    new_locations: list[int]
    cumulative_locations: list[int]
    cumulative_gateways: list[int]
    cumulative_cameras: list[int]
    cumulative_location_license_fees: list[float]
    cumulative_gateway_license_fees: list[float]
    cumulative_cameras_license_fees: list[float]
    total_license_fee: list[float]
    new_partners: Optional[list[int]] = None
    cumulative_partners: Optional[list[int]] = None

@dataclass
class CostParams():
    cost_per_month: float

@dataclass
class SalesParams():
    commission_rate: float

@dataclass
class ValuationParams():
    years: int
    discount_rate: float