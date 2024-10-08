# Захват веб-камеры
import cv2

# Инициализируем камеру
cap = cv2.VideoCapture(0)

while True:
    # Читаем кадр с камеры
    ret, frame = cap.read()
    
    # Если кадр прочитан успешно, то отображаем его
    if ret:
        cv2.imshow('Camera', frame)
    
    # Если нажата клавиша 'q', то выходим из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
