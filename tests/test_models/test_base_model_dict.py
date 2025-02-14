from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(f"Model ID: {my_model.id}")
print(f"Model Representation: {my_model}")
print(f"Model Created At: {
      my_model.created_at} (Type: {type(my_model.created_at)})")
print("--")
my_model_json = my_model.to_dict()
print("Model JSON Representation:")
for key in my_model_json.keys():
    print(
        f"\t{key}: (Type: {type(my_model_json[key])}) - {my_model_json[key]}")

print("--")
my_new_model = BaseModel(**my_model_json)
print(f"New Model ID: {my_new_model.id}")
print(f"New Model Representation: {my_new_model}")
print(f"New Model Created At: {type(my_new_model.created_at)}")

print("--")
print(f"Is original model the same as new model? {my_model is my_new_model}")
# ... existing code ...