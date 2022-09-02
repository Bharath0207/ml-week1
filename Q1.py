#1
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25,24]
#sorting
ages.sort()
print('Ages List:',ages)
#To find the minimum in ages
a=min(ages)
print('Minimum in ages:',a)
#To find the maximum in ages
b=max(ages)
print('maximum in ages:',b)
#Add the min age and the max age again to the list
c=[a]+ages[:]+[b]
print('Sum of min age and the max age',c)
#median age (one middle item or two middle items divided by two)
print('median age:',statistics.median(c))
#average age (sum of all items dividend by their number)
Average=sum(c)/len(c)
print('Avg age:',Average)
#range of the ages (max minus min)
Range=c[-1]-c[0]
print('range of the ages:',Range)
