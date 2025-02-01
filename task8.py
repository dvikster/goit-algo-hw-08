import heapq

def minimal_merge_cost(cables):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0
    merge_order = []  # Для збереження порядку об’єднання кабелів

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Дістаємо два найменші кабелі
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        cost = a + b  # Обчислюємо вартість їхнього об’єднання
        total_cost += cost
        # Додаємо результат об’єднання назад до купи
        heapq.heappush(cables, cost)
        # Зберігаємо інформацію про об’єднання
        merge_order.append((a, b, cost))
    
    return total_cost, merge_order

# Приклад використання
cables = [10, 20, 30, 40]
cost, order = minimal_merge_cost(cables)
print("Порядок об'єднання:")
for a, b, cost in order:
    print(f"Об'єднуємо кабелі довжиною {a} і {b}, вартість об'єднання: {cost}")
print("Загальні витрати:", cost)
