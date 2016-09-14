file_numbers = open("no_of_elements_in_each_cluster_Dmel.txt")
#outfile = open("coordinates.txt".'w')
list_of_numbers = file_numbers.readlines()
final_list = []
for i in range(len(list_of_numbers)):
    tmp = list_of_numbers[i]
    tmp = list_of_numbers[i].replace('\n','')
    tmp = int(tmp)
    final_list.append(tmp)


with open("coordinates.txt",'a') as outfile:
    #coordinates = []
    temp = 0
    for index in range(len(final_list)):
        temp = temp+final_list[index]
        #coordinates.append(str(temp)+'\n')
        outfile.write(str(temp)+'\n')


#print(coordinates)
