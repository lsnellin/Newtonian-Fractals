out = open("Fractals/1.txt")
lines = out.read()    
lines = lines.split("\n")

for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            print(i, j)
            print(int(lines[i][j]))

