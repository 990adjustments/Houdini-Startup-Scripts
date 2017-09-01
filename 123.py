#!/usr/bin/env python

# Create Camera - 1080
def create_camera():
  node = hou.node("/obj").createNode("cam", "cam_1080")
  node.setParms({"resx": 1920, "resy": 1080})
  node.setDisplayFlag(False)

# Create Mantra - PBR driver
def mantra_driver():
  node = hou.node("/out")
  out = node.createNode("ifd")
  out.setParms({"vm_renderengine": "pbrraytrace", "override_camerares": True, "camera": "/obj/cam_1080"})

def main():
  create_camera()
  mantra_driver()


if __name__ == '__main__':
  main()