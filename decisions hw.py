
#User info
average_speed = float(input('Enter your average speed (mph):  '))
speed_limit = float(input('Enter the speed limit (mph):  '))
distance = float(input('Enter the distance traveled (miles):  '))

#Calculate time of average speed
actual_time = distance / average_speed

#Calculate time of speed limit
speed_limit_time = distance / speed_limit

# Calculate time saved in hours
time_saved = (speed_limit_time - actual_time) * 60

#Display results
print(f'Time saved: {time_saved:.0f} minutes')
