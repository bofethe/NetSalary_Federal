### This script calulates your net annual salary after USA federal taxes for the 2021 tax year.
### Metrics were taken from https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets on August 27, 2021

# Define calculator function 

def totalSalary(salary = 0):

#Set metrics based on gross annual salary and tax brackets

    rate = 0
    base = 0

    if salary <= 9950:
        rate = .1
        extraTaxed = 0

    elif 9951 <= salary <= 40525:
        rate = .12
        base = 995
        
        if salary - base > 9950:
            extraTaxed = salary - base - 9950
        else:
            extraTaxed = 0

    elif 40526 <= salary <= 86375:
        rate = .22
        base = 4664

        if salary - base > 40525:
            extraTaxed = salary - base - 40525 
        else:
            extraTaxed = 0

    elif 86376 <= salary <= 164925:
        rate = .24
        base = 14751

        if salary - base > 86375:
            extraTaxed = salary - base - 86375
        else:
            extraTaxed = 0

    elif 164926 <= salary <= 209425:
        rate = .32
        base = 33603

        if salary - base > 164925:
            extraTaxed = salary - base - 164925
        else:
            extraTaxed = 0

    elif 209426 <= salary <= 523600:
        rate = .35
        base = 47843

        if salary - base > 209425:
            extraTaxed = salary - base - 209425
        else:
            extraTaxed = 0

    elif salary >= 523601:
        rate = .37
        base = 157804.25

        if salary - base > 523600:
            extraTaxed = salary - base - 523600    
        else:
            extraTaxed = 0

    total = int(salary - base - (extraTaxed * rate))

    print('Annual Salary = ${}\nTax Rate = {}\nBase Subtract = ${}\nExtra Taxed = ${}\nNet Salary = ${}\n'.format(salary, rate, base, extraTaxed, total))

#Enter the pre-taxed salary you want to calculate

totalSalary()