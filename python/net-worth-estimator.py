import matplotlib
import matplotlib.pyplot as plt

def netWorthByAge(
    ages, 
    savingsRate = 0.15, 
    startingNetWorth = 10000,
    startingSalary = 40000,
    raises = 0.025,
    
    marketReturn = 0.06,
    inflation = 0.02,
    
    retirementAge = 65
  ):

  netWorthList = []
  savings = 0
  netWorth = 0
  startingAge = ages[0]
  
  for age in ages:

    if age == startingAge:
      netWorth = startingNetWorth
    else:
      netWorth = netWorth * (1 + marketReturn) + savings

    if age >= retirementAge:
      savings = -startingSalary * pow(1+inflation, age - startingAge) * (1 - savingsRate) * 0.9
    else:
      savings = startingSalary * pow(1+raises, age - startingAge) * savingsRate

    netWorthList.append(netWorth)

  return netWorthList

ages = range(25, 86)
scenarioA = netWorthByAge(ages = ages, savingsRate = 0.18)
scenarioB = netWorthByAge(ages = ages, savingsRate = 0.12)

plt.plot(ages, scenarioA, ages, scenarioB)
plt.savefig('net-worth.png')
