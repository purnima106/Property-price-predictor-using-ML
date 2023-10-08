from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

root = Tk()
root.title("Realty Area Price Predictor")
root.geometry("500x600+100+100")
f = ("Cambria", 25 , "bold")
root.configure(bg="lightgreen")


lab_header=Label(root,text ="Realty Area Price Predictor", font=f)
lab_header.pack(pady = 30)

lab_area = Label(root, text ="Enter Area" , font=f)
ent_area = Entry(root, font = f)
lab_area.pack(pady = 10)
ent_area.pack(pady = 5)

lab_bedrooms = Label(root,text = "Enter no. of Bedrooms",font = f)
ent_bedrooms = Entry(root, font=f)
lab_bedrooms.pack(pady = 10)
ent_bedrooms.pack(pady = 5)

def find():
		data = pd.read_csv("C:/Users/Purnima/OneDrive/Desktop/ML3/abpsep23.csv")
		features = data[["area", "bedrooms"]]
		target = data["price"]
		x_train, x_test, y_train,y_test = train_test_split(features, target)
		model = LinearRegression()
		model.fit(x_train, y_train)
	
		try:
			area = float(ent_area.get())
		except ValueError:
			lab_ans.configure(text = "Inaccurate Area")
			ent_area.focus()
			return

		if (area < 1):
			lab_ans.configure(text = "Mininum Area expected :1")
			ent_area.focus()
			return
		try:
			bedrooms = float(ent_bedrooms.get())
		except ValueError:
			lab_ans.configure(text = "Inaccurate Data")
			ent_bedrooms.focus()
			return

		if (bedrooms < 1):
			lab_ans.configure(text = "Mininum Bedrooms expected :1")
			ent_bedrooms.focus()
			return

		price = model.predict([[area, bedrooms]])
		msg = "price = " + str(round(price[0], 2)) + "crs"
		lab_ans.configure(text=msg)

btn_predict = Button(root, text ="Predict Property Price", font = f,command=find,background ="grey",foreground="black")
lab_ans = Label(root, font = f)
btn_predict.pack(pady = 5)
lab_ans.pack(pady = 5)

root.mainloop()


			


