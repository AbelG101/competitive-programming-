number_of_stops = int(input())
total_passengers = 0
max_tram_capacity = 0
for i in range(number_of_stops-1):
  out, _in = input().split()
  total_passengers += int(_in) - int(out)
  max_tram_capacity = max(max_tram_capacity, total_passengers)

print(max_tram_capacity)
