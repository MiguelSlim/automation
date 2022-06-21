import sys
from utils.validate import is_valid_rgb
from utils.convert import covert_to_hex
from utils.clipboard import get_clipboard_value, add_to_clip
from utils.status import success, error

def main():
  rgb_val = get_clipboard_value()
  success_info = "from clipboard"

  if len(sys.argv) > 1:
    rgb_val = "".join(sys.argv[1:])
    success_info = "from cli argument"

  if not rgb_val or not is_valid_rgb(rgb_val):
    error("missing rgb value to convert")

  hex_val = covert_to_hex(rgb_val)
  add_to_clip(hex_val)
  success(hex_val, success_info, rgb_val)

main()
