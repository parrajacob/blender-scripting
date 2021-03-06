import bpy
from bpy import context

def generate_render(file_path):
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

def create_primitive_monkey():
    bpy.ops.mesh.primitive_monkey_add(location=(0.00,0.00,1.00))

def save_blender_file(file_path):
    bpy.ops.wm.save_as_mainfile(filepath=file_path)

if __name__ == '__main__':
    clear_all_objects()
    create_primitive_monkey()
    generate_render("model.png")
    save_blender_file("script.blend")