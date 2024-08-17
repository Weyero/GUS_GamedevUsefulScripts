import bpy
import re

# function for searching original material
def find_original_material(name):
    base_name = re.sub(r'\.\d{3}$', '', name)  # delete suffix .001, .002 etc.
    if base_name in bpy.data.materials:
        return bpy.data.materials[base_name]
    return None

# array for materials that needs to be deleted
materials_to_remove = []
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    if obj.type == 'MESH':  # only mesh
        for slot in obj.material_slots:
            material = slot.material
            if material:
                # if there suffix .001, .002 etc.
                if re.search(r'\.\d{3}$', material.name):
                    original_material = find_original_material(material.name)
                    if original_material:
                        slot.material = original_material  # replace material in slot
                        materials_to_remove.append(material)  # add to remove array

# delete unused materials from blend file
for material in set(materials_to_remove):
    if material.users == 0:  # check if material is not used
        bpy.data.materials.remove(material)

print(" replacement and removing duplicated materials are done.")
