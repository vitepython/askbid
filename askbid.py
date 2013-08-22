print '''
Asking and Bidding version 0.01
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
    To Quit press any key
    '''
    choice = float (raw_input("Enter Choice: "))
    if choice == 1:
        usd2btc()
    if choice == 2:    
        btc2usd()
        
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
    buy = (price * afee) + price
    print "Youre new asking price should be %s" % buy
    return main();
    
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
    buy = ((price * afee) - price) * -1
    print "Youre new asking price should be %s" % buy
    return main();

main()
