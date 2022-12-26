capital = {
    "France": "Paris",
    "Korean": "Seoul",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary

treveler_log = {
    "France": ["Paris","Lille","Dijon"],
    "Korean": ["Seoul","Daegu","Busan"],
}

not_problem = ["A","B",["C","D",["E","F"]]]

# Nesting Dictionary in a Dictionary (딕셔너리 중첩)


treveler_log = {
    "France": {"cities_visted": ["Paris","Lille","Dijon"]},
    "Korean": {"cites_visted": ["Seoul","Daegu","Busan"],
                "total_visted": 3},
}

# Nesting Dictionary in a List
treveler_log = [
    {
      "country": "France",
      "cities_visted": ["Paris","Lille","Dijon"],
      "total_visted": 12
    },
    {
      "country": "Korean",
      "cites_visted": ["Seoul","Daegu","Busan"],
      "total_visted": 5
    }, 
]

# 중요 포인트: 키와 값 사이에는 ":" 가 존재해야한다.
# dict1 = {Key:value}
