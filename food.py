spots = [{"name": "Taco Bell", "cuisine": "Mexican"}, 
          {"name": "Panda Express", "cuisine": "Chinese"}, 
          {"name": "Olive Garden", "cuisine": "Italian"} 
          ]
print(spots[0]["name"], spots[0]["cuisine"])
print(spots[1]["name"], spots[1]["cuisine"])
print(spots[2]["name"], spots[2]["cuisine"])

if spots[0]["cuisine"] != spots[1]["cuisine"] and spots[0]["cuisine"] != spots[2]["cuisine"] and spots[1]["cuisine"] != spots[2]["cuisine"]:
    print("All three restaurants have different cuisines.")