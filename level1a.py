import json

def divide_into_subdictionaries(dct, num_subdictionaries, target_sum):
    subdictionaries = {f'subdict{i}': {'current_sum': 0, 'items': {}} for i in range(num_subdictionaries)}
    remaining_space = {key: target_sum for key in subdictionaries}

    for n, value in sorted(dct.items(), key=lambda x: x[1], reverse=True):
        best_subdict = max(subdictionaries, key=lambda key: remaining_space[key])
        if remaining_space[best_subdict] >= value:
            subdictionaries[best_subdict]['items'][n] = value
            subdictionaries[best_subdict]['current_sum'] += value
            remaining_space[best_subdict] -= value
        else:
            continue

    return subdictionaries


with open("Z:\Student Handout\level1a\level1a.json", 'r') as file:
    data = json.load(file)

    #print(data[i])


n_neighbourhoods = data["n_neighbourhoods"]
n_restaurants = data["n_restaurants"]
neighbourhoods = data["neighbourhoods"]
restaurants = data["restaurants"]
vehicles = data["vehicles"]
#print(neighbourhoods)
orders = {}
for i in neighbourhoods:
    for j in neighbourhoods[i]:
        if j=="order_quantity":
            #print(neighbourhoods[i][j])
            #print(i)
            orders[i] = neighbourhoods[i][j]


print(orders)


# Number of subdictionaries
num_subdictionaries = 3

# Target sum for each subdictionary
target_sum = 600

# Divide into subdictionaries
result = divide_into_subdictionaries(orders, num_subdictionaries, target_sum)

# Output the result
#print("Subdictionaries with sum equal to 600: ", result)

print(result)
level1a={}
output = {}
sum2 = 1
output = {}

for i, subdict in enumerate(result.values(), start=1):
    path = ["r0"] + list(subdict.get('items', {}).keys()) + ["r0"]
    print(path)
    output[f"path{i}"] = path

level1a["v0"] = output




output_json = json.dumps(level1a, indent=2)

print(output_json)

jsonString = json.dumps(level1a)
jsonFile = open("Z:\Student Handout\level1a\level1a_output.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


