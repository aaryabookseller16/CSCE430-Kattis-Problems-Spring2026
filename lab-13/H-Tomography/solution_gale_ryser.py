row_count, column_count = map(int, input().split())

row_sums = list(map(int, input().split()))
column_sums = list(map(int, input().split()))

possible = True

if sum(row_sums) != sum(column_sums):
    possible = False

row_sums.sort(reverse=True)
column_sums.sort(reverse=True)

if possible:
    left_side = 0
    for how_many_rows in range(1, row_count + 1):
        left_side = left_side + row_sums[how_many_rows - 1]

        right_side = 0
        for column_need in column_sums:
            if column_need < how_many_rows:
                right_side = right_side + column_need
            else:
                right_side = right_side + how_many_rows

        # print("check", how_many_rows, left_side, right_side)

        if left_side > right_side:
            possible = False
            break

if possible:
    print("Yes")
else:
    print("No")
