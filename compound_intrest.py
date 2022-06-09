
from matplotlib import pyplot as plt
l=[]
def compound_intrest(principle,rate,num_of_years):
    if num_of_years==0:
        return principle
    else:
        principle=principle+(principle*rate)/100
        l.append(principle)
        return compound_intrest(principle, rate, num_of_years-1)

#Lets check using Examples
p,r,t=1000,10,5
comp=compound_intrest(p,r,t)-p
print('Total Compound intrest for {} years'.format(t) , comp)
years=[i+1 for i in range(len(l))]
print(l)
plt.bar(years,l,width=0.2)
plt.title('Amount to be paid for each Year')
plt.xlabel('Number of Years')
plt.ylabel('Principle Amount for each Year')
