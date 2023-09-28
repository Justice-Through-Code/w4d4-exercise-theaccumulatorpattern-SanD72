
'''
    You are given a list of temperature readings in Celsius for a week. Your task is to implement a function that calculates and returns the average temperature for the week. To achieve this, you will use the accumulator pattern to accumulate the sum of temperatures and then calculate the average.

    Input

    A list temperatures containing n floating-point numbers representing the temperature readings for the week.
    (1 <= n <= 7, -20 <= temperatures[i] <= 40)
    
    Input Example
    temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0]

    Output

    A single floating-point number representing the calculated average temperature.
    Example Output
    22.357142857142858

'''
# Take this to OH, email Dario maybe I'm not ready for all this.

from typing import List
# S~ list imported
# exercise started in pod with james hoholik, eddie menefee, and andrew borda.
# resources I used were docs.python.org, stackoverflow, and chat gpt ended up throwing out suggestions to K.I.S.S. why is simple so hard? 
#temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0]
#temperatures = []

def calculate_average_temperature(temperatures: List[float]) -> float:
  
     # 1.1 TODO: # Initialize an accumulator variable to keep track of the sum of temperatures.
    temp_sum = 0
    
    # 1.2 TODO:# Iterate through the `temperatures` list, updating the accumulator with the current temperature.
    for temp in temperatures:
            temp_sum += temp #adding current temp to sum
    if len(temperatures) == 0:
          print('The list is empty.')
    else:
          
          
    # 1.3 TODO: # Calculate and return the average temperature using the accumulated sum and the total number of readings.
    #take total numbers of current temps in list and divide total sum by of temps.
        ave_temp = (temp_sum/ len(temperatures))

    
    # 1.3 TODO: return the average temperature
        return (ave_temp)
# calculate_average_temperature()  
