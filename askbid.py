print '''
AskBid version 0.01
Pensando Panama Copyright 2013


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

# Function to choose subfunctions
def main():
    print '''Please choose your function:
    To convert from USD to BTC Press 1
    To convert from BTC to USD Press 2
    To Finish press 3
    '''
    fcts = {1 : usd2btc, 2 : btc2usd, 3 : finish}
    choice = None
    while choice not in fcts.keys() :
        choice = int (raw_input("Enter Choice: "))
        fcts[choice]()
                
# Function to determine asking price when converting from Bitcoin to USD
def btc2usd():
    print "This function lets you know an asking price when converting Bitcoin to USD"
    print "At what price did you purchase the Bitcoins"
    price = float (raw_input("Enter Amount: "))
    print "You entered %s" % price
    print "Please enter the conversion fee you will be charged"
    fee = float (raw_input ("Enter Fee % Amount: "))
    print "You entered %s" % fee
    afee = fee / 100
    usdbuy = (price * afee) + price
    print "Youre new asking price should be %s" % usdbuy
    main()
    
# Function to determine asking price when converting from USD to Bitcoin
def usd2btc() :
    print "This function lets you know an asking price when converting USD to Bitcoin"
    print "At what price did you sell the Bitcoins"
    price = float (raw_input("Enter Amount: "))
    print "You entered %s" % price
    print "Please enter the conversion fee you will be charged"
    fee = float (raw_input ("Enter Fee % Amount: "))
    print "You entered %s" % fee
    afee = fee / 100
    btcbuy = price * (1 - afee)
    print "Youre new asking price should be %s" % btcbuy
    main()

def finish() :
    quit()

main()
