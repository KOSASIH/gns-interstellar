import time

class PowerManager:
    """
    A class to manage power usage in a spacecraft.

    Attributes:
    power_capacity (int): The total power capacity of the spacecraft.
    power_usage (int): The current power usage of the spacecraft.
    power_threshold (int): The power usage threshold at which warnings are issued.
    """

    def __init__(self, power_capacity, power_threshold):
        """
        Initializes the PowerManager object.

        Parameters:
        power_capacity (int): The total power capacity of the spacecraft.
        power_threshold (int): The power usage threshold at which warnings are issued.
        """
        self.power_capacity = power_capacity
        self.power_usage = 0
        self.power_threshold = power_threshold

    def use_power(self, power_amount):
        """
        Uses a specified amount of power.

        Parameters:
        power_amount (int): The amount of power to be used.

        Returns:
        None
        """
        if power_amount + self.power_usage > self.power_capacity:
            raise ValueError("Power usage exceeds capacity.")
        self.power_usage += power_amount

    def stop_using_power(self, power_amount):
        """
        Stops using a specified amount of power.

        Parameters:
        power_amount (int): The amount of power to stop using.

        Returns:
        None
        """
        if power_amount > self.power_usage:
            raise ValueError("Power usage is less than specified amount.")
        self.power_usage -= power_amount

    def check_power_usage(self):
        """
        Checks the current power usage and issues warnings if necessary.

        Returns:
        None
        """
        if self.power_usage > self.power_threshold:
            print(f"Power usage is at {self.power_usage} out of {self.power_capacity}. Warning: power usage is high.")
        elif self.power_usage == self.power_threshold:
            print(f"Power usage is at {self.power_usage} out of {self.power_capacity}. Warning: power usage is at the threshold.")

class SolarPanel:
    """
    A class to model a solar panel.

    Attributes:
    power_output (int): The current power output of the solar panel.
    """

    def __init__(self):
        """
        Initializes the SolarPanel object.
        """
        self.power_output = 0

    def generate_power(self):
        """
        Generates power from the solar panel.

        Returns:
        int: The amount of power generated.
        """
        self.power_output = 10
        return self.power_output

class Battery:
    """
    A class to model a battery.

    Attributes:
    power_capacity (int): The total power capacity of the battery.
    power_level (int): The current power level of the battery.
    """

    def __init__(self, power_capacity):
        """
        Initializes the Battery object.

        Parameters:
        power_capacity (int): The total power capacity of the battery.
        """
        self.power_capacity = power_capacity
        self.power_level = 0

    def charge(self, power_amount):
        """
        Charges the battery with a specified amount of power.

        Parameters:
        power_amount (int): The amount of power to be charged.

        Returns:
        None
        """
        if power_amount > self.power_capacity - self.power_level:
            raise ValueError("Power level exceeds capacity.")
        self.power_level += power_amount

    def discharge(self, power_amount):
        """
        Discharges the battery with a specified amount of power.

        Parameters:
        power_amount (int): The amount of power to be discharged.

        Returns:
        None
        """
        if power_amount > self.power_level:
            raise ValueError("Power level is less than specified amount.")
        self.power_level -= power_amountclass PowerSystem:
    """
    A class to manage the power system of a spacecraft.

    Attributes:
    power_manager (PowerManager): The power manager for the spacecraft.
    solar_panels (list): The solar panels on the spacecraft.
    batteries (list): The batteries on the spacecraft.
    """

    def __init__(self, power_capacity, power_threshold, solar_panel_count, battery_count, battery_capacity):
        """
        Initializes the PowerSystem object.

        Parameters:
        power_capacity (int): The total power capacity of the spacecraft.
        power_threshold (int): The power usage threshold at which warnings are issued.
        solar_panel_count (int): The number of solar panels on the spacecraft.
        battery_count (int): The number of batteries on the spacecraft.
        battery_capacity (int): The total power capacity of each battery.
        """
        self.power_manager = PowerManager(power_capacity, power_threshold)
        self.solar_panels = [SolarPanel() for _ in range(solar_panel_count)]
        self.batteries = [Battery(battery_capacity) for _ in range(battery_count)]

    def update_power_generation(self):
        """
        Updates the power generation from the solar panels.

        Returns:
        None
        """
        for solar_panel in self.solar_panels:
            self.power_manager.use_power(solar_panel.generate_power())

    def charge_batteries(self):
        """
        Charges the batteries with excess power.

        Returns:
        None
        """
        excess_power = self.power_manager.power_usage - self.power_manager.power_capacity
        for battery in self.batteries:
            if excess_power > 0:
                battery.charge(min(excess_power, battery.power_capacity - battery.power_level))
                excess_power -= battery.power_capacity - battery.power_level
            else:
                break

    def discharge_batteries(self):
        """
        Discharges the batteries to supply power.

        Returns:
        None
        """
        power_deficit = self.power_manager.power_capacity - self.power_manager.power_usage
        for battery in self.batteries:
            if power_deficit > 0:
                battery.discharge(min(power_deficit, battery.power_level))
                power_deficit -= battery.power_level
            else:
                break

    def check_power_system(self):
        """
        Checks the power system and issues warnings if necessary.

        Returns:
        None
        """
        self.power_manager.check_power_usage()
        for battery in self.batteries:
            if battery.power_level == 0:
                print(f"Battery {battery} is empty.")
            elif battery.power_level == battery.power_capacity:
                print(f"Battery {battery} is full.")
