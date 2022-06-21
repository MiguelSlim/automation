import os
import subprocess

def get_clipboard_value():
  return str(subprocess.check_output(["pbpaste"]), "UTF-8")

def add_to_clip(text):
  command = 'echo "' + text.strip() + '"| pbcopy'
  os.system(command)