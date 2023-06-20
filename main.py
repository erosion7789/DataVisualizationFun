#EDA:exploratory data analysis
import matplotlib.pyplot as plt
import pandas as pd

def line_chart_example(x_ser,y_ser):
    plt.plot(x_ser,y_ser, label="Population")
    plt.plot(x_ser,y_ser*2, label="Population x2",c="blue",ls="--")
    plt.legend()
    plt.ylabel("Population (in millions)")
    plt.xlabel("City Class")
    plt.title("Chinese Population Analysis")
    plt.show()

def scatter_chart_example(x_ser,y_ser):
    plt.scatter(x_ser,y_ser,s=300,marker="x")
    plt.figure()
    plt.show()

def bar_chart_example(x_ser,y_ser):
    plt.figure()
    plt.bar(x_ser,y_ser)
    plt.show()

def pie_chart_example(values_ser,labels_ser):
    plt.figure()
    plt.pie(values_ser,labels_ser,autopac="%1.1f%%")
    plt.show()
    
    
    

df = pd.read_csv("merged.csv")
print(df)

grouped_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)

line_chart_example(class_pop_ser.index,#L,M,S
                   class_pop_ser)#47.9,7.9,2.6

#great for numeric data poins that can be
#2. scatter chat
scatter_chart_example(class_pop_ser.index,
                      class_pop_ser)

#3. bar chat
bar_chart_example(class_pop_ser,
                  class_pop_ser.index)

#4. pie chat
pie_chart_example(class_pop_ser.index,
                  class_pop_ser)
