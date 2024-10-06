from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Transportation Data
    car_miles = float(request.form.get('car_miles', 0))
    car_mpg = float(request.form.get('car_mpg', 0))
    bus_miles = float(request.form.get('bus_miles', 0))
    train_miles = float(request.form.get('train_miles', 0))
    flights_per_year = int(request.form.get('flights_per_year', 0))

    # Energy Data
    electricity_kwh = float(request.form.get('electricity_kwh', 0))
    natural_gas_therms = float(request.form.get('natural_gas_therms', 0))
    fuel_oil_gallons = float(request.form.get('fuel_oil_gallons', 0))
    propane_gallons = float(request.form.get('propane_gallons', 0))

    # Diet Data
    diet_choice = request.form.get('diet_choice', '2')

    # Waste Data
    recycle_paper = request.form.get('recycle_paper', 'no')
    recycle_plastic = request.form.get('recycle_plastic', 'no')
    recycle_glass = request.form.get('recycle_glass', 'no')
    recycle_metal = request.form.get('recycle_metal', 'no')

    # Calculations
    total_transport = get_transportation_emissions(car_miles, car_mpg, bus_miles, train_miles, flights_per_year)
    total_energy = get_energy_emissions(electricity_kwh, natural_gas_therms, fuel_oil_gallons, propane_gallons)
    total_diet = get_diet_emissions(diet_choice)
    total_waste = get_waste_emissions(recycle_paper, recycle_plastic, recycle_glass, recycle_metal)

    total_emissions = total_transport + total_energy + total_diet + total_waste
    total_emissions_metric_tons = total_emissions * 0.000453592

    # National average comparison (approximate)
    national_average = 16000  # lbs CO2 per person per year
    below_average = total_emissions < national_average

    return render_template('results.html',
                           total_transport=total_transport,
                           total_energy=total_energy,
                           total_diet=total_diet,
                           total_waste=total_waste,
                           total_emissions=total_emissions,
                           total_emissions_metric_tons=total_emissions_metric_tons,
                           below_average=below_average)

def get_transportation_emissions(car_miles, car_mpg, bus_miles, train_miles, flights_per_year):
    # Emission factors
    gas_emission_factor = 19.6  # lbs CO2 per gallon of gasoline
    bus_emission_factor = 0.65  # lbs CO2 per passenger mile
    train_emission_factor = 0.41  # lbs CO2 per passenger mile
    flight_emission_factor = 1100  # lbs CO2 per 4-hour flight

    # Calculations
    annual_car_miles = car_miles * 52
    annual_gallons = annual_car_miles / car_mpg if car_mpg != 0 else 0
    car_emissions = annual_gallons * gas_emission_factor

    bus_emissions = bus_miles * 52 * bus_emission_factor
    train_emissions = train_miles * 52 * train_emission_factor
    flight_emissions = flights_per_year * flight_emission_factor

    total_transportation_emissions = car_emissions + bus_emissions + train_emissions + flight_emissions

    return total_transportation_emissions

def get_energy_emissions(electricity_kwh, natural_gas_therms, fuel_oil_gallons, propane_gallons):
    # Emission factors
    electricity_emission_factor = 1.22  # lbs CO2 per kWh
    natural_gas_emission_factor = 11.7  # lbs CO2 per therm
    fuel_oil_emission_factor = 22.4  # lbs CO2 per gallon
    propane_emission_factor = 12.7  # lbs CO2 per gallon

    # Calculations
    annual_electricity_emissions = electricity_kwh * 12 * electricity_emission_factor
    annual_natural_gas_emissions = natural_gas_therms * 12 * natural_gas_emission_factor
    annual_fuel_oil_emissions = fuel_oil_gallons * 12 * fuel_oil_emission_factor
    annual_propane_emissions = propane_gallons * 12 * propane_emission_factor

    total_energy_emissions = (annual_electricity_emissions + annual_natural_gas_emissions +
                              annual_fuel_oil_emissions + annual_propane_emissions)

    return total_energy_emissions

def get_diet_emissions(diet_choice):
    # Emission factors (lbs CO2 per year)
    diet_emissions_dict = {
        '1': 3300,   # Meat-heavy diet
        '2': 2800,   # Average diet
        '3': 1500,   # Vegetarian
        '4': 1000    # Vegan
    }
    diet_emissions = diet_emissions_dict.get(diet_choice, 2800)
    return diet_emissions

def get_waste_emissions(recycle_paper, recycle_plastic, recycle_glass, recycle_metal):
    # Baseline emissions
    waste_emissions = 692  # lbs CO2 per person per year

    # Reductions
    if recycle_paper.lower() == 'yes':
        waste_emissions -= 79
    if recycle_plastic.lower() == 'yes':
        waste_emissions -= 35
    if recycle_glass.lower() == 'yes':
        waste_emissions -= 25
    if recycle_metal.lower() == 'yes':
        waste_emissions -= 46

    return waste_emissions

if __name__ == '__main__':
    app.run(debug=True)
