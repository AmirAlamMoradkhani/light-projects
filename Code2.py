def min_steps_to_target(N, start, end):
    # تمامی حرکت‌های ممکن اسب
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

    # صف برای ذخیره مکان‌ها و تعداد قدم‌ها
    queue = [(start[0], start[1], 0)]
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.pop(0)  # اولین عنصر را از صف خارج کن

        if (x, y) == end:
            return steps

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1  # اگر به هدف نرسید

# مقادیر ورودی
N = 8  # اندازه تخته شطرنج
start = (2, 3)
end = (6, 6)

# محاسبه تعداد قدم‌های حداقل
steps = min_steps_to_target(N, start, end)
print("Minimum steps required:", steps)
