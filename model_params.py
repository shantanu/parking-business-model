from dataclasses import dataclass

@dataclass
class LinearModelParams():
    first_month_of_location: int
    months_between_location: int

@dataclass
class GrowthModelParams():
    first_month_of_location: int
    growth_multiplier: float


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
    partner_params: PartnerParams
    location_model_params: LinearModelParams # | GrowthModelParams
    pricing_params: PricingParams
