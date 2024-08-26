import unittest
from datetime import datetime
from car_module.car_fcatory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(calliop_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(calliop_car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(calliop_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(calliop_car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.1, 1.0, 0.1, 0.1]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(calliop_car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        calliop_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(calliop_car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(glissade_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(glissade_car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(glissade_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(glissade_car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.5, 2.0, 1.0, 0.0]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(glissade_car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.5, 0.9, 1.0, 0.05]

        glissade_car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(glissade_car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertTrue(TestPalindrome_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        warning_light_is_on = False
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertFalse(TestPalindrome_car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertTrue(TestPalindrome_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertFalse(TestPalindrome_car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wear_sensor = [0.8, 1.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertTrue(TestPalindrome_car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wear_sensor = [0.8, 0.0, 0.0, 0.0]

        TestPalindrome_car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on, wear_sensor)
        self.assertFalse(TestPalindrome_car.needs_service())
class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(rorschach_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(rorschach_car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(rorschach_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(rorschach_car.needs_service())
    
    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.9, 0.8, 0.7, 1.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(rorschach_car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(rorschach_car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(throvex_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(throvex_car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(throvex_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.0, 0.0, 0.0, 0.0]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(throvex_car.needs_service())

    def test_tire_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.1, 0.9, 0.3, 0.1]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertTrue(throvex_car.needs_service())

    def test_tire_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_sensor = [0.5, 0.2, 0.05, 0.05]

        throvex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor)
        self.assertFalse(throvex_car.needs_service())


if __name__ == '__main__':
    unittest.main()
