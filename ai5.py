traffic_light = input("Enter traffic light color (red/green/yellow): ").lower()
obstacle_input = input("Is there an obstacle ahead? (yes/no): ").lower()
obstacle = obstacle_input == 'yes'
speed_limit =int(input("Enter speed limit (km/h): "))
current_speed = int(input("Enter current speed (km/h): "))
print("\nEnvironmental conditions:")
print(f"Traffic light: {traffic_light}")
print(f"Obstacle ahead: {obstacle}")
print(f"Speed limit: {speed_limit} km/h")
print(f"Current speed: {current_speed} km/h")
if traffic_light == 'red' or obstacle:
    action = 'stop'
elif traffic_light == 'yellow' or current_speed > speed_limit:
    action = 'slow down'
else:
    action = 'go'
print(f"\nCar's decision: {action}") 