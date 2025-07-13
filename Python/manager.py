import create_model as cm
import execute_prompt as pt

file_name = "../csv/buy_computer_data.csv"
primary_classified = "exist"
index = "id"

if __name__ == "__main__":
    model = cm.run(file_name,primary_classified,index)

# print(pt.execute(model, primary_classified, age="youth", income="medium", student="no", credit_rating="fair"))