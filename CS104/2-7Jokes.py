import json

jsonstring = """
[{"type":"programming","setup":"Why do programmers always get Christmas and Halloween mixed up?","punchline":"Because DEC 25 = OCT 31","id":389}
,{"type":"general","setup":"Where do sheep go to get their hair cut?","punchline":"The baa-baa shop.","id":292}
,{"type":"general","setup":"What does a pirate pay for his corn?","punchline":"A buccaneer!","id":239}
,{"type":"programming","setup":"How many programmers does it take to change a lightbulb?","punchline":"None that's a hardware problem","id":25}
,{"type":"general","setup":"Did you hear about the Mexican train killer?","punchline":"He had loco motives","id":92}
,{"type":"general","setup":"Why are fish easy to weigh?","punchline":"Because they have their own scales.","id":303}
,{"type":"general","setup":"What do you give a sick lemon?","punchline":"Lemonaid.","id":236}
,{"type":"general","setup":"What did Michael Jackson name his denim store?","punchline":"   Billy Jeans!","id":161}
,{"type":"general","setup":"Why are ghosts bad liars?","punchline":"Because you can see right through them!","id":305}
,{"type":"general","setup":"When does a joke become a dad joke?","punchline":"When it becomes apparent.","id":286}]
"""

data = json.loads(jsonstring)

combined_strings = []

for entry in data:
    combined_string = (
        f"{entry['setup']} - {entry['type']}\n Punch: {entry['punchline']}"
    )
    combined_strings.append(combined_string)
print("\n".join(combined_strings))
# print(data[2]['type'])
