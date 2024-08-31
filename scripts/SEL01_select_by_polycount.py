#SEL01_select_by_polycount.py

import bpy

def select_high_poly_meshes(threshold):
    # Ensure we are in object mode
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Iterate through all objects in the scene
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            # Calculate the number of polygons (faces)
            polygon_count = len(obj.data.polygons)
            
            # Select the object if it exceeds the threshold
            if polygon_count > threshold:
                obj.select_set(True)

# Получаем аргумент threshold
if 'args' in locals():
    threshold = args[0]
    select_high_poly_meshes(threshold)
else:
    print("No threshold provided.")
