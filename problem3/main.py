def cetak_table_perkalian(number):
    pattern = ""
    for i in range(1, number + 1):
        row = ""
        for j in range(1, number + 1):
            product = i * j
            row += "{:2d} ".format(product)
        pattern += row.strip() + "\n"
    return pattern.strip()

input_number = 9
result = cetak_table_perkalian(input_number)
print(result)