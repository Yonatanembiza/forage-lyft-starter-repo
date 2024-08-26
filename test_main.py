# Import the necessary classes from your modules
from car_module.car_fcatory import CarFactory
from datetime import date

def run_tests():
    # Test creating a Calliope car
    print("Testing Calliope...")
    calliope_car = CarFactory.create_calliope(
        current_date=date(2024, 8, 26),
        last_service_date=date(2023, 8, 26),
        current_mileage=55000,
        last_service_mileage=20000
    )
    
    # Check if the car needs service
    print(f"Calliope needs service: {calliope_car.needs_service()}")

    # Test creating a Rorschach car
    print("\nTesting Rorschach...")
    rorschach_car = CarFactory.create_rorschach(
        current_date=date(2024, 8, 26),
        current_mileage=75000,
        last_service_date=date(2020, 8, 26),
        last_service_mileage=35000
    )

    # Check if the car needs service
    print(f"Rorschach needs service: {rorschach_car.needs_service()}")

if __name__ == "__main__":
    run_tests()
