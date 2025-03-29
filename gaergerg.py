import tkinter as tk

# Настройки окна
width, height = 800, 600
ball_radius = 10
paddle_width = 100
paddle_height = 10

# Начальные параметры мячика
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 4
ball_speed_y = 4

# Параметры ракетки
paddle_x = (width - paddle_width) // 2
paddle_y = height - 30

# Счёт
score = 0

# Функция для обновления позиции мячика и ракетки
def update_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_x, score

    # Обновление позиции мячика
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Проверка на столкновение со стенами
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x  # Изменение направления по оси X
    if ball_y - ball_radius < 0:
        ball_speed_y = -ball_speed_y  # Изменение направления по оси Y
    if ball_y + ball_radius > height:
        # Если мячик упал ниже ракетки, обнуляем счёт
        score = 0
        reset_ball()

    # Проверка на столкновение с ракеткой
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y + ball_radius < paddle_y + paddle_height):
        ball_speed_y = -ball_speed_y  # Изменение направления по оси Y
        score += 1  # Увеличиваем счёт

    # Очистка канваса и рисование мячика и ракетки
    canvas.delete("all")
    canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius,
                       ball_x + ball_radius, ball_y + ball_radius,
                       fill="white")
    canvas.create_rectangle(paddle_x, paddle_y,
                            paddle_x + paddle_width, paddle_y + paddle_height,
                            fill="white")

    # Отображение счёта
    canvas.create_text(50, 20, text=f"Score: {score}", fill="white", font=("Arial", 16))

    # Запланировать следующий вызов функции
    root.after(30, update_game)

# Функция для сброса мячика в центр
def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = width // 2
    ball_y = height // 2
    ball_speed_x = 4
    ball_speed_y = 4

# Функция для управления ракеткой
def move_paddle(event):
    global paddle_x
    if event.keysym == "Left" and paddle_x > 0:
        paddle_x -= 20
    elif event.keysym == "Right" and paddle_x < width - paddle_width:
        paddle_x += 20

# Создание основного окна
root = tk.Tk()
root.title("Пинг-понг со счётчиком")

# Создание канваса для рисования
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

# Привязка клавиш к функции управления ракеткой
root.bind("<Key>", move_paddle)

# Запуск анимации
update_game()

# Запуск основного цикла приложения
root.mainloop()