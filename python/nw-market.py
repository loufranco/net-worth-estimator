import matplotlib
import matplotlib.pyplot as plt

import sys

import lib.mktdata as mktdata
import lib.networth as networth


def plotSavingsRateMktScenarios(
    plotFile = 'net-worth-market.png', 
    endingAge = 85,
    savingsRate = 0.18,
    fromYear = 1928, toYear = 1960
  ):

  ages = range(25, endingAge + 1)
  mktData = mktdata.readMktData()

  plt.clf()

  fig, ax = plt.subplots(figsize=(8,8))

  ax.ticklabel_format(style='plain', useOffset=False)
  ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

  for startingYear in range(fromYear, toYear, 5):
    scenario = networth.netWorthByAge(ages = ages,
      savingsRate = savingsRate, 
      marketReturn = (lambda age: mktdata.mktReturn(mktData, age, startingYear = startingYear))
    )
    ax.plot(ages, scenario)
  
  plt.title("Historical Market Return (Savings Rate: " + str(savingsRate*100) + "%)")
  plt.savefig(plotFile)

def usage(extraMsg = ""):
    print("Usage: python "+sys.argv[0] + " <chart output file> <ending age> <savings rate>")
    print("Example: python "+sys.argv[0] + " market.png 65 0.18")
    if extraMsg != "":
      print(extraMsg)

def main():
  if len(sys.argv) != 4:
    usage()
    exit(1)

  endingAge = int(sys.argv[2])
  if endingAge < 30 or endingAge > 85:
    usage(extraMsg = "ending age must be between 30 and 85")
    exit(1)

  plotSavingsRateMktScenarios(
    plotFile = sys.argv[1], 
    endingAge = endingAge, 
    savingsRate = float(sys.argv[3]))

main()
