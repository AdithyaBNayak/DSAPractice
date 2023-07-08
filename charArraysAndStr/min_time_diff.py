# Minimum Time Differences
"""
Given a list of 24-hour clock time points in "HH-MM" format,
Return the minimum minutes difference between any two time-point in list 

arr1 = ['23:59','00.00']
output = 1

arr2 = ['00.00','23:59','00.00']
output = 0
"""

# Function Definition
def min_time_diff(times):

    # Step1: Convert the time into minutes array
    mins = []
    for i in range(len(times)):
        mins.append(int(times[i][0:2])*60 + int(times[i][3:5]))
    
    # Step2: Sort the array
    mins = sorted(mins)

    # Step3: Check for minimum
    minimum = mins[1] - mins[0]
    for j in range(1,len(mins)-1):
        minimum = min(minimum, mins[j+1] - mins[j])

    # Step4: Important step (if time is ['23:59','00:00'])
    lastDiff1 = (mins[0] +  1440) - mins[len(mins)-1]
    # 23:59 is 1439

    # But in case 1st ele is 10 and last ele is 700
    lastDiff2 = mins[len(mins)-1] - mins[0]
    lastDiff = min(lastDiff1,lastDiff2)
    minimum = min(lastDiff, minimum)

    return minimum

# Driver Code
times1 = ['23:59','00.00']
times2 = ['00.00','23:59','00.00']
print(min_time_diff(times1))