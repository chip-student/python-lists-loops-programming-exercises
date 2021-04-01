all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
    return color["sexy"] == True

def generate_li(items):
    return '<li>' + items["label"] + '</li>'

list_filtra = list(filter(filter_colors, all_colors))        

result = list(map(generate_li, list_filtra))

htmlString=""
for i in range(len(result)):
    htmlString += result[i]

print(htmlString)
