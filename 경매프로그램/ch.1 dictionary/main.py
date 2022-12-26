programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
    ,
    }

# # value를 호출하고 싶으면 key의 철자를 정확이 입력해야한다.
# print(programming_dictionary["Bug"])

# # 따옴표를 빼고 문자열을 아니게 입력하면 에러가 난다.

# # Adding new items to dictionary. (Loop)
# programming_dictionary["Loop"] = "The action of doing something over and over agian."
# print(programming_dictionary)

# # create empty list
# empty_list = []

# # create empty dictionary
# empty_dictionary = {}

# # 이렇게 하면 나중 단계에서 빈 딕셔너리에 key와 value를 추가할 수 있다.

# # 딕셔너리를 통째로 지우고 싶을 때 빈 딕셔너리로 만들면 된다.
# programming_dictionary = {}

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A month in your computer."

# print(programming_dictionary["Bug"])

# dictionary와 for loop
# for thing in programming_dictionary:
#    print(thing)

# key만 출력하게 된다. key와 value 둘 다 출력되지 않는다. 여기서 thing은 key에 해당하므로 key만 출력한다.
# value를 출력하고 싶다면

# for thing in programming_dictionary:
#    print(programming_dictionary[thing])