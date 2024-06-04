from model_params import (
    ModelOutput, 
    ModelParams, 
    PartnerParams, 
    LinearModelParams, 
    GrowthModelParams, 
    PricingParams
)


def get_linear_model_locations(params: ModelParams) -> list[float]:
    # INPUT: linear model parameters
    # OUTPUT: new locations per month
    new_partners = [0]*params.months
    new_locations = [0]*params.months
    for partner in range(params.partner_params.num_partners):
        month_started = 4 + params.partner_params.months_between_partners*partner
        if month_started >= params.months:
            break
        
        new_partners[month_started] += 1
        
        for new_location in range(params.partner_params.max_locations):
            new_location_month = month_started + params.location_model_params.first_month_of_location + params.location_model_params.months_between_location*new_location
            
            if new_location_month >= params.months:
                break
            
            new_locations[new_location_month] += 1 

    return new_locations, new_partners

def get_growth_model_locations(params: ModelParams) -> list[float]:
    # INPUT: linear model parameters
    # OUTPUT: new locations per month
    model_params = params.location_model_params

    new_locations = [model_params.first_six_months_locations] * 6
    new_locations.extend([model_params.next_six_months_locations] * 6)

    remaining_months_locations = (model_params.total_locations - (model_params.first_six_months_locations*6) \
                                  - (model_params.next_six_months_locations*6)) // params.months + 1

    new_locations.extend([remaining_months_locations] * (params.months - 12))

    return new_locations



def get_locations(params: ModelParams):
    new_locations = [0]*params.months
    new_partners = [0]*params.months
    location_license_fees = [0]*params.months
    gateway_license_fees = [0]*params.months
    cameras_license_fees = [0]*params.months
    cumulative_gateways = [0]*params.months
    cumulative_cameras = [0]*params.months

    if isinstance(params.location_model_params, LinearModelParams):
        new_locations, new_partners = get_linear_model_locations(params)
    else:
        new_locations = get_growth_model_locations(params)
    
    for new_location_month, locs in enumerate(new_locations):
        for m in range(new_location_month, params.months):
            location_license_fees[m] += params.pricing_params.location_license_fee*locs
            gateway_license_fees[m] += params.pricing_params.gateway_license_fee * params.gateways_per_location * locs
            cameras_license_fees[m] += params.pricing_params.camera_license_fee * params.cameras_per_gateway * params.gateways_per_location * locs
            

    cumulative_partners = [0]*params.months
    for i in range(1, params.months):
        cumulative_partners[i] = cumulative_partners[i-1] + new_partners[i]
        
    cumulative_locations = [0]*params.months
    cumulative_location_license_fees = [0]*params.months
    cumulative_gateway_license_fees = [0]*params.months
    cumulative_cameras_license_fees = [0]*params.months
    for i in range(1, params.months):
        cumulative_locations[i] = cumulative_locations[i-1] + new_locations[i]
        cumulative_gateways[i] = cumulative_gateways[i-1] + params.gateways_per_location*new_locations[i]
        cumulative_cameras[i] = cumulative_cameras[i-1] + params.cameras_per_gateway*params.gateways_per_location*new_locations[i]
        cumulative_location_license_fees[i] = cumulative_location_license_fees[i-1] + location_license_fees[i]
        cumulative_gateway_license_fees[i] = cumulative_gateway_license_fees[i-1] + gateway_license_fees[i]
        cumulative_cameras_license_fees[i] = cumulative_cameras_license_fees[i-1] + cameras_license_fees[i]
    total_license_fee = [0]*params.months
    for i in range(1, params.months):
        total_license_fee[i] = cumulative_location_license_fees[i] + cumulative_gateway_license_fees[i] + cumulative_cameras_license_fees[i]
        
    return ModelOutput(
        new_partners=new_partners, 
        cumulative_partners=cumulative_partners, 
        new_locations=new_locations, 
        cumulative_locations=cumulative_locations, 
        cumulative_location_license_fees=cumulative_location_license_fees, 
        cumulative_gateway_license_fees=cumulative_gateway_license_fees,
        cumulative_cameras_license_fees=cumulative_cameras_license_fees,
        cumulative_gateways=cumulative_gateways,
        cumulative_cameras=cumulative_cameras,
        total_license_fee=total_license_fee
    )

def print_model_output(model_name: str, model_output: ModelOutput):
    print(f"{model_name} MODEL OUTPUT")
    print("New Partners:", model_output.new_partners)
    print("Cumulative Partners:", model_output.cumulative_partners)
    print("New Locations:", model_output.new_locations)
    print("Cumulative Locations:", model_output.cumulative_locations)
    print("Cumulative Gateways:", model_output.cumulative_gateways)
    print("Cumulative Cameras:", model_output.cumulative_cameras)
    print("Cumulative License Fees for Location:", model_output.cumulative_location_license_fees)
    print("Cumulative License Fees for Gateway:", model_output.cumulative_gateway_license_fees)
    print("Cumulative License Fees for Cameras:", model_output.cumulative_cameras_license_fees)
    print(f"Total License Fee {model_name}:", model_output.total_license_fee)
    print()

