from PIL import Image
import os


def draw_pic(path):
	if not(os.path.isfile(path)):
		input(f"Ошибка в названии файла: '{path}'\nОн должен быть в той же папке, что и программа!\n")
		return -1
	file = open(path, "r")
	size = (960, 540)
	img = Image.new("RGB", size, color="white")
	for line in file:
		line = line[:-1].split(" ")
		if not(line[0].isdigit()) or not(line[1].isdigit()): 
			file.close()
			input("В файле недопустимые координаты!\n")
			break
		img.putpixel((int(line[1]), size[1]-int(line[0])), (0, 0, 0))
	file.close()

	img_name = path[:-4]+".png"
	img.save(img_name)
	os.startfile(img_name)
	input(f"Успешно выполнено! Файл сохранён как '{img_name}'!")


draw_pic(input("Введите название файла: "))
