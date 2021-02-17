from Utils.Array import input_array

# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


ARRIVAL = "ARRIVAL"
DEPARTURE = "DEPARTURE"
"""
Let the two arrays are of size n & m
Time  : O(K log K)        where k = n+m       because we are soring an array that contains elements of both the array
Space : O(k)

This same approach can be applied with a little better time complexity,
so if we don't put all the elements in one big array then we will be having the sorting in     O(n lg n) + O(m lg m)

Also, then to know if the event is corresponding to the ARRIVAL or DEPARTURE, we would not require to do mapping
we would know, from the array we are reading, if we are reading from arrivals array it will be an arrival event
and if we are reading form departure array it will be a departure event 
"""


def minimum_platforms(arrivals, departures) -> int:
    arrivals_mapped = [(arrival, ARRIVAL) for arrival in arrivals]
    departures_mapped = [(departure, DEPARTURE) for departure in departures]
    time_status_mapping = arrivals_mapped + departures_mapped  # concatenating it all in one array
    time_status_mapping.sort(key=lambda time_status: time_status[0])  # sorting on time, which is first element
    # print(time_status_mapping)

    max_arrivals = float("-inf")
    curr_arrivals = 0
    for time_status in time_status_mapping:
        status = time_status[1]
        if status == ARRIVAL:
            curr_arrivals += 1
        elif status == DEPARTURE:
            curr_arrivals -= 1
        else:
            print("Invalid Status")

        max_arrivals = max(max_arrivals, curr_arrivals)

    return max_arrivals


if __name__ == '__main__':
    arrival_times = input_array()
    departure_times = input_array()
    min_platforms = minimum_platforms(arrival_times, departure_times)
    print(min_platforms)

"""
arrival   = [0900 0940 0950 1100 1500 1800]
departure = [0910 1200 1120 1130 1900 2000]
3 

arrival   = [900  940] 
departure = [910  1200]
1
"""
