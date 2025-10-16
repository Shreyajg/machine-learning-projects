#implementing Linear Regression from scratch:
import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#equation y'=mx+c
m,c=0.0,0.0 #initializing parameters
a=0.01 #learning rate
epochs=1000 #number of iterations
n=len(x)
#the gradient descent algorithm to find the most efficient values of m and c for which the cost function is minimized
for ephoc in range(epochs):
    dm=0.0
    dc=0.0
    for i,j in zip(x,y):
        dm+=(j-(m*i+c))*i
        dc+=(j-(m*i+c))
    dm=(-2/n)*dm
    dc=(-2/n)*dc
    m-=a*dm
    c-=a*dc
#found values of m and c
m=1.9951803506719779
c=0.017400463340610635
print(m)
print(c)
print("Predicted y values:")
for i in x:
    print(m*i+c)

#Plotting the graph of expected vs predicted values that is fit to a line mx+c
plt.figure(figsize=(2,6))
plt.scatter(x,y,color='blue',alpha=0.5)
plt.plot(x,[m*i+c for i in x],color='red',label='Fitted line')
plt.xlabel("x dataset")
plt.ylabel("target variable")
plt.show()