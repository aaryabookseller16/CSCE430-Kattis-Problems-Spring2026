import math

spoke_count, ring_count, city_radius = input().split()
spoke_count = int(spoke_count)
ring_count = int(ring_count)
city_radius = float(city_radius)
start_spoke, start_ring, end_spoke, end_ring = map(int, input().split())
ring_width = city_radius / ring_count
angle_between_points = abs(start_spoke - end_spoke) * math.pi / spoke_count
best_distance = 10 ** 20

for meeting_ring in range(ring_count + 1):
    radial_part = abs(start_ring - meeting_ring) * ring_width + abs(end_ring - meeting_ring) * ring_width
    arc_radius = meeting_ring * ring_width
    curved_part = arc_radius * angle_between_points
    total_distance = radial_part + curved_part
    if total_distance < best_distance:
        best_distance = total_distance
    # print("ring", meeting_ring, radial_part, curved_part, total_distance)

print(best_distance)
