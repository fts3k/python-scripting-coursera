# Question 1: color_translator function recevied the name of a color, then prints the hex value.
## Currently it only supports the three additive primary colors (red, green, blue), so it returns 
# unknown for all other colors.

from turtle import color


def color_translator(color):
    if color == "red":
        hex_color = "#f0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue")) 
print(color_translator("yellow"))  


## Value of python expression
print("big" > "small")


## Question 4:
# Students in a class receive their grade as Pass/Fail. Scores of 60 or more (out of 100) mean the grade is a "Pass"
# Lower scores - grade is a "Fail"
# In addition, scores above 95 (not included) are graded as "Top Score"

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >=60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65))
print(exam_grade(95))
print(exam_grade(100))    

## Question 5: Value of Python Script:

print(11%5)


## Question 6: Function that returns correctly formatted names:
def format_name(first_name, last_name):
    string = ('Nam')
    if first_name != '' and last_name !='':
        string='Name: '+ ' ' + last_name, first_name

    elif first_name != '' and last_name =='' or first_name =='' and last_name !='':
        string = 'Name:'+' '+ first_name + last_name
    else:
        string = last_name, first_name
    return string

format_name("Kevin","Don")
format_name("Chaos") 
format_name("Money", "Machine")                


