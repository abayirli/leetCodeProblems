# LeedCode June Challange Day 3
# Two City Scheduling Problem

# Definition:
# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

def twoCitySchedCost(costs):
	n = int(len(costs)/2)
	cost_diff = sorted(costs, key = lambda k: abs(k[0] - k[1]), reverse = True)

	sum_cost = 0
	n0, n1 = (0,0)
	k = 0
	while(k < 2*n):
		t0 = cost_diff[k][0]
		t1 = cost_diff[k][1]

		if((t0 <= t1 and n0 < n) or n1 == n):
			sum_cost += t0
			n0 += 1
		else:
			sum_cost += t1
			n1 += 1
		k += 1
	return sum_cost

def test():
	assert twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859
	assert twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
	assert twoCitySchedCost([[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]) == 3671
	print("All test passed!")

test()