import time
from abc import abstractmethod


class VehicleBuilder:
    # Abstract builder
    """An abstract class Creates various parts of a rental vehicle."""

    @abstractmethod
    def set_brand(self, brand):
        pass

    @abstractmethod
    def set_model(self, model):
        pass

    @abstractmethod
    def set_year(self, year):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_tires(self):
        pass

    @abstractmethod
    def set_doors(self):
        pass

    @abstractmethod
    def set_sun_roof(self, sun_roof):
        pass

    @abstractmethod
    def set_price_per_day(self, price_per_day):
        pass

    @abstractmethod
    def set_type(self):
        # Method to set the vehicle type.
        pass

    @abstractmethod
    def build(self):
        # Finalizes construction and returns the built vehicle.
        pass


class Vehicle:
    # Product class
    """ Product class, The final product.
    A rental car is being searched by the "director" class
    from part (brand, model ...) """

    def __init__(self):
        # Initializes a vehicle with default attributes.
        self._brand = None
        self._model = None
        self._year = None
        self._color = None
        self._doors = None
        self._sun_roof = None
        self._engine = None
        self._tires = None
        self._price_per_day = None
        self._vehicle_type = None  # new attribute which can distinguish car types

    def display_info(self):
        """Displays the basic information of the Vehicle."""
        return f"Vehicle Type: {self._vehicle_type}, Brand: {self._brand}, Model: {self._model}, " \
               f"Year: {self._year}, Color: {self._color}, Doors: {self._doors}, Sun Roof: {self._sun_roof}, " \
               f"Engine: {self._engine}, Tires: {self._tires}, Price Per Day: {self._price_per_day}"

    # The following methods are getters and setters for the vehicle attributes.
    def get_price(self):
        """Return the price per day which used in rental class"""
        return self._price_per_day

    def get_brand(self):
        """Return the brand"""
        return self._brand

    def get_model(self):
        """Return the model"""
        return self._model

    def get_year(self):
        """Return the year"""
        return self._year

    def get_color(self):
        """Return the color"""
        return self._color

    def get_doors(self):
        """Return the doors"""
        return self._doors

    def get_sun_roof(self):
        """Return the sun_roof"""
        return self._sun_roof

    def get_engine(self):
        """Return the engine"""
        return self._engine

    def get_tires(self):
        """Return the tires"""
        return self._tires

    def set_price(self, value):
        # Setter for price_per_day, ensuring it's not negative.
        if value < 0:
            raise ValueError("Price per day cannot be negative.")
        self._price_per_day = value

    # Additional setter methods for various vehicle attributes.
    # These methods allow for the properties to be updated after initialization.
    def set_brand(self, brand):
        """setter for brand"""
        self._brand = brand

    def set_model(self, model):
        """setter for model"""
        self._model = model

    def set_year(self, year):
        """setter for year"""
        self._year = year

    def set_color(self, color):
        """setter for color"""
        self._color = color

    def set_doors(self, doors):
        """setter for doors"""
        self._doors = doors

    def set_sun_roof(self, sun_roof):
        """setter for sun_roof"""
        self._sun_roof = sun_roof

    def set_engine(self, engine):
        """setter for engine"""
        self._engine = engine

    def set_tires(self, tires):
        """setter for tires"""
        self._tires = tires

    def set_type(self, vehicle_type):
        """setter for vehicle type"""
        self._vehicle_type = vehicle_type


class SedanBuilder(VehicleBuilder):
    # Concrete builder for constructing Sedan vehicles.
    def __init__(self):
        self.vehicle = Vehicle()

    # Implementation of VehicleBuilder's abstract methods specifically for Sedans.
    # These methods define the characteristics of a Sedan.
    def set_brand(self, brand):
        self.vehicle.set_brand(brand)

    def set_model(self, model):
        self.vehicle.set_model(model)

    def set_year(self, year):
        self.vehicle.set_year(year)

    def set_color(self, color):
        self.vehicle.set_color(color)

    def set_doors(self):
        self.vehicle.set_doors(4)

    def set_sun_roof(self, sun_roof):
        self.vehicle.set_sun_roof(sun_roof)

    def set_engine(self):
        self.vehicle.set_engine("1.6L")

    def set_tires(self):
        self.vehicle.set_tires(4)

    def set_price_per_day(self, price_per_day):
        self.vehicle.set_price(price_per_day)

    def set_type(self):
        self.vehicle.set_type("Sedan")

    def build(self):
        return self.vehicle


