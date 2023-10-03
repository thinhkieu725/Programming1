"""
COMP.CS.100 Programming 1
6.0.Project_WeatherStatistics.py
Creator: Thinh Kieu
Student number: 152167613

The program reads inputs for temperatures of days and gives back the analysis based on mean and median values.
"""

def input_temperatures(numberOfDays):
    """
    read the inputs for temperatures from the user
    variables: numberOfDays _ int _ the number of days for calculation
    return: temperatures _ list _ a list of temperatures corresponding to the days
    """
    temperatures = []
    for i in range(numberOfDays):
        temp = input (f"Enter day {i+1}. temperature in Celcius: ")
        temperatures.append(float(temp))

    return temperatures

def mean(listOfNumbers):
    """
    calculate the mean of a list of numbers
    variables: listOfNumbers _ list _ a list of numbers to be calculated
    return: float _ the median of the list
    """
    return sum(listOfNumbers) / len(listOfNumbers)

def median(listOfNumbers):
    """
    calculate the median of a list of numbers
    variables: listOfNumbers _ list _ a list of numbers to be calculated
    return: float _ the median of the list
    """
    sortedNumbers = sorted(listOfNumbers)
    l = len(sortedNumbers)
    if l == 0:
        print("ERROR in calculating the median value: list of numbers is empty.")
        return 0
    if l % 2 == 1:
        return sortedNumbers[l//2]
    else:
        return (sortedNumbers[l//2 -1] + sortedNumbers[l//2])/2

def print_temperatures(temperatures, day, tMean):
    """
    print out the temperatures corresponding to the day and its difference to the mean temperature
    variables:
        temperatures _ list _ list of temperatures
        day _ int _ the inquired day
        tMean _ float _ the mean temperature
    return: none
    """
    # calculate the difference between the temperature of the dasy and the mean temperature
    difference = temperatures[day - 1] - tMean
    print(f"Day{day:3d}.{temperatures[day-1]:6.1f}C difference to mean:{difference:6.1f}C")

def main():
    numberOfDays = input("Enter amount of days: ")
    numberOfDays = int(numberOfDays)

    temperatures = input_temperatures(numberOfDays)

    # Calculating the mean temperature
    tMean = mean(temperatures)

    # Calculating the median temperature
    tMedian = median(temperatures)

    # Print mean and median temperature
    print()
    print(f"Temperature mean: {tMean:.1f}C")
    print(f"Temperature median: {tMedian:.1f}C")

    # Print out the result by 2 groups
    print()
    print("Over or at median were:")
    for i in range(numberOfDays):
        if temperatures[i] >= tMedian:
            print_temperatures(temperatures, i+1, tMean)

    print()
    print("Under median were:")
    for i in range(numberOfDays):
        if temperatures[i] < tMedian:
            print_temperatures(temperatures, i+1, tMean)

if __name__ == "__main__":
    main()
