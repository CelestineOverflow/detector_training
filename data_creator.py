import bpy
import mathutils
import random
import subprocess
import os
import json
import math
import os
empty_images_results = r'D:\training\data\dataset\empty'
full_images_results = r'D:\training\data\dataset\full'
if not os.path.exists(empty_images_results):
    os.makedirs(empty_images_results)
if not os.path.exists(full_images_results):
    os.makedirs(full_images_results)

#get the object named "Chip"

chip = bpy.data.objects['Chip']

#get the object named "Light"

light = bpy.data.objects['Light']

#get the camera object

camera = bpy.data.objects['Camera']

#get original camera location

original_camera_location = camera.location.copy()

#get original camera rotation

original_camera_rotation = camera.rotation_euler.copy()


def create_rand_image():
    #move the camera to a random location + - 1 meter from the original location in x and y
    camera.location.x = original_camera_location.x + random.uniform(-1, 1)
    camera.location.y = original_camera_location.y + random.uniform(-1, 1)
    #rotate the camera to a random rotation + - 10 degrees from the original rotation in x and y
    camera.rotation_euler.x = original_camera_rotation.x + math.radians(random.uniform(-5, 5))
    camera.rotation_euler.y = original_camera_rotation.y + math.radians(random.uniform(-5, 5))
    #change the light color to a random color

    light.data.color = (random.random(), random.random(), random.random())

    #change the chip color to intensity to a random value between 100w and 1000w

    light.data.energy = random.randint(100, 1000)

    #make the chip appear and disappear from viewport view and render view

    show_hide = random.choice([True, False])
    chip.hide_render = show_hide
    chip.hide_viewport = show_hide
    # render the image and save it to the corresponding folder
    filename = 'image_{}.png'.format(random.randint(0, 1000000))
    path = None
    if show_hide:
        path = empty_images_results
    else:
        path = full_images_results
    bpy.context.scene.render.filepath = os.path.join(path, filename)
    bpy.ops.render.render(write_still=True)
        
    
for _ in range(1000):
    create_rand_image()
    
#reset the camera location and rotation to the original values
camera.location = original_camera_location
camera.rotation_euler = original_camera_rotation