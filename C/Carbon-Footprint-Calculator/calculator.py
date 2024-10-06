# Carbon Footprint Calculator
# Author: [Your Name]
# Date: [Date]
# Description: Calculates the user's annual carbon footprint based on various lifestyle factors.

def get_transportation_emissions():
    print("\n--- Transportation Emissions ---")
    car_miles = float(input("Enter average weekly miles driven by car: "))
    car_mpg = float(input("Enter your car's fuel efficiency (mpg): "))
    bus_miles = float(input("Enter average weekly miles traveled by bus: "))
    train_miles = float(input("Enter average weekly miles traveled by train: "))
    flights_per_year = int(input("Enter number of flights taken per year (average length 4 hours): "))

    # Emission factors
    gas_emission_factor = 19.6  # lbs CO2 per gallon of gasoline
    diesel_emission_factor = 22.4  # lbs CO2 per gallon of diesel
    bus_emission_factor = 0.65  # lbs CO2 per passenger mile
    train_emission_factor = 0.41  # lbs CO2 per passenger mile
    flight_emission_factor = 1100  # lbs CO2 per 4-hour flight

    # Calculations
    annual_car_miles = car_miles * 52
    annual_gallons = annual_car_miles / car_mpg
    car_emissions = annual_gallons * gas_emission_factor

    bus_emissions = bus_miles * 52 * bus_emission_factor
    train_emissions = train_miles * 52 * train_emission_factor
    flight_emissions = flights_per_year * flight_emission_factor

    total_transportation_emissions = car_emissions + bus_emissions + train_emissions + flight_emissions

    print(f"\nTotal Annual Transportation Emissions: {total_transportation_emissions:.2f} lbs CO2")
    return total_transportation_emissions

def get_energy_emissions():
    print("\n--- Home Energy Use ---")
    electricity_kwh = float(input("Enter average monthly electricity usage (kWh): "))
    natural_gas_therms = float(input("Enter average monthly natural gas usage (therms): "))
    fuel_oil_gallons = float(input("Enter average monthly fuel oil usage (gallons): "))
    propane_gallons = float(input("Enter average monthly propane usage (gallons): "))

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

    print(f"\nTotal Annual Home Energy Emissions: {total_energy_emissions:.2f} lbs CO2")
    return total_energy_emissions

def get_diet_emissions():
    print("\n--- Dietary Impact ---")
    print("Select your diet type:")
    print("1. Meat-heavy diet")
    print("2. Average diet")
    print("3. Vegetarian")
    print("4. Vegan")
    diet_choice = input("Enter the number corresponding to your diet: ")

    # Emission factors (lbs CO2 per year)
    if diet_choice == '1':
        diet_emissions = 3,300
    elif diet_choice == '2':
        diet_emissions = 2,800
    elif diet_choice == '3':
        diet_emissions = 1,500
    elif diet_choice == '4':
        diet_emissions = 1,000
    else:
        print("Invalid choice. Defaulting to average diet.")
        diet_emissions = 2,800

    print(f"\nAnnual Dietary Emissions: {diet_emissions} lbs CO2")
    return diet_emissions

def get_waste_emissions():
    print("\n--- Waste and Recycling ---")
    print("Answer 'yes' or 'no' to the following recycling practices.")
    recycle_paper = input("Do you recycle paper? ").strip().lower()
    recycle_plastic = input("Do you recycle plastic? ").strip().lower()
    recycle_glass = input("Do you recycle glass? ").strip().lower()
    recycle_metal = input("Do you recycle metal? ").strip().lower()

    # Baseline emissions
    waste_emissions = 692  # lbs CO2 per person per year

    # Reductions
    if recycle_paper == 'yes':
        waste_emissions -= 79
    if recycle_plastic == 'yes':
        waste_emissions -= 35
    if recycle_glass == 'yes':
        waste_emissions -= 25
    if recycle_metal == 'yes':
        waste_emissions -= 46

    print(f"\nAnnual Waste Emissions after recycling reductions: {waste_emissions} lbs CO2")
    return waste_emissions

def main():
    print("Welcome to the Carbon Footprint Calculator!")
    total_transport = get_transportation_emissions()
    total_energy = get_energy_emissions()
    total_diet = get_diet_emissions()
    total_waste = get_waste_emissions()

    total_emissions = total_transport + total_energy + total_diet + total_waste

    # Convert lbs CO2 to metric tons
    total_emissions_metric_tons = total_emissions * 0.000453592

    print("\n--- Summary of Your Annual Carbon Footprint ---")
    print(f"Transportation Emissions: {total_transport:.2f} lbs CO2")
    print(f"Home Energy Emissions: {total_energy:.2f} lbs CO2")
    print(f"Dietary Emissions: {total_diet} lbs CO2")
    print(f"Waste Emissions: {total_waste} lbs CO2")
    print(f"\nTotal Annual Emissions: {total_emissions:.2f} lbs CO2")
    print(f"Which is equivalent to {total_emissions_metric_tons:.2f} metric tons of CO2")

    # National average comparison (approximate)
    national_average = 16000  # lbs CO2 per person per year
    if total_emissions < national_average:
        print("\nCongratulations! Your carbon footprint is below the national average.")
    else:
        print("\nYour carbon footprint is above the national average. Consider making changes to reduce it.")

    # Suggestions for reduction
    print("\n--- Suggestions to Reduce Your Carbon Footprint ---")
    print("- Use public transportation, carpool, or cycle when possible.")
    print("- Improve home insulation and use energy-efficient appliances.")
    print("- Consider a plant-based diet or reduce meat consumption.")
    print("- Recycle and reduce waste whenever possible.")
    print("- Use renewable energy sources if available.")

if __name__ == "__main__":
    main()
