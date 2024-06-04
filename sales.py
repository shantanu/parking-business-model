from model_params import SalesParams

def get_sales_commission(sales_params: SalesParams, monthly_license_fee: list[float]) -> list[float]:
    # OUTPUT: monthly sales commission
    return [sales_params.commission_rate * fee for fee in monthly_license_fee]
