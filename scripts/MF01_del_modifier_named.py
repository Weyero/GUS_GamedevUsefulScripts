import bpy

def delete_modifier(modifier_name):
    # Iterate over all selected objects
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            # Iterate through all modifiers of the object
            for modifier in list(obj.modifiers):
                # If the modifier matches the name, remove it
                if modifier.name == modifier_name:
                    obj.modifiers.remove(modifier)
                    print(f"Modifier '{modifier_name}' removed from {obj.name}")
        else:
            print(f"Skipping non-mesh object: {obj.name}")

# Get the modifier name from the passed arguments
if 'args' in locals():
    modifier_name = args[0]  # Extract the name from the passed arguments
    delete_modifier(modifier_name)
else:
    print("No arguments provided.")
