import sys
from utils.validate import is_valid_hex
from utils.convert import covert_to_rgb
from utils.clipboard import get_clipboard_value, add_to_clip
from utils.status import success, error

def main():
  hex_val = get_clipboard_value()
  success_info = "from clipboard"

  if len(sys.argv) > 1:
    hex_val = "".join(sys.argv[1:])
    success_info = "from cli argument"

  if not hex_val or not is_valid_hex(hex_val):
    error("missing rgb value to convert")

  rgb_val = covert_to_rgb(hex_val)
  add_to_clip(rgb_val)
  success(rgb_val, success_info, hex_val)

main()
