import sys

def moon_weight():
    print('Enter current weight: ')
    weight = int(sys.stdin.readline())
    #weight = int(weight)
    print('Enter average weight increase per year: ')
    weight_increase = float(sys.stdin.readline())
    #weight_increase = float(weight_increase)
    print('Enter moon visit number of years: ')
    num_years = int(sys.stdin.readline())
    #num_years = int(num_years)

    for i in range(1, num_years+1):
        print(('Year #%s: ' + str(weight*0.165)) %(i))
        print(('Current Weight: %s') %(weight))
        weight += weight_increase
