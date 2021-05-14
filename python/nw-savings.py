import matplotlib
import matplotlib.pyplot as plt

import sys

import lib.mktdata as mktdata
import lib.networth as networth


def plotSavingsRateScenarios(
    plotFile = 'net-worth-savings.png', 
    savingsRate1 = 0.18, 
    savingsRate2 = 0.12):

  ages = range(25, 86)
  scenarioA = networth.netWorthByAge(ages = ages, savingsRate = savingsRate1)
  scenarioB = networth.netWorthByAge(ages = ages, savingsRate = savingsRate2)

  plt.clf()
  fig, ax = plt.subplots(figsize=(8,8))

  ax.ticklabel_format(style='plain', useOffset=False)
  ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

  plt.plot(ages, scenarioA, ages, scenarioB)
  plt.title("Net Worth Estimation (Savings Rate: " + \
    str(savingsRate1*100) + "%" + " vs. " + str(savingsRate2*100) + "%)")
  plt.savefig(plotFile)


def main():
  if len(sys.argv) != 4:
      print("Usage: python "+sys.argv[0]+" <chart output file> <savings rate 1> <savings rate 2>")
      print("Example: python "+sys.argv[0]+" savings.png 0.18 0.12")
      exit(1)

  plotSavingsRateScenarios(
    plotFile = sys.argv[1], 
    savingsRate1 = float(sys.argv[2]), 
    savingsRate2 = float(sys.argv[3]))

main()