
# SCENE
getFilePath()

# PREFERENCES
setPreferencesValues()

bpy.context.scene.render.fps = 45    # Set FPS


# OUTLINER
cShortcut - Hide Layer - Ctrl+H
cShortcut - UnHide Layer - Ctrl+H


# MODEL
count vertices, faces of object
count no of objects present in the scene


# RENDERING
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'



bpy.ops.preferences.addon_enable(module='add_curve_extra_objects')      # Add Curve : Extra Objects
bpy.ops.preferences.addon_enable(module='add_mesh_extra_objects')       # Add Mesh : Extra Objects
bpy.ops.preferences.addon_enable(module='ant_landscape')
bpy.ops.preferences.addon_enable(module='space_view3d_modifier_tools')  # Interface : Modifier Tools

Check mesh tools in default Blender addons

Object : Fluent : Power Trip - https://www.blendermarket.com/products/fluent
3D View : BoxCutter - https://blendermarket.com/products/hard-ops--boxcutter-ultimate-bundle
