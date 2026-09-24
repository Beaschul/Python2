class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_water_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato","Lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as error:
        print(f"Caugth PlantError: {error}")
        return
    finally:
        print("Closing watering system")
        
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
       for plant in ["Tomato", "lettuce"]:
            water_plant(plant)
    except PlantError as error:
        print(f"Caugth PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_water_system()