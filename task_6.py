def greedy_algorithm(items, budget):
    sorted_items = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        sorted_items.append((name, info["cost"], info["calories"], ratio))
    
    sorted_items.sort(key=lambda x: x[3], reverse=True)
    
    chosen_items = []
    total_calories = 0
    remaining_budget = budget
    
    for name, cost, calories, ratio in sorted_items:
        if remaining_budget >= cost:
            chosen_items.append(name)
            total_calories += calories
            remaining_budget -= cost
            
    return {
        "items": chosen_items,
        "total_calories": total_calories,
        "remaining_budget": remaining_budget
    }


def dynamic_programming(items, budget):
    item_list = [(name, info["cost"], info["calories"]) for name, info in items.items()]
    n = len(item_list)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, cost, calories = item_list[i - 1]
        for w in range(budget + 1):
            # Якщо поточна страва коштує більше, ніж поточний проміжний бюджет
            if cost > w:
                dp[i][w] = dp[i - 1][w]  # Просто копіюємо попередній найкращий результат
            else:
                # Вибираємо максимум: або НЕ брати страву, або взяти її (додавши її калорії 
                # до оптимального результату для залишку бюджету w - cost)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
                
    # Відновлення відповіді (розкручуємо таблицю назад, щоб знайти які саме страви ми взяли)
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        # Якщо значення змінилося порівняно з попереднім рядком — ми взяли цей предмет
        if dp[i][w] != dp[i - 1][w]:
            name, cost, calories = item_list[i - 1]
            chosen_items.append(name)
            w -= cost  # Зменшуємо залишок бюджету
            
    chosen_items.reverse()
    
    return {
        "items": chosen_items,
        "total_calories": dp[n][budget],
        "remaining_budget": w
    }


# === ДЕМОНСТРАЦІЯ РОБОТИ ===
if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    # Задамо тест для бюджету, де алгоритми дадуть РІЗНИЙ результат (наприклад, бюджет 60)
    test_budget = 60
    
    print(f"--- Результати тестування для бюджету: {test_budget} ---")
    
    greedy_res = greedy_algorithm(items, test_budget)
    print("\n[Жадібний алгоритм]:")
    print(f"  Обрані страви: {greedy_res['items']}")
    print(f"  Сумарна калорійність: {greedy_res['total_calories']}")
    print(f"  Залишок бюджету: {greedy_res['remaining_budget']}")
    
    dp_res = dynamic_programming(items, test_budget)
    print("\n[Динамічне програмування]:")
    print(f"  Обрані страви: {dp_res['items']}")
    print(f"  Сумарна калорійність: {dp_res['total_calories']}")
    print(f"  Залишок бюджету: {dp_res['remaining_budget']}")