class CoupeBuilder(VehicleBuilder):
    # Concrete builder for constructing Coupe vehicles.
    def __init__(self):
        self.vehicle = Vehicle()

    # Implements the VehicleBuilder's methods for Coupes.
    def set_brand(self, brand):
        self.vehicle.set_brand(brand)

    def set_model(self, model):
        self.vehicle.set_model(model)

    def set_year(self, year):
        self.vehicle.set_year(year)

    def set_color(self, color):
        self.vehicle.set_color(color)

    def set_doors(self):
        self.vehicle.set_doors(2)

    def set_sun_roof(self, sun_roof):
        self.vehicle.set_sun_roof(sun_roof)

    def set_engine(self):
        self.vehicle.set_engine("2.0L")

    def set_tires(self):
        self.vehicle.set_tires(4)

    def set_price_per_day(self, price_per_day):
        self.vehicle.set_price(price_per_day)

    def set_type(self):
        self.vehicle.set_type("Coupe")

    def build(self):
        return self.vehicle


class RentDirector:
    """ Controls the construction process. (has a construct method)
        Director has a builder associated with him. Director then
        delegates building of the smaller parts to the builder and
        assembles them together. """

    def __init__(self, builder):
        self._builder = builder

    def construct_vehicle(self, brand, model, year, color, sun_roof, price_per_day):
        # The order of steps can be modified here without changing the builders.
        self._builder.set_type()
        self._builder.set_brand(brand)
        self._builder.set_model(model)
        self._builder.set_year(year)
        self._builder.set_color(color)
        self._builder.set_engine()
        self._builder.set_doors()
        self._builder.set_sun_roof(sun_roof)
        self._builder.set_tires()
        self._builder.set_price_per_day(price_per_day)
        return self._builder.build()


def days_between_dates(dt1, dt2):
    """Calculate the date difference between rental date and return date"""
    date_format = "%m/%d/%Y"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    return int(delta / 86400)


class Rental:
    def __init__(self, customer, vehicle, rental_date, return_date):
        self.customer = customer  # A string with customer names
        self.vehicle = vehicle  # An instance of vehicle
        self.rental_date = rental_date
        self.return_date = return_date

    def rental_contract(self):
        date_dif = days_between_dates(self.rental_date, self.return_date)
        price = date_dif * self.vehicle.get_price()
        contract = (f"Rental Contract\n"
                    f"Customer: {self.customer}\n"
                    f"Vehicle: {self.vehicle.display_info()}\n"
                    f"Rental Date: {self.rental_date}\n"
                    f"Return Date: {self.return_date}\n"
                    f"Price: {price}")
        print(contract)


# Usage example Create instance of ConcreteBuilder (SedanBuilder & CoupeBuilder) and RentDirector
sedan_builder = SedanBuilder()
coupe_builder = CoupeBuilder()
rentDirector1 = RentDirector(sedan_builder)
rentDirector2 = RentDirector(coupe_builder)


# construct a Sedan and a coupe
car1 = rentDirector1.construct_vehicle("Toyota", "Camry", 2021, "black", "No", 200)
car2 = rentDirector2.construct_vehicle("BMW", "430i", 2023, "blue", "Yes", 500)
print(car1.display_info())
print(car2.display_info())
print()

# Creating two rental classes
my_rental = Rental("Ray Chen", car1, "2/12/2024", "2/15/2024")
rental2 = Rental("Oliver Zipse", car2, "1/11/2024", "2/11/2024")
my_rental.rental_contract()
print()
rental2.rental_contract()
print()
