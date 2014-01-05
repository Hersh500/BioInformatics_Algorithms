#WORKS

minNumCoins = {0:0} #Dictionary 

def DPChange(money, coins):
	for m in range(1, money + 1):
		minNumCoins[m] = 100000000
		for i in range(0, len(coins)):
			if m >= coins[i]:
				if minNumCoins[m - coins[i]] + 1 < minNumCoins[m]: 
					minNumCoins[m] = minNumCoins[m - coins[i]] + 1 
	return (minNumCoins[money])

coins = [22,19,12,6,5,3,1] #provided dataset
money = 17434 #provided dataset

print (DPChange(money, coins))

						
	
