import bpy
from bpy import context

# General Functions
def render(file_path):
    bpy.ops.object.camera_add(enter_editmode=False, align="VIEW", location=(0, -5, 4.00), rotation=(45, 0, 0))
    context.scene.camera = context.object
    bpy.ops.object.light_add(type='POINT', radius=1, align="WORLD", location=(0, 0, 1))
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath=file_path)
    objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'LIGHT')]
    bpy.ops.object.delete({"selected_objects": objs}) 

def clear_all_objects():
    for obj in bpy.context.view_layer.objects:
        obj.select_set(True)
    bpy.ops.object.delete()

def save_blender_file(file_path):
    bpy.ops.wm.save_as_mainfile(filepath=file_path)

# Modeling
def model():
    create_primitive_sphere()
    add_sphere_modifiers()


def add_sphere_modifiers():
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()
    

def create_primitive_sphere():
    bpy.ops.mesh.primitive_uv_sphere_add(location=(0.00,0.00,1.00))

if __name__ == '__main__':
    clear_all_objects()
    model()
    render("model.png")
    # uv_map()
    # texture()
    # rig()
    # animate()
    # light()
    save_blender_file("script.blend")