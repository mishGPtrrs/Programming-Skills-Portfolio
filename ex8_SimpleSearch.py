# search

#initialize list of names
names = ["jake", "zac", "ian", "ron", "sam", "dave"]

#define name search
search_name = "sam"

#search for the name in the list
if search_name in names:
    print(f"{search_name} found in the list")
else:
    print(f"{search_name} not found in the list")
