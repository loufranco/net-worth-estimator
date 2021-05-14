def netWorthByAge(
    ages, 
    savingsRate = 0.18, 
    startingNetWorth = 10000,
    startingSalary = 40000,
    raises = 0.025,
    
    marketReturn = (lambda age: 0.06),
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
      netWorth = netWorth * (1 + marketReturn(age - 1)) + savings

    if age >= retirementAge:
      savings = -startingSalary * pow(1+inflation, age - startingAge) * (1 - savingsRate) * 0.9
    else:
      savings = startingSalary * pow(1+raises, age - startingAge) * savingsRate

    netWorthList.append(netWorth)

  return netWorthList