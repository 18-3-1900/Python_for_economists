"""Assignment: Administration
Created on 27 june 2021
Author: Jelmer Haverkate"""

# This program reads the registration files of two detectors as input
# and print the license plates of all cars that are between the two sensors and a list of cars that have been speeding.

SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60
SPEED_LIMIT_IN_KM_PER_HOUR = 50
DISTANCE_BETWEEN_SENSORS_IN_METER = 200
METER_PER_SECOND_TO_KM_PER_HOUR = 3.6


def speed(time_sensor_1, time_sensor_2):
    speed_in_meter_per_second = DISTANCE_BETWEEN_SENSORS_IN_METER / (time_sensor_2 - time_sensor_1)
    speed_in_km_per_hour = speed_in_meter_per_second * METER_PER_SECOND_TO_KM_PER_HOUR
    return speed_in_km_per_hour


def car_speeding(car, time_sensor_1, time_sensor_2):
    if speed(time_sensor_1, time_sensor_2) > SPEED_LIMIT_IN_KM_PER_HOUR:
        return "%s - %d km/h\n" % (car, speed(time_sensor_1, time_sensor_2))


def sort_fastest_to_slowest(input_cars):
    cars = input_cars.splitlines()
    cars_sorted = {}
    for car in cars:
        car_and_speed = car.split(" - ")
        license_plate = car_and_speed[0]
        speediness = int(car_and_speed[1].split()[0])
        cars_sorted[license_plate] = speediness
    cars_sorted = sorted(cars_sorted, key=cars_sorted[license_plate], reverse=True)
    print(cars_sorted)


def cars_between_sensors_or_speeding(dictionary_sensor_1, dictionary_sensor_2):
    print("The following cars are currently between the two sensors:")
    cars_speeding = {}

    for car in dictionary_sensor_1:

        if car not in dictionary_sensor_2:
            print(car)
        elif car_speeding(car, dictionary_sensor_1[car], dictionary_sensor_2[car]) is not None:
            cars_speeding += car_speeding(car, dictionary_sensor_1[car], dictionary_sensor_2[car])

    print("\nThe following cars went over the speed limit:")
    print(cars_speeding)


def hh_mm_ss_to_seconds(hh_mm_ss):
    hours_in_seconds = int(hh_mm_ss[0]) * SECONDS_PER_HOUR
    minutes_in_seconds = int(hh_mm_ss[1]) * SECONDS_PER_MINUTE
    total_seconds = hours_in_seconds + minutes_in_seconds + int(hh_mm_ss[2])
    return total_seconds


def progressing_input_sensor(input_sensor):
    sensor = {}
    for line in input_sensor:
        sensor_time_and_license_plate = line.split()
        sensor_time_hh_mm_ss = sensor_time_and_license_plate[0]
        sensor_time_in_seconds = hh_mm_ss_to_seconds(sensor_time_hh_mm_ss.split(":"))
        sensor_license_plate = sensor_time_and_license_plate[1]
        sensor[sensor_license_plate] = sensor_time_in_seconds

    return sensor


def report_cars_speeding(input_sensor_1, input_sensor_2):
    sensor_1 = progressing_input_sensor(input_sensor_1)
    sensor_2 = progressing_input_sensor(input_sensor_2)
    cars_between_sensors_or_speeding(sensor_1, sensor_2)


lines_sensor_1 = open("input_b_sensor_1.txt").read().splitlines()
lines_sensor_2 = open("input_b_sensor_2.txt").read().splitlines()

report_cars_speeding(lines_sensor_1, lines_sensor_2)
