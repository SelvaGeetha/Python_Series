#store the key value pair , enclosed with curly bracket

dictionary={
    "1":"one",
    "2":"two",
    "3":"three"

}
print(dictionary.get("1"))

#set default message

print(dictionary.get("9","invalid key"))