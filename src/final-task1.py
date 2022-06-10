a = []
b = []
str_list = []

def read_txt(list, filename, sep):
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        try:
            x, y = line.split(sep)
            list.append((int(x), y))
        except:
            continue
    
    f.close()

def build_list():
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][0] == b[j][0]:
                str_list.append((a[i][1], b[j][1]))

if __name__ == '__main__':
    read_txt(a, 'a.txt', ',')
    read_txt(b, 'b.txt', ' ')
    build_list()
    print(str_list)
