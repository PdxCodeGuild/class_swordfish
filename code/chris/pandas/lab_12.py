import pandas as pd #captures table in a df
import matplotlib.pyplot as plt #using to visualize final results
import numpy as np #if needed to calculate 

#Why am I doing this? Had a Ops Manager state that long drive times due to 
#distance are leading to increase lateness

#Hypothesis: For the month of August
#Increase in AVG DEL Time (>60min.) due to AVG Distance is leading to < 75% On Time Arrival


#*********Pandas and Numpy*****************
#Open a CSV as a df in Pandas
aug_orders_df = pd.read_csv('/Users/ckeego/code-guild/class_swordfish/code/chris/pandas/Restaurant Efficiency Report (Aug).csv')
# aug_orders_df["COMBINED"] = aug_orders_df["LOCAITON_NAME"].astype(str) + "-" + aug_orders_df["RESTAURANT_NAME"].astype(str)
# print(aug_orders_df)
# t = type(aug_orders_df) #validate df
# print(t)
# print(aug_orders_df.tail()) #understand amount of rows working with
# head = aug_orders_df.head() #see headers
# print('Headers: ', head)

#Basics of DF - Establish Macro
orders_df = aug_orders_df.drop(columns=['AVG_PLACED', 'AVG_ARRIVED', 'AVG_DELIVERED', 'AVG_ENROUTE', 'AVG_PLACED_ARRIVED', 'AVG_ARR_ENROUTE', 'AVG_PREP_TIME']) #eliminate columns with no macro significance
print('Initial Row Count:', len(orders_df.index))
number_orders = orders_df.sort_values(by=['NUMBER_OF_ORDERS'], ascending=False) 
# print(number_orders)

#Stats
mean = round(orders_df['NUMBER_OF_ORDERS'].mean(), 1) #basic python
# print('Orders Average: ', mean)
median = orders_df['NUMBER_OF_ORDERS'].median() #basic python
# print('Orders Median: ', median)
# stdv = (round(np.std(number_orders['NUMBER_OF_ORDERS']), 1))
# print('STDV: ', stdv)
quartile = np.percentile(orders_df['NUMBER_OF_ORDERS'], [25, 50, 75]) #used np
# print('Will drop bottom 25%: ', quartile)

#Top Restaurants 75% for NUMBER_OF_ORDERS
bottom_twenty_five = number_orders.drop(number_orders[number_orders['NUMBER_OF_ORDERS']<5].index, inplace=True) #drop rows with values < 5 
# print('This should return nothing -->', bottom_twenty_five) #should return None
# print('Orders >5', number_orders) #should return Top 75% based on orders ~ 5 Order Minimum to qualify for restaurant

#Sort based on Average Delivery Time and keep Top 10% of highest AVG DEL. Time and overlay with ON Time
new_del_time_count = number_orders.drop(number_orders[number_orders['AVG_DEL_TIME']<60].index, inplace=True) #including restaurants with min. of 5 orders for Aug and > 60min. Del Time
# print('On Time > 80%', number_orders) #from 184 rows to 56 rows

delivery_time = number_orders.sort_values(by=['AVG_DEL_TIME'], ascending=False)
pd.set_option('display.colheader_justify', 'center')
# print('D.T. >60', delivery_time)
locations = number_orders.sort_values(by=['LOCATION_NAME'], ascending=False)
# print(locations)
# print(type(number_orders))

#Combine City and Restaurant
number_orders["COMBINED"] = number_orders["LOCATION_NAME"].astype(str) + " " + "-" + " " + number_orders["RESTAURANT_NAME"].astype(str)
# print(number_orders)
print('Final Row Count:', len(number_orders.index))
# head = number_orders.head() #see headers
# print('Headers: ', head)

#Export to new CSV
number_orders.to_csv('/Users/ckeego/code-guild/class_swordfish/code/chris/pandas/On_Time.csv')

#***********MATPLOTLIB***************
#Visualize data in matplotlib
#Bar Graphs - Avg Distance
#Line - On Time


dataframe = pd.read_csv('/Users/ckeego/code-guild/class_swordfish/code/chris/pandas/On_Time.csv')
print(dataframe)
combined = dataframe['COMBINED']
avg_del_time = dataframe['AVG_DEL_TIME']
avg_dist = dataframe['AVG_DISTANCE']
on_time = dataframe['ON_TIME']
# print(plt.style.available)

# print(type(combined))

# plt.figure(figsize=(25,10)) #width and height
# plt.style.use('fivethirtyeight')
# plt.bar(x=combined, height=avg_del_time, color='purple')
# colors = ['blue' if (bar >= 5(avg_dist) else 'cyan' for bar in avg_dist]
# plt.bar(x=combined, height=on_time, color='purple', label='on_time')
fig, ax1 = plt.subplots()
plt.xticks(rotation=90, fontsize=8)
ax1.bar(combined, avg_dist, color='cyan', label='Left Y Axis: avg_dist (in miles)')
ax2 = ax1.twinx()
ax2.plot(on_time, color='orange', label='Right Y Axis: > Percent on_time', linewidth=1.5)


# plt.bar(x=combined, height=avg_dist, color='cyan', label='avg_dist') #, bottom=avg_del_time
# plt.plot(on_time, color='orange', label='on_time', linewidth=1.5)
plt.axhline([75], color='red', label='on_time Standard', linewidth=2)
# plt.axhline([5], color='green', label='5 miles', linewidth=2)
# plt.xticks(rotation=90, fontsize=8)
# plt.legend()
plt.figlegend()
plt.tight_layout()
plt.show()







#Lessons Learned
#1. A lot of work on research and how to manipulate data - I need to improve on outlining steps and solving smaller pieces
#2. pandas and numpy - more efficient. need to keep learning what i can do  #cheatsheets
#3. I am really bad at decoding ref. guides
#4. Google and YouTube - both inspire me - type in term I don't understand (this has given me confidence to attack).
#5. I could have used functions better, but didn't know I needed it until it was too late. built-in functions are great.
#6. Pay attention to column names and positions