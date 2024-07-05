import pandas as pd
from model_params import ModelOutput

def model_output_to_dataframe(model_output: ModelOutput, model_name: str) -> pd.DataFrame:
    data = {
        f"New Partners {model_name}": model_output.new_partners,
        f"Cumulative Partners {model_name}": model_output.cumulative_partners,
        f"New Locations {model_name}": model_output.new_locations,
        f"Cumulative Locations {model_name}": model_output.cumulative_locations,
        f"Cumulative Gateways {model_name}": model_output.cumulative_gateways,
        f"Cumulative Cameras {model_name}": model_output.cumulative_cameras,
        f"Cumulative Location License Fees {model_name}": model_output.cumulative_location_license_fees,
        f"Cumulative Gateway License Fees {model_name}": model_output.cumulative_gateway_license_fees,
        f"Cumulative Cameras License Fees {model_name}": model_output.cumulative_cameras_license_fees,
        f"Total License Fee {model_name}": model_output.total_license_fee
    }

    return pd.DataFrame(data)

def results_output_to_dataframe(data: dict[str, list[int|float]]) -> pd.DataFrame:
    return pd.DataFrame(data)
