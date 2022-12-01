import json

# the file to be converted
filename = 'Logs.txt'

# resultant dictionary
dict1 = {}
timestamp = ""

# fields in the sample file
fields = ['Timestamp', 'Server', 'Service', 'Message']

with open(filename) as fh:
    # count variable for data id creation
    l = 1

    for line in fh:
        # reading line by line from the text file
        description = list(line.strip().split(None, 5))

        # for output see below
        # print(description)
        # for automatic creation of id for each data
        sno = 'data' + str(l)

        # loop variable
        i = 0
        j=0
        # intermediate dictionary
        dict2 = {}
        while i < len(fields):
            # creating dictionary for each data

            #appending  0,1,2  index value to timestamp
            if j<3:
                timestamp = timestamp +" " + description[j]
                j=j+1
            else:
                dict2[fields[0]] = timestamp
                timestamp = ""
                dict2[fields[1]] = description[3]
                dict2[fields[2]] = description[4]
                dict2[fields[3]] = description[5]
            i = i + 1
        # appending the record of each employee to
        # the main dictionary
        dict1[sno] = dict2
        l = l + 1

    # print(dict1)
# creating json file
out_file = open("test2.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()