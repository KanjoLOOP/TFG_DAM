class CostCalculator:
    def __init__(self):
        pass

    def calculate_filament_cost(self, weight_g, price_per_kg):
        """Calcula el coste del filamento."""
        if weight_g < 0 or price_per_kg < 0:
            return 0.0
        return (weight_g / 1000) * price_per_kg

    def calculate_energy_cost(self, power_watts, time_hours, cost_per_kwh):
        """Calcula el coste de energía."""
        if power_watts < 0 or time_hours < 0 or cost_per_kwh < 0:
            return 0.0
        kwh_consumed = (power_watts * time_hours) / 1000
        return kwh_consumed * cost_per_kwh

    def calculate_total_cost(self, filament_cost, energy_cost, additional_costs=0.0):
        """Calcula el coste total."""
        return filament_cost + energy_cost + additional_costs
    
    def calculate_sale_price(self, total_cost, margin_multiplier):
        """Calcula el precio de venta aplicando el margen de ganancia."""
        if total_cost < 0 or margin_multiplier < 0:
            return 0.0
        return total_cost * margin_multiplier
