reciever_list = [2 , 1 , 5 , 3 , 4]
dict1 = {
    (reciever_list.index(reciever_list[0])+1):reciever_list[0],
    (reciever_list.index(reciever_list[1])+1):reciever_list[1],
    (reciever_list.index(reciever_list[2])+1):reciever_list[2],
    (reciever_list.index(reciever_list[3])+1):reciever_list[3],
    (reciever_list.index(reciever_list[4])+1):reciever_list[4]
    }
key_list = list(dict1.keys())
val_list = list(dict1.values())
donor_list=[0,0,0,0,0]
for i in range(5):
    position = val_list.index(reciever_list[i])
    donor_list[val_list[position]-1] = key_list[position]

print(donor_list)
