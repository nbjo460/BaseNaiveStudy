import create_model as cm
import execute_prompt as pt
file_name = "buy_computer_data.csv"
primary_classified = "exist"


model = cm.run(file_name,primary_classified)
print(pt.execute(model, "exist", age="youth", income="medium", student="no", credit_rating="fair"))