def find_combination(coins, target_sum):
    # Создаем двумерный массив для хранения возможных комбинаций сумм
    dp = [[-1] * (target_sum + 1) for _ in range(len(coins) + 1)]

    # Инициализируем значения для суммы 0 - есть только один способ (не брать ни одной монеты)
    for i in range(len(coins) + 1):
        dp[i][0] = []

    # Заполняем массив dp
    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                without_this_coin = dp[i - 1][j]
                with_this_coin = dp[i][j - coins[i - 1]]
                if with_this_coin != -1:
                    dp[i][j] = with_this_coin + [coins[i - 1]]
                elif without_this_coin != -1:
                    dp[i][j] = without_this_coin

    # Возвращаем результат
    return dp[len(coins)][target_sum]

# Пример использования
coins = [3, 2]
target_sum = 13
result = find_combination(coins, target_sum)

if result != -1:
    print(f"Монеты для получения суммы {target_sum}: {result}")
else:
    print(f"Невозможно получить сумму {target_sum} из заданных монет.")