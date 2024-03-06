def draw_xyz(N):
    letters = ['Y', 'Z', 'X']
    pattern = ""
    for i in range(N):
        row = ""
        for j in range(N):
            letter = letters[(i + j) % 3]
            row += letter + " "
        pattern += row.strip() + "\n"
    return pattern.strip()

print(draw_xyz(3))
print(draw_xyz(5))