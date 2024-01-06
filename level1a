import json

def min_sublists(arr, target_sum):
    sublists = []
    current_sublist = []
    current_sum = 0

    for value in arr:
        if current_sum + value <= target_sum:
            current_sublist.append(value)
            current_sum += value
        else:
            sublists.append(current_sublist)
            current_sublist = [value]
            current_sum = value

    if current_sublist:
        sublists.append(current_sublist)

    return sublists



import json


def divide_into_subdictionaries(dct, num_subdictionaries, target_sum):
    subdictionaries = {f'subdict{i}': {} for i in range(num_subdictionaries+1)}
    current_sum = {key: 0 for key in subdictionaries}

    for n, value in dct.items():
        selected_subdict = min(subdictionaries, key=lambda key: current_sum[key])
        if current_sum[selected_subdict] + value <= target_sum:
            subdictionaries[selected_subdict][n] = value
            current_sum[selected_subdict] += value
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
print(neighbourhoods)
orders = {}
for i in neighbourhoods:
    for j in neighbourhoods[i]:
        if j=="order_quantity":
            print(neighbourhoods[i][j])
            print(i)
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
level1a={}
output = {}
sum2 = 1
for i in result:
    sum = 1
    temp=[]
    temp.append("r0")
    for j in result[i]:
        
        temp.append(j)
    temp.append("r0")
    output[f"path{sum2}"] = temp
    sum2=sum2+1



level1a["v0"] = output



output_json = json.dumps(level1a, indent=2)
print(output_json)


jsonString = json.dumps(level1a)
jsonFile = open("Z:\Student Handout\level1a\level1a_output.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
