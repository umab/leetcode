

def faltten_json(obj):
    print(obj)

    res = {}
    def flatten(x, key=""):
        if type(x) is list:
            print("inside list")
            i = 0
            for v in x:
                flatten(v, key + str(i) + "_")
                i += 1
        elif type(x) is dict:
            print("inside dict")
            for cur_key in x:
                flatten(x[cur_key], key + cur_key + "_")
        else:
            # this is for basic datatypes 
            # this is where you finally want to end up by decompiling the complex data types above
            # like list / arrays | dict/ json object etc
            print("inside else")
            res[key[:-1]] = x
    
    flatten(obj, "")
    print(res)

def main():
    json = object = {
        "name": {
            "area": [
                {
                    "my name":"my name",
                    "my name1":"my name"
                }
            ]
        }, 
        "address": ["123","345","345"]
    }
    faltten_json(json)

main()