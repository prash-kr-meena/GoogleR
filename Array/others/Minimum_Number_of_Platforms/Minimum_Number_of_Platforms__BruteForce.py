from Utils.Array import input_array
from Utils.Range import range_overlaps


# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# Time  : O(n2)
# Space : O(1)
def minimum_platforms(arrivals, departures) -> int:
    time_range = [(arrive, depart) for arrive, depart in zip(arrivals, departures)]
    n = len(time_range)

    max_overlaps = float("-inf")

    for i in range(n):
        overlaps = 0
        for j in range(i + 1, n):
            ith_range = time_range[i]
            jth_range = time_range[j]
            if range_overlaps(ith_range[0], ith_range[1], jth_range[0], jth_range[1]):
                overlaps += 1
        max_overlaps = max(max_overlaps, overlaps)

    return max_overlaps + 1  # 1 is for the range we are checking for


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
