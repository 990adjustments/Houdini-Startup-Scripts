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
  # Check for camera node
  nodes = hou.node('/obj').glob('*')
  cam_exists = False

  for node in nodes:
    if node.type().name() == 'cam':
      cam_exists = True
      break
  
  if not cam_exists:
    create_camera()
  
  # Check for mantra node
  rops = hou.node('/out').glob('*')
  rop_exists = False

  for node in rops:
    if node.type().name() == 'ifd':
      rop_exists = True
      break

  if not rop_exists:
    mantra_driver()


if __name__ == '__main__':
  main()