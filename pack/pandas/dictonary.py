sentence = "What is the Airspeed Velocity of an Unladen Swallon ?"
sent_list = sentence.split()
print(sent_list)

result = {word : len(word) for word in sent_list}
print(result)



weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" :22,
    "Sunday" : 24,
}

weather_f = {day:(temp*9/5)+32 for(day, temp) in weather_c.items()}
print(weather_f)


student_dict = {
    "student" : ["Aryan", "Krishna", "Surya"],
    "score" : [75,68,89]
}

# looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd
student_data = pd.DataFrame(student_dict)
# print(student_data)

# loop through a data frame
for(key,value) in student_data.items():
    print(value)
