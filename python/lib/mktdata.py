import os
import sys
import csv

# The market data in this file came from
#   http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
#
# The columns are
#  Year / S&P 500 / 3 month T Bill / US T Bond / Corporate bonds
def readMktData():  
  tsv_file = open("data/mkt-data.tsv")
  mkt_data = list(csv.reader(tsv_file, delimiter="\t"))
  tsv_file.close()

  return mkt_data

# This gets the market return for a specific age
# given a historical start year and then blends it in 
# a portfolio that is 70% stocks and 30% a mixed set of bonds
def mktReturn(mktData, age, startingYear):
  mktForYear = mktData[startingYear - 1928 + age - 25]
  portfolioReturn = float(mktForYear[1]) * 0.70 + \
    float(mktForYear[2]) * 0.15 + \
    float(mktForYear[3]) * 0.12 + \
    float(mktForYear[4]) * 0.03

  return portfolioReturn