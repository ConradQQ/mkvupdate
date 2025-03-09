import os
import subprocess
import sys

def modify_mkv_resolution(dir, width, height):
  
  # Select and Loop over MKVs in a directory
  
  for filename in os.listdir(dir):
    if filename.lower().endswith(".mkv"):
      filepath = os.path.join(dir, filename)
      
      # Edit the display width value on the MKV
      
      try: 
        command_width = [
          "mkvpropedit",
          filepath,
          "--edit", "track:v1",
          "--set", f"display-width={width}"
        ]
        subprocess.run(command_width, check=True)
        
        # Edit the display height value on the MKV
        
        command_height = [
          "mkvpropedit",
          filepath,
          "--edit", "track:v1",
          "--set", f"display-height={height}"
        ]
        subprocess.run(command_height, check=True)
        
        # Error checking
        
      except subprocess.CalledProcessError as e:
        print(f"  Error modifying resolution: {e}")
      except Exception as e:
        print(f"  An unexpected error occurred: {e}")
        
# Uses sys module to add function arguments to variables, then calls modify_mkv_resoultion
if len(sys.argv) == 4:
  
  directory_path = sys.argv[1]
  height_val = sys.argv[2]
  width_val = sys.argv[3]
  modify_mkv_resolution(directory_path, height_val, width_val)
  
# Error checking for bad CLI usage
else:
    print("Usage: python3 mkvUpdate.py <directory> <height> <width>")

