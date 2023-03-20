print("Введите два цвета для смешивания")
color1 = input().strip().lower()
color2 = input().strip().lower()

blender = tuple(sorted([color1, color2]))

res = {
    ('красный', 'синий'): 'фиолетовый',
    ('желтый', 'красный'): 'оранжевый',
    ('желтый', 'синий'): 'зеленый',
}

if blender in res:
    print("Получившийся цвет: ", res[blender])
else:
    print("Ошибка, смешивание данных цветов не предусмотрено")


