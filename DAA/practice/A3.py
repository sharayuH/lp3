def knapsack_dynamic_programming(w, weights, price, n):
    k = [[0 for x in range(w+1)] for x in range(n+1)]
    items = []
    for i in range(n+1):
        for w in range(w+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif weights[i-1] <= w:
                k[i][w] = max(price[i-1] + k[i-1][w-weights[i-1]], k[i-1][w])
                items.append(i)
            else:
                k[i][w] = k[i-1][w]
    w = W
    res = k[n][w]
    for i in range(n, 0, -1):
        if res <= 0:
            break
        elif res == k[i-1][w]:
            continue
        else:
            print("Weight: ", weights[i-1], " - ", "Price: ", price[i-1])
            res -= price[i-1]
            w -= weights[i-1]

    return k[n][W]


ch = "1"
while(ch != "0"):
    print("1. Knapsack problem ")
    ch = input("0. Exit")
    if(ch == "0"):
        break
    elif ch == "1":
        price = []
        weights = []
        n = int(input("Enter number of items: "))
        for i in range(0, n):
            x = int(input("Enter price: "))
            y = int(input("Enter weight: "))
            price.append(x)
            weights.append(y)
        W = int(input("Enter the weight of the knapsack: "))
        print("The optimum price is : ",
              knapsack_dynamic_programming(W, weights, price, n))
    else:
        print("Invalid input")
