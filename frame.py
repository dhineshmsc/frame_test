import json
import pandas as pd
from datetime import datetime

with open('json.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()

given_string = file_content.strip()
# print("file=====================>", given_string)
dictionary = json.loads(given_string)
nonn_frame = []
shelf_movement_frame =[]
misc_frame = []
interaction_frame = []
Staring_frame = []
Moving_frame = []




frame_none = {}
frame_seldmovement = {}
frame_misc = {}
frame_interaction ={}
frame_staring = {}
frame_moving = {}


for item in dictionary['tracking-annotations']:
    if item.get('frame-attributes', {}).get('Categories') == 'none':
        nonn_frame.append(item['frame-no'])
        nonn_frame = list(map(int, nonn_frame))
        ranges = []
        start = nonn_frame[0]
        end = nonn_frame[0]
        for i in range(1, len(nonn_frame)):
            if nonn_frame[i] == end + 1:
                end = nonn_frame[i]
            else:
                ranges.append((start, end))
                start = nonn_frame[i]
                end = nonn_frame[i]
            
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_none = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_none={'NONE':frame_none}

    elif item.get('frame-attributes', {}).get('Categories') == 'Shelf movement':
        shelf_movement_frame.append(item['frame-no'])
        shelf_movement_frame = list(map(int, shelf_movement_frame))
        ranges = []
        start = shelf_movement_frame[0]
        end = shelf_movement_frame[0]
        for i in range(1, len(shelf_movement_frame)):
            if shelf_movement_frame[i] == end + 1:
                end = shelf_movement_frame[i]
            else:
                ranges.append((start, end))
                start = shelf_movement_frame[i]
                end = shelf_movement_frame[i]
            
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_self = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_seldmovement={'SHELF MOVEMENT':frame_self}
    elif item.get('frame-attributes', {}).get('Categories') == 'Misc':
        misc_frame.append(item['frame-no'])
        misc_frame = list(map(int, misc_frame))
        ranges = []
        start = misc_frame[0]
        end = misc_frame[0]
        for i in range(1, len(misc_frame)):
            if misc_frame[i] == end + 1:
                end = misc_frame[i]
            else:
                ranges.append((start, end))
                start = misc_frame[i]
                end = misc_frame[i]
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_misc = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_misc={'MISC':frame_misc}
    elif item.get('frame-attributes', {}).get('Categories') == 'Interaction':
        interaction_frame.append(item['frame-no'])
        interaction_frame = list(map(int, interaction_frame))
        ranges = []
        start = interaction_frame[0]
        end = interaction_frame[0]
        for i in range(1, len(interaction_frame)):
            if interaction_frame[i] == end + 1:
                end = interaction_frame[i]
            else:
                ranges.append((start, end))
                start = interaction_frame[i]
                end = interaction_frame[i]
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_interaction = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_interaction={'INTERACTION':frame_interaction}

    elif item.get('frame-attributes', {}).get('Categories') == 'Staring':
        Staring_frame.append(item['frame-no'])
        Staring_frame = list(map(int, Staring_frame))
        ranges = []
        start = Staring_frame[0]
        end = Staring_frame[0]
        for i in range(1, len(Staring_frame)):
            if Staring_frame[i] == end + 1:
                end = Staring_frame[i]
            else:
                ranges.append((start, end))
                start = Staring_frame[i]
                end = Staring_frame[i]
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_staring = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_staring={'STARTING':frame_staring}

    elif item.get('frame-attributes', {}).get('Categories') == 'Moving':
        Moving_frame.append(item['frame-no'])
        Moving_frame = list(map(int, Moving_frame))
        ranges = []
        start = Moving_frame[0]
        end = Moving_frame[0]
        for i in range(1, len(Moving_frame)):
            if Moving_frame[i] == end + 1:
                end = Moving_frame[i]
            else:
                ranges.append((start, end))
                start = Moving_frame[i]
                end = Moving_frame[i]
        ranges.append((start, end))
        list_of_dicts = [{"start": start, "end": end} for start, end in ranges]
        frame_moving = [d for d in list_of_dicts if not (d["start"] == 0 and d["end"] == 0)]
        frame_moving={'MOVING':frame_moving}

data = [(frame_none),(frame_seldmovement),(frame_misc),(frame_interaction),(frame_moving),(frame_staring)]
print(data)
df_list = []
for category_dict in data:
    for key, value in category_dict.items():
        for entry in value:
            df_list.append({
                'Category': key,
                'Start': entry['start'],
                'End': entry['end']
            })

df = pd.DataFrame(df_list)
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save the dataframe to an Excel file
excel_path = f'data_export_{current_datetime}.xlsx'.replace(":", "-")
df.to_excel(excel_path, index=False)
print('Successfully Exported Data, Path is :',excel_path)
