from model_params import ValuationParams


def get_cash_flow(fee, commission, cost):
    return fee - commission - cost

def discount(amount, rate, years):
    return (amount / ((1 + rate)**years))

def format_money(money: float) -> str:
    return f'${round(money):,}'

def get_yearly_valuation(valuation_params: ValuationParams, monthly_cumulative_cash_flow: list[float]) -> list[float]:
    return [
        discount(monthly_cumulative_cash_flow[year*12-1], valuation_params.discount_rate, year)
        for year in range(1, valuation_params.years+1)
    ]