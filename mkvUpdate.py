import os
import subprocess
import sys

def modify_mkv_resolution(dir, width, height):
  
  for filename in os.listdir(dir):
    if filename.lower().endswith(".mkv"):
      filepath = os.path.join(dir, filename)
      
      try: 
        command_width = [
          "mkvpropedit",
          filepath,
          "--edit", "track:v1",
          "--set", f"display-width={width}"
        ]
        subprocess.run(command_width, check=True)
        
        command_height = [
          "mkvpropedit",
          filepath,
          "--edit", "track:v1",
          "--set", f"display-height={height}"
        ]
        subprocess.run(command_height, check=True)
        
      except subprocess.CalledProcessError as e:
        print(f"  Error modifying resolution: {e}")
      except Exception as e:
        print(f"  An unexpected error occurred: {e}")
        
      
if len(sys.argv) == 4:
  
  directory_path = sys.argv[1]
  height_val = sys.argv[2]
  width_val = sys.argv[3]
  modify_mkv_resolution(directory_path, height_val, width_val)
  
else:
    print("Usage: python3 mkvUpdate.py <directory> <height> <width>")

