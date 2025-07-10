import create_model as cm
import execute_prompt as pt

file_name = "phishing.csv"
primary_classified = "class"


model = cm.run(file_name,primary_classified)

# print(pt.execute(model, primary_classified, age="youth", income="medium", student="no", credit_rating="fair"))