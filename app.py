#calculate avg velocity 
initial_position = float(input("Enter the initial position (in meters): "))
final_position = float(input("Enter final position (in meters): "))
time_taken = float(input("Enter the time taken (in seconds): "))
displacement = final_position - initial_position
average_velocity = displacement / time_taken 
print("The average velocity is: ", average_velocity, "meters per second")

#calculate final velocity 
initial_velocity = float(input("Enter the initial velocity (in meters per second): "))
acceleration = float(input("Enter the constant acceleration (in meters per second): "))
time_for_final_velocity = float(input("Enter the time for which acceleration occurs (in seconds): "))
final_velocity = initial_velocity + (acceleration * time_for_final_velocity)
print("The final velocity is: ", final_velocity, "meters per second")

