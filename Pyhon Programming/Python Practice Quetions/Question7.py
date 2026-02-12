# Traffic Light Program Using if elif else statements.

# Taking input from the user for the traffic light color.
traffic_light_color = input("Enter the traffic light color (red, yellow, green): ")
# Using if elif else statements to determine the action based on the traffic light color.
if traffic_light_color.lower() == "red":  # Checking if the traffic light color is red.
    print("A Car is Coming You Should Stop")  # If the traffic light color is red, print "Stop".
elif traffic_light_color.lower() == "yellow":  # Checking if the traffic light color is yellow.
    print("Be More Caution")  # If the traffic light color is yellow, print "Caution".
elif traffic_light_color.lower() == "green":  # Checking if the traffic light color is green.
    print("You Can Go Ahead")  # If the traffic light color is green, print "Go".
else:  # If the traffic light color is not red, yellow, or green, execute this block of code.
    print("Invalid traffic light color")  # Print "Invalid traffic light color" if the input is not valid.

print("End of the program")  # Print "End of the program" to indicate that the program has ended.