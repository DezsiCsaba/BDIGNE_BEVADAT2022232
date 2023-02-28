# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
input_list = [1,2,3,4,5]
#input_list = [1,3,5,7,9]

def contains_odd(input_list):
    isOdd = False
    for i in range(len(input_list)):
        if (input_list[i] % 2 == 0):
            isOdd = True
            return isOdd
    return isOdd

contains_odd(input_list)
#print(contains_odd(input_list))

    

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
ints = [1,2,3,4,5]
#ints = [1,3,5,7,9]
#I am not sure if mask means if I have to rewrite the content of the original list
    #that's why the second function is commented out
def is_odd(input_list):
    output = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            output.append(True)
        else:
            output.append(False)
    return output

#def is_odd(input_list):
#    output = []
#    for i in range(len(input_list)):
#        if input_list[i] % 2 == 0:
#            input_list[i] = True
#        else:
#            input_list[i] = False
#    return output

output_list = is_odd(ints)

#for i in range(len(output_list)):
#    print(output_list[i])

# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
input_list_1 = [1,2,3,4]
input_list_2 = [1,1,1]
#input_list_2 = [1,1,1,1]

def element_wise_sum(input_list_1, input_list_2):
    #we assume that either the first list is bigger, or they are even in length
    output=[]
    ct1 = 0
    ct2 = 0
    for i in range(len(input_list_1)):
        output.append(input_list_1[i])
        ct1 += 1
    for i in range(len(input_list_2)):
        output[i] = output[i] + input_list_2[i]
        ct2 += 1
    
    if (ct1 > ct2):
        while ct1 < len(input_list_1):
            output.append(input_list_1[ct1])
            ct1 += 1

    return output

output_list = element_wise_sum(input_list_1, input_list_2)
#for i in range(len(output_list)):
#    print(output_list[i])


# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
input_dict = {
  "conference" : "Western",
  "Division": "Pacific",
  "Founded": 1946,
  "Colors": ["Royal Blue", "yellow"],
  "GM": "Bob Myers",
  "Head Coach": "Steve Kerr"
}
def dict_to_list(input_dict):
    output = []
    for x, y in input_dict.items():
        output.append((x,y))
    return output

output = dict_to_list(input_dict)
#for i in range(len(output)):
#    print(output[i])

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


