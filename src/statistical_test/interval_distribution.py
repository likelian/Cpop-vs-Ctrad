from scipy.stats import chisquare
from scipy.stats import power_divergence
import numpy as np
import json



def load_distribution_to_list(distribution_name, dataset_name):

    path = "../../results/"

    complete_path = path + distribution_name + dataset_name

    with open(complete_path) as json_file:
        dictionary = json.load(json_file)

    category_list = list(dictionary.values())

    category_list = [1 if x==0 else x for x in category_list]

    #print(dictionary)
    #print(category_list)

    print(distribution_name)

    return category_list







distribution_name = "/interval_distribution"

dataset_list = ["/CoCoPops.json", "/han.json", "/POP909.json"]

category_dict = {}

for dataset in dataset_list:
    category_list = load_distribution_to_list(distribution_name, dataset)
    category_dict[dataset] = category_list
    #print(category_list)


    

dataset_1 = "/POP909.json"

dataset_2_list = ["/CoCoPops.json", "/han.json"]


diff_arr_dict = {}

for dataset_2 in dataset_2_list:

    print(" ")
    print(dataset_1)
    print(dataset_2)

    

    dataset_1_arr = np.array(category_dict[dataset_1], dtype = 'float')
    dataset_2_arr = np.array(category_dict[dataset_2], dtype = 'float')


    #print(dataset_1_arr)
    #print(dataset_2_arr)

    #continue
    diff_arr_dict[dataset_2] = dataset_1_arr - dataset_2_arr



    dataset_1_sum = np.sum(dataset_1_arr)
    dataset_2_sum = np.sum(dataset_2_arr)

    if dataset_1_sum > dataset_2_sum:
        dataset_1_arr /= dataset_1_sum
        dataset_1_arr *= dataset_2_sum
    else:
        dataset_2_arr /= dataset_2_sum
        dataset_2_arr *= dataset_1_sum

    #dataset_1_arr /= dataset_1_sum
    #dataset_2_arr /= dataset_2_sum

    #print(np.sum(dataset_1_arr))
    #print(np.sum(dataset_2_arr))


    output = chisquare(dataset_2_arr, f_exp=dataset_1_arr)
    print(output)

    


dataset_1 = "/POP909.json"

dataset_2_list = ["/CoCoPops.json", "/han.json"]

print("")
print("chisquare on the difference of [POP909, CoCoPops] and the difference of [POP909, han]")
output = chisquare(diff_arr_dict[dataset_2_list[0]], f_exp=diff_arr_dict[dataset_2_list[1]])

print(output)



