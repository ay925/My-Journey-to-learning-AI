chai_types={"Masala": "Spicy",
            "Ginger":"Zesty",
           "Green":"Mild",
           }
# print(chai_types["Masala"]) #same as print(chai_types.get("Ginger")) but if key is diffrent so not through an error
# print(chai_types)
# chai_types["Ginger"]="Freah"
# print(chai_types)
# for chai in chai_types:
#     print(chai, chai_types[chai])
#same as
# for key,value in chai_types.items():
#     print(key,value)
# if "Masala" in chai_types:
#     print("I have in chai types")
# chai_types["Earl Gray"]="Citrus"
# print(chai_types)
# chai_types.pop("Ginger")
# print(chai_types)
# del chai_types["Green"]
# print(chai_types)
# tea_shop={
#     "Chai":{"Masala":"Spicy","Ginger":"Zensty"},
#     "Tea":{"Green":"Mild","Black":"Strong"}
# }
# print(tea_shop["Chai"])
# print(tea_shop["Chai"]["Ginger"])
squared_num={x:x**2 for x in range(1,6)}
print(squared_num)
keys=["Masala","Ginger","Lemon"]
print(keys)
default_value="Delicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)
