# Запись экрана
# Импорт библиотек
import pyautogui
import cv2
import numpy as np
 
# Установка разрешения
resolution = (1920, 1080)
 
# Установка кодека
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# Имя файла
filename = "Recording.avi"
 
# Количество кадров в секунду
fps = 20.0
 
 
# Создание объекта записи
out = cv2.VideoWriter(filename, codec, fps, resolution)
 
# Создание окна для вывода
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
 
# Делаем окно меньше
cv2.resizeWindow("Live", 480, 270)
 
while True:
    # Получаем кадр
    img = pyautogui.screenshot()
 
    # Конвертируем в нужный нам вид
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # Записываем кадр в файл
    out.write(frame)
     
    # Отображаем кадр в окне
    cv2.imshow('Live', frame)
     
    # Остановка записи клавишей 'q'
    if cv2.waitKey(1) == ord('q'):
        break
 
# Закрываем
out.release()
cv2.destroyAllWindows()
