import math

spoke_count, ring_count, city_radius = input().split()
spoke_count = int(spoke_count)
ring_count = int(ring_count)
city_radius = float(city_radius)

start_spoke, start_ring, end_spoke, end_ring = map(int, input().split())

ring_width = city_radius / ring_count
angle_between_points = abs(start_spoke - end_spoke) * math.pi / spoke_count

center_distance = (start_ring + end_ring) * ring_width

outer_ring_to_try = min(start_ring, end_ring)
outer_radial_part = (start_ring - outer_ring_to_try) * ring_width + (end_ring - outer_ring_to_try) * ring_width
outer_arc_part = outer_ring_to_try * ring_width * angle_between_points
outer_distance = outer_radial_part + outer_arc_part

# print("center", center_distance, "outer-ish", outer_distance)

if center_distance < outer_distance:
    print(center_distance)
else:
    print(outer_distance)
