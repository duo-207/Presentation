import time


class Vehicle:
    """Base class for all type of cars"""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day):
        """ Private attributes with '_' """
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color
        self._doors = doors
        self._sun_roof = sun_roof
        self._engine = engine
        self._tires = tires
        self._price_per_day = price_per_day

    # getter
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

    # setter
    def set_price(self, value):
        """Setter for price_per_day, should not be negative"""
        if value < 0:
            raise ValueError("Price per day cannot be negative.")
        self._price_per_day = value

    def set_brand(self, brand):
        """Setter for brand"""
        self._brand = brand

    def set_model(self, model):
        """Setter for model"""
        self._model = model

    def set_year(self, year):
        """Setter for year"""
        self._year = year

    def set_color(self, color):
        """Setter for color"""
        self._color = color

    def set_doors(self, doors):
        """Setter for doors"""
        self._doors = doors

    def set_sun_roof(self, sun_roof):
        """Setter for sun_roof"""
        self._sun_roof = sun_roof

    def set_engine(self, engine):
        """Setter for engine"""
        self._engine = engine

    def set_tires(self, tires):
        """Setter for tires"""
        self._tires = tires

    def display_info(self):
        """Displays the basic information of the Vehicle."""
        return f"Brand: {self._brand}, Model: {self._model}, Year: {self._year}, Color: {self._color}, " \
               f"Doors: {self._doors}, Sun Roof: {self._sun_roof}, Engine: {self._engine}, " \
               f"Tires: {self._tires}, Price Per Day: {self._price_per_day}"


class Car(Vehicle):
    """Derived class from Vehicle for Cars."""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day, car_type):
        super().__init__(brand, model, year, color, doors, sun_roof, engine, tires, price_per_day)
        self._car_type = car_type

    def display_info(self):
        """Displays car information including car type"""
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Car type: {self._car_type}"

    def set_type(self, vehicle_type):
        self._car_type = vehicle_type

    def get_type(self):
        return self._car_type

class Truck(Vehicle):
    """Derived class from Vehicle for Trucks."""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day, truck_type):
        super().__init__(brand, model, year, color, doors, sun_roof, engine, tires, price_per_day)
        self._truck_type = truck_type

    def display_info(self):
        """Displays truck information including truck type"""
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Truck type: {self._truck_type}"

    def set_type(self, vehicle_type):
        self._truck_type = vehicle_type

    def get_type(self):
        return self._truck_type


class SUV(Vehicle):
    """Derived class from Vehicle for SUV."""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day, suv_type):
        super().__init__(brand, model, year, color, doors, sun_roof, engine, tires, price_per_day)
        self._suv_type = suv_type

    def display_info(self):
        """Displays SUV information including suv type"""
        vehicle_info = super().display_info()
        return f"{vehicle_info}, SUV type: {self._suv_type}"

    def set_type(self, vehicle_type):
        self._suv_type = vehicle_type

    def get_type(self):
        return self._suv_type


class Motorcycle(Vehicle):
    """Derived class from Vehicle for Motorcycle."""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day, motor_type):
        super().__init__(brand, model, year, color, doors, sun_roof, engine, tires, price_per_day)
        self._motor_type = motor_type

    def display_info(self):
        """Displays motor information including motor type"""
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Motorcycle type: {self._motor_type}"

    def set_type(self, vehicle_type):
        self._motor_type = vehicle_type

    def get_type(self):
        return self._motor_type


class Electric(Vehicle):
    """Derived class from Vehicle for Electric."""
    def __init__(self, brand, model, year, color, doors, sun_roof, engine, tires, price_per_day, electric_type):
        super().__init__(brand, model, year, color, doors, sun_roof, engine, tires, price_per_day)
        self._electric_type = electric_type

    def display_info(self):
        """Displays electric information including electric type"""
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Electric type: {self._electric_type}"

    def set_type(self, vehicle_type):
        self._electic_type = vehicle_type

    def get_type(self):
        return self._electric_type


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
        self.vehicle = vehicle   # An instance of vehicle
        self.rental_date = rental_date
        self.return_date = return_date

    def rental_contract(self):
        date_dif = days_between_dates(self.rental_date, self.return_date)
        price = date_dif * self.vehicle.get_price()
        contract = (f"Rental Contract\n"
                    f"Customer: {self.customer}\n"
                    f"Vehicle:\n{self.vehicle.display_info()}\n"
                    f"Rental Date: {self.rental_date}\n"
                    f"Return Date: {self.return_date}\n"
                    f"Price: {price}")
        print(contract)


# Usage example

# Creating a car class
car1 = Car("Toyota", "Camry", 2021, "black", 4, "yes", "1.6L", 4, 300, "Sedan")
print(car1.display_info())
print()

# Creating a rental class
my_rental = Rental("Ray Chen", car1, "2/12/2024", "2/15/2024")
my_rental.rental_contract()
print()

# Modify the price
car1.set_price(350)
print(car1.display_info())
