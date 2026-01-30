# Flask Api integration here 
# Entry point to model from UI
import pickle

fx = open("model.pkl", "rb")
model = pickle.load(fx)

# text = ["i am feeling very excited today"]
# prediction = model.predict(text)

# print(prediction)

while True:
    user_input = input("Enter you text:")
    prediction = model.predict([user_input])
    print("Emotion:",prediction)
