# The number of cars.
cars = 100
# The numbers of spaces in a car.
space_in_a_car = 4.0
# Number of drivers.
drivers = 30
# Number of passengers.
passengers = 90
# Excess cars not driven.
cars_not_driven = cars - drivers
# Number of cars being driven.
cars_driven = drivers
# Total number of spaces.
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers per car.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."