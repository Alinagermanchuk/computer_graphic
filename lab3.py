from PIL import Image, ImageDraw
import os


def rotate(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def jarvis(cords):
    n = len(cords)
    P = list(range(n))
    for i in range(1, n):
        if cords[P[i]][0] < cords[P[0]][0]:
            P[i], P[0] = P[0], P[i]
    RESULT = [P[0]]
    del P[0]
    P.append(RESULT[0])
    while True:
        r = 0
        for i in range(1, len(P)):
            if rotate(cords[RESULT[-1]], cords[P[r]], cords[P[i]]) < 0:
                r = i
        if P[r] == RESULT[0]:
            break
        else:
            RESULT.append(P[r])
            del P[r]
    return RESULT


def draw_pic(path):
    if not(os.path.isfile(path)):
        input(f"Ошибка в названии файла: '{path}'\nОн должен быть в той же папке, что и программа!\n")
        return -1
    file = open(path, "r")
    size = (960, 540)
    img = Image.new("RGB", size, color="white")
    draw = ImageDraw.Draw(img)

    coordinates = []
    for line in file:
        line = line[:-1].split(" ")
        if not(line[0].isdigit()) or not(line[1].isdigit()):
            file.close()
            input("В файле недопустимые координаты!\n")
            break
        coordinates.append((int(line[1]), size[1]-int(line[0])))
        img.putpixel(coordinates[-1], (0, 0, 0))

    c_hull = jarvis(coordinates)
    for i in range(len(c_hull) - 1):
        draw.line((coordinates[c_hull[i]], coordinates[c_hull[i + 1]]), fill=(0,0,255), width=4)
    draw.line((coordinates[c_hull[0]], coordinates[c_hull[-1]]), fill=(0,0,255), width=4)
    file.close()

    img_name = path[:-4]+".png"
    img.save(img_name)
    os.startfile(img_name)
    input(f"Успешно выполнено! Файл сохранён как '{img_name}'!")


draw_pic(input("Введите название файла: "))



