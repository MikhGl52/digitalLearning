# TODO Найдите количество книг, которое можно разместить на дискете

diskSize = 1.44 * 1024 ** 2  # bytes
bookSize = 100 * 50 * 25 * 4  # bytes in 1 book
print("Количество книг, помещающихся на дискету:", int(diskSize//bookSize))
