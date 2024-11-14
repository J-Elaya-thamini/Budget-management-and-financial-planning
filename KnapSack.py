# Define the investment options (each with a cost and expected return)
investments = [
    {"name": "Investment A", "cost": 2000, "return": 5000},
    {"name": "Investment B", "cost": 3000, "return": 7000},
    {"name": "Investment C", "cost": 1500, "return": 4000},
    {"name": "Investment D", "cost": 3500, "return": 9000},
    {"name": "Investment E", "cost": 2500, "return": 6000},
]

# Get budget constraint from the user
try:
    budget = int(input("Enter your available budget (between 2000 and 10000): "))
    if budget < 2000 or budget > 10000:
        print("The budget should be between 2000 and 10000. Please enter a valid budget.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid integer for the budget.")
    exit()

# Convert investments to arrays for the knapsack algorithm
costs = [item["cost"] for item in investments]
returns = [item["return"] for item in investments]
n = len(investments)

# Create a table to store the maximum return for each budget limit
# Initialize a 2D array where dp[i][j] represents the maximum return
# achievable with the first i investments and a budget of j
dp = [[0] * (budget + 1) for _ in range(n + 1)]

# Fill the dp table
for i in range(1, n + 1):
    for j in range(budget + 1):
        if costs[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + returns[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

# The maximum return with the given budget is now in dp[n][budget]
max_return = dp[n][budget]
print(f"Maximum Return: {round(max_return, 2)}")

# Find the selected investments
selected_investments = []
w = budget
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_investments.append(investments[i - 1])
        w -= costs[i - 1]

# Display selected investments
print("\nSelected Investments:")
for inv in selected_investments:
    print(f"{inv['name']} (Cost: {inv['cost']}, Return: {inv['return']})")
