import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("/Users/alberthu/Desktop/Final Project 2.1/CO2_Emissions_1960-2018.csv")

data = data.dropna()


def build_prediction():
	historical_data = data.loc[:,"2009":"2018"]
	label_data = data["2019"]

	rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
	rf.fit(training_data.values, label_data.values)

	for row in predict_data.values:
    	print(rf.predict([row]))

	# get model, rehydrate model

	# historical_data = "insert 4 years of data"

	# predictions = []

	# for i in range(0,5):
	# 	this_prediction = my_model.predict(historical_data[i:] + predictions)
	# 	predictions.append(this_prediction)

	# return predictions
	# 	# prediction list provides the y values to graph 
	# 	# x values are 2018 - 2023 

	# y_values = predictions

	# x_values = [2018 + i for i in range(0,5)]

