import cv2

# Инициализируем камеру
cap = cv2.VideoCapture(0)

while True:
    # Читаем кадр с камеры
    ret, frame = cap.read()
    
    # Если кадр прочитан успешно, то отображаем его и сохраняем в файл
    if ret:
        cv2.imshow('Camera', frame)
        cv2.imwrite(f'photo.jpg', frame)
    
    # Если нажата клавиша 'q', то выходим из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
