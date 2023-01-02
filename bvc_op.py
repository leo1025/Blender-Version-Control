import bpy
from bpy.types import Operator

class BVC_OT_Create_New(Operator):
    bl_idname = "object.create_new_project"
    bl_label = "New Project"
    bl_description = "Create a new Version Controlled project directory structure."

    def execute(self, context):
        pass