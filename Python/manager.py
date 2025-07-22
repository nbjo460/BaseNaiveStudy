import create_model as cm
import execute_prompt as pt

file_name = "buy_computer_data"
primary_classified = "exist"
index = "id"

file_name = "phishing"
primary_classified = "class"
index = "Index"

file_name = "titanic"
primary_classified = "Survived"
index = "Name"

if __name__ == "__main__":
    model = cm.run(file_name,primary_classified,index)

pt.execute(model, primary_classified)
print("finish")