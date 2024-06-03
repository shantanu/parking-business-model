from model_params import CostParams

def get_costs(cost_params: CostParams, months: int) -> list[float]:
    # INPUT: cost params
    # OUTPUT: cost per months
    costs_per_month = [cost_params.cost_per_month]*months

    return costs_per_month