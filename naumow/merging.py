
def merge(filename1, filename2, filename3):
    try:
        file1 = open(filename1, 'r', encoding="UTF-8")
        file2 = open(filename2, 'r', encoding="UTF-8")
        file3 = open(filename3, 'w', encoding="UTF-8")

        for line1 in file1.readlines():
            line2 = file2.readline()
            file3.write(line1)
            file3.write(line2)


    finally:
        file1.close()
        file2.close()
        file3.close()


merge("input.txt", "output.txt", "asf.txt")
