row_count, column_count = map(int, input().split())
row_sums = list(map(int, input().split()))
column_sums = list(map(int, input().split()))
possible = True
if sum(row_sums) != sum(column_sums):
    possible = False

row_sums.sort(reverse=True)
if possible:
    for row_need in row_sums:
        column_sums.sort(reverse=True)
        if row_need > column_count:
            possible = False
            break
        for column_number in range(row_need):
            column_sums[column_number] = column_sums[column_number] - 1
            if column_sums[column_number] < 0:
                possible = False
                break
        # print("after row", row_need, column_sums)
        if possible == False:
            break
if possible and sum(column_sums) == 0:
    print("Yes")
else:
    print("No")
