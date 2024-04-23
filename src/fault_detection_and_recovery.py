# fault_detection_and_recovery.py

import time
import logging

class Subsystem:
    def __init__(self, name):
        self.name = name
        self.status = "Normal"
        self.fault_history = []

    def check_status(self):
        # Simulate checking the subsystem's status
        if self.status == "Normal":
            if time.time() % 10 == 0:
                self.status = "Fault"
                self.fault_history.append(f"{time.ctime()} - Fault detected")
                logging.warning(f"Fault detected in {self.name} subsystem")
        elif self.status == "Fault":
            if time.time() % 5 == 0:
                self.status = "Normal"
                self.fault_history.append(f"{time.ctime()} - Fault recovered")
                logging.info(f"Fault recovered in {self.name} subsystem")

    def get_status(self):
        return self.status

    def get_fault_history(self):
        return self.fault_history

class Spacecraft:
    def __init__(self):
        self.subsystems = [
            Subsystem("Propulsion"),
            Subsystem("Power"),
            Subsystem("Communication"),
            Subsystem("Navigation"),
            Subsystem("Payload")
        ]

    def monitor_health(self):
        for subsystem in self.subsystems:
            subsystem.check_status()

    def diagnose_faults(self):
        faulty_subsystems = [subsystem for subsystem in self.subsystems if subsystem.get_status() == "Fault"]
        return faulty_subsystems

    def execute_recovery(self, subsystem):
        # Simulate executing recovery procedures for the given subsystem
        if subsystem.get_status() == "Fault":
            time.sleep(1)  # Simulate recovery time
            subsystem.status = "Normal"
            subsystem.fault_history.append(f"{time.ctime()} - Recovery executed")
            logging.info(f"Recovery executed for {subsystem.name} subsystem")

if __name__ == '__main__':
    logging.basicConfig(filename='fault_log.log', level=logging.INFO)
    spacecraft = Spacecraft()

    while True:
        spacecraft.monitor_health()
        faulty_subsystems = spacecraft.diagnose_faults()
        if faulty_subsystems:
            for subsystem in faulty_subsystems:
                spacecraft.execute_recovery(subsystem)
        time.sleep(1)
