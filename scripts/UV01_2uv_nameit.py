# UV01_2uv_nameit.py

import bpy

def create_uv_channel(uv_channel_name):
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == 'MESH':
            if uv_channel_name not in obj.data.uv_layers:
                obj.data.uv_layers.new(name=uv_channel_name)
                print(f"UV channel '{uv_channel_name}' added to {obj.name}")
            else:
                print(f"UV channel '{uv_channel_name}' already exists for {obj.name}")
        else:
            print(f"Skipping non-mesh object: {obj.name}")

# get the uv channel name from args
if 'args' in locals():
    uv_channel_name = args[0]  # extract uv channel name
    create_uv_channel(uv_channel_name)
else:
    print("No arguments provided.")
