import create_model as cm
import execute_prompt as pt

file_name = "../csv/buy_computer_data.csv"
primary_classified = "exist"
index = "id"

file_name = "../csv/phishing.csv"
primary_classified = "class"
index = "Index"

file_name = "../csv/titanic.csv"
primary_classified = "Survived"
index = "Name"

if __name__ == "__main__":
    model = cm.run(file_name,primary_classified,index)

pt.execute(model, primary_classified)
print("finish")