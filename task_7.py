import random

def dice_rolling_monte_carlo(num_rolls=1000000):
    sum_counts = {i: 0 for i in range(2, 12 + 1)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_sum = die1 + die2
        
        sum_counts[total_sum] += 1
        
    analytical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    print(f"Результати симуляції Монте-Карло ({num_rolls:,} кидків):")
    print("-" * 75)
    print(f"{'Сума':<6} | {'Кількість':<12} | {'Монте-Карло (%)':<18} | {'Аналітична (%)':<16} | {'Різниця':<10}")
    print("-" * 75)
    
    for s in range(2, 13):
        count = sum_counts[s]
        mc_prob = (count / num_rolls) * 100
        analytical_prob = analytical_probabilities[s]
        
        diff = abs(mc_prob - analytical_prob)
        
        print(f"{s:<6} | {count:<12,} | {mc_prob:<18.2f} | {analytical_prob:<16.2f} | {diff:<10.2f}")
    print("-" * 75)

if __name__ == "__main__":
    dice_rolling_monte_carlo()
