# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    output = []
    ct = start_index
    while (ct <= end_index):  #if we go with the assumption that the ending index is still part of the subset it's '<='
        output.append(input_list[ct])       #if we don't wish to include the ending index then it is just '<'
        ct += 1                             #I was unsure which way to go, so I went with the first
    return output             #kinda same with the start index, but it is usually included before eincreasing the indexer

#subset([0,1,2,3,4], 0, 1)

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    output = []
    ct = step_size - 1  #unsure if we want the list[index] or the n-th
    while (ct < len(input_list)):
        output.append(input_list[ct])
        ct += step_size    
    return output

#every_nth([0,1,2,3,4,5,6,7,8,9], 2)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    out = []
    for item in input_list:
        if (item in out):
            return False
        else : out.append(item)
    return True
#unique([1,2,3,4,1])

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    out = []
    for nested in input_list:
        for mini in nested:
            out.append(mini)
    return out
#flatten([[1,2,3],[1,2],[1]])

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_list(*args):
    out = []
    for item in args:
        out += item
    return out

#merge_list([1,2],[[2,3],[4,5]],["a","b"],[{"a":"A", "b":"B"}])

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):  #this won't work with bigger tuples, but i assumed we need tuples with value pairs as in the exmaple
    out = []
    for tuple in input_list:
        newtuple = (tuple[1], tuple[0])
        out.append(newtuple)
    return out

#reverse_tuples([("x", "y"),("a", "b"),("b", "c")])

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list):
    out = []
    for item in input_list:
        if (item not in out):
            out.append(item)
    input_list = out
    return input_list

#remove_tuplicates([1,2,3,4,5,2,3,4])

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
#I want numpy :(
def transpose(input_list):
    out = []

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if len(out) < len(input_list[i]):
                out.append([])
            out[j].append(input_list[i][j])

    return out

#transpose([[0,1],[2,3],[4,5]])

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    flat = []
    out = []
    for nested in input_list:
        for mini in nested:
            flat.append(mini)

    chunk = []
    for i in range(len(flat)):
        chunk.append(flat[i])
        if ((i+1) % chunk_size == 0):
            out.append(chunk)
            chunk = []
    if (len(chunk) != 0):
        out.append(chunk)
    return out

#split_into_chunks([[0,1],[2,3],[4,5]], 5)

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    out={}
    for d in dict:
        for x,y in d.items():
            out[x] = y
    return out

#merge_dicts({
#  "brand": "Ford",
#  "model": "Mustang",
#},{
#  "conference" : "Western",
#  "Division": "Pacific",
#})

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    out={"even": [], "odd":[]}

    for num in input_list:
        if (num % 2 == 0): out["even"].append(num)
        else: out["odd"].append(num)    
    return out

#by_parity([1,2,3,4,5,6,7,7,2])

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    out = {}
    for key in input_dict.keys():
        group = []
        for item in input_dict[key]:
            group.append(item)
        mean = 0
        ct = 0
        for i in range(len(group)):
            mean += group[i]
            ct += 1
        mean = mean / ct
        out[key] = mean
    return out

#mean_key_value({"even": [2, 4, 6, 8], "odd": [1, 3, 5, 7]})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


