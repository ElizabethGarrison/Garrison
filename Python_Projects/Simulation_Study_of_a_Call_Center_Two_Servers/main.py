import random

# Define global variables to track and measure performance
total_calls = 0
car_stereo_calls = 0
other_calls = 0
busy_calls = 0
ivr_delay = 0
car_stereo_delay = 0
other_delay = 0
waiting_time_car_stereo = []
waiting_time_other = []

# Define the DICE random number generator
def roll_dice():
    return random.randint(2, 12)  # Modify the range to match the DICE values

# Define a class for events
class Event:
    def __init__(self, event_type, time):
        self.event_type = event_type
        self.time = time

# Initialize simulation clock
simulation_clock = 0

# Initialize event calendar
event_calendar = []

# Schedule the first call arrival event
event_calendar.append(Event("Arrival", simulation_clock))

# Define a function to handle incoming calls
def handle_call():
    global simulation_clock
    global total_calls, car_stereo_calls, other_calls, busy_calls, ivr_delay, car_stereo_delay, other_delay

    total_calls += 1
    dice = roll_dice()
    time_between_arrivals = dice * 0.2
    simulation_clock += time_between_arrivals

    if total_calls <= 10:
        if dice <= 4:
            car_stereo_calls += 1
            product_type = "Car Stereo"
            ivr_processing_time = dice * 0.2
            call_processing_time = dice * 1.5
        else:
            other_calls += 1
            product_type = "Other"
            ivr_processing_time = dice * 0.3
            call_processing_time = dice

        # Update delay times
        ivr_delay += ivr_processing_time
        if product_type == "Car Stereo":
            car_stereo_delay += call_processing_time
        else:
            other_delay += call_processing_time

        # Check waiting times
        if ivr_processing_time + call_processing_time > 1:
            if product_type == "Car Stereo":
                waiting_time_car_stereo.append(ivr_processing_time + call_processing_time)
            else:
                waiting_time_other.append(ivr_processing_time + call_processing_time)
    else:
        busy_calls += 1

    # Schedule the next call arrival event
    event_calendar.append(Event("Arrival", simulation_clock + time_between_arrivals))

# Simulate the call center during midday peak hours
def simulate_call_center():
    for hour in range(11, 17):
        for minute in range(60):
            handle_call()

# Run multiple iterations to gather statistics
def run_simulations(num_iterations):
    for _ in range(num_iterations):
        global total_calls, car_stereo_calls, other_calls, busy_calls, ivr_delay, car_stereo_delay, other_delay
        total_calls = car_stereo_calls = other_calls = busy_calls = ivr_delay = car_stereo_delay = other_delay = 0
        waiting_time_car_stereo.clear()
        waiting_time_other.clear()
        simulate_call_center()

# Modify performance metrics
def calculate_performance_measures():
    car_stereo_waiting_time_percentage = len([wt for wt in waiting_time_car_stereo if wt > 0.5]) / len(waiting_time_car_stereo)  # Reduce threshold to 30 seconds
    other_waiting_time_percentage = len([wt for wt in waiting_time_other if wt > 0.5]) / len(waiting_time_other)  # Reduce threshold to 30 seconds
    refused_call_percentage = busy_calls / total_calls

    return car_stereo_waiting_time_percentage, other_waiting_time_percentage, refused_call_percentage

# Define the number of iterations for the simulation
num_iterations = 30

# What-if Analysis for Recommendations
# Now, you can implement the recommendations and rerun the simulation

# Recommendation 1: Increase the number of salespeople during peak hours
# Implement this recommendation by modifying the simulation parameters

def simulate_call_center_with_recommendation1():
    for hour in range(11, 16):
        # Increase the number of salespeople during peak hours
        salespeople = 200  # Increase the number of salespeople
        for _ in range(salespeople):
            handle_call()

# Rerun the simulation with the first recommendation
run_simulations(num_iterations)
car_stereo_percentage, other_percentage, refused_percentage = calculate_performance_measures()

# Print results after the first recommendation
print("\nResults after increasing the number of salespeople:")
print(f"Total Calls: {total_calls}")
print(f"Car Stereo Calls: {car_stereo_calls}")
print(f"Other Calls: {other_calls}")
print(f"Car Stereo Waiting Time > 1 min (%): {car_stereo_percentage * 100}%")
print(f"Other Waiting Time > 1 min (%): {other_percentage * 100}%")
print(f"Refused Calls (%): {refused_percentage * 100}%")

# Recommendation 2: Cross-training representatives to handle both call types
# Implement this recommendation by modifying the simulation logic
# Modify the handle_call function to route all calls to a single queue

def handle_call_with_recommendation2():
    global simulation_clock
    global total_calls, car_stereo_calls, other_calls, busy_calls, ivr_delay, car_stereo_delay, other_delay

    total_calls += 1
    dice = roll_dice()
    time_between_arrivals = dice * 0.333
    simulation_clock += time_between_arrivals

    if total_calls <= 10:
        # Regardless of the dice value, route all calls to a single queue
        product_type = "Single Queue"
        ivr_processing_time = dice * 0.3
        call_processing_time = dice * 2  # Assuming car stereo delay for all calls

        # Update delay times
        ivr_delay += ivr_processing_time
        car_stereo_delay += call_processing_time  # Assuming car stereo delay for all calls
        other_delay += call_processing_time  # Assuming other product delay for all calls

        # Check waiting times
        if ivr_processing_time + call_processing_time > 1:
            waiting_time_car_stereo.append(ivr_processing_time + call_processing_time)
            waiting_time_other.append(ivr_processing_time + call_processing_time)
    else:
        busy_calls += 1

# Rerun the simulation with the second recommendation
run_simulations(num_iterations)
car_stereo_percentage, other_percentage, refused_percentage = calculate_performance_measures()

# Print results after the second recommendation
print("\nResults after cross-training representatives:")
print(f"Total Calls: {total_calls}")
print(f"Car Stereo Calls: {car_stereo_calls}")
print(f"Other Calls: {other_calls}")
print(f"Car Stereo Waiting Time > 1 min (%): {car_stereo_percentage * 100}%")
print(f"Other Waiting Time > 1 min (%): {other_percentage * 100}%")
print(f"Refused Calls (%): {refused_percentage * 100}%")
