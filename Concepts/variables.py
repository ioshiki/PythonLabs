#variables

name = "Joseph"
car = "Toyota Matrix"
color = "black"
driver = 1
capacity = 4
engine = 2.4
total_capacity = driver + capacity

print name," drives a ",color,car 
print "it has a ", engine, " Engine"  
#we can use %d as a formatter to do so instead of the way above
print "the total capacity of the car is %d people" % total_capacity #%d returns digits
print "Hence we can also display the first line as follows"
print "%s drives a %s %s" %(name, car, color)  #%s returns the string value 




