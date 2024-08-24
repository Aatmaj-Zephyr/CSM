import random

global total_utilization_loader
total_utilization_loader = [0, 0]
global total_utilization_scaler
total_utilization_scaler = 0


class truck:
    probability = [0.4, 0.3, 0.2, 0.1]
    time_required = [40, 60, 80, 100]

    def __init__(self, name) -> None:
        self.time_left = -1
        self.name = name

    def advance(self):
        if self.time_left == -1:
            self.time_left = random.choices(
                self.time_required, self.probability, k=1)[0]

            print(f"Truck {self.name} has started journey.")
            print(
                f"Truck {self.name} will finish journey after {self.time_left} minutes.")
        self.time_left -= 1
        if self.time_left == 0:
            load_waiting_queue.append(self)
            print(f"Truck {self.name} has reached.")
            self.time_left = -1


class scale:
    probability = [0.7, 0.3]
    time_required = [12, 16]
    process_queue = []

    def __init__(self) -> None:
        self.time_left = 0

    def advance(self):
        global total_utilization_scaler  # Declare global

        self.time_left -= 1
        if self.time_left <= 0:
            if len(self.process_queue) != 0:
                truck_to_be_removed = self.process_queue.pop()
                print(f"Truck {truck_to_be_removed.name} has left scaler")
                travel_waiting_queue.append(truck_to_be_removed)

            if len(scale_waiting_queue) != 0:
                if len(self.process_queue) == 0:
                    truck_to_be_added = scale_waiting_queue.pop()
                print(
                    f"Truck {truck_to_be_added.name} has been taken in for scaling")
                self.process_queue.append(truck_to_be_added)
                self.time_left = random.choices(
                    self.time_required, self.probability, k=1)[0]

                total_utilization_scaler += self.time_left
                print(
                    f"Truck {truck_to_be_added.name} will leave scaler after {self.time_left} minutes")


class loader:
    probability = [0.3, 0.6, 0.2]
    time_required = [5, 10, 15]
    process_queue = [[], []]

    def __init__(self) -> None:
        self.time_left = [0, 0]

    def advance(self):
        self.time_left[0] -= 1
        self.time_left[1] -= 1

        if self.time_left[0] <= 0 and len(load_waiting_queue) != 0:
            if len(self.process_queue[0]) != 0:
                truck_to_be_removed = self.process_queue[0].pop()
                print(f"Truck {truck_to_be_removed.name} has left loader 1")
                scale_waiting_queue.append(truck_to_be_removed)
            truck_to_be_added = load_waiting_queue.pop()
            self.process_queue[0].append(truck_to_be_added)
            print(
                f"Truck {truck_to_be_added.name} has been taken in for loading by loader 1")
            self.time_left[0] = random.choices(
                self.time_required, self.probability, k=1)[0]
            total_utilization_loader[0] += self.time_left[0]
            print(
                f"Truck {truck_to_be_added.name} will leave loader 1 after {self.time_left[0]} minutes")

        if self.time_left[1] <= 0 and len(load_waiting_queue) != 0:
            if len(self.process_queue[1]) != 0:
                truck_to_be_removed = self.process_queue[1].pop()
                print(f"Truck {truck_to_be_removed.name} has left loader 2")
                scale_waiting_queue.append(truck_to_be_removed)
            truck_to_be_added = load_waiting_queue.pop()
            self.process_queue[1].append(truck_to_be_added)
            print(
                f"Truck {truck_to_be_added.name} has been taken in for loading by loader 2")

            self.time_left[1] = random.choices(
                self.time_required, self.probability, k=1)[0]
            total_utilization_loader[1] += self.time_left[1]
            print(
                f"Truck {truck_to_be_added.name} will leave loader 2 after {self.time_left[1]} minutes")


global load_waiting_queue
load_waiting_queue = []
global scale_waiting_queue
scale_waiting_queue = []
global travel_waiting_queue
travel_waiting_queue = []

myloader = loader()
myscale = scale()
load_waiting_queue = [truck(f"{i}") for i in range(6)]

for t in range(150):
    print(f"time = {t}")
    myloader.advance()
    myscale.advance()
    for running_truck in travel_waiting_queue:
        running_truck.advance()

print(total_utilization_loader)
print(total_utilization_scaler)
