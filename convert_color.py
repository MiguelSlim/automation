import sys
from utils.validate import is_valid_rgb, is_valid_hex
from utils.convert import covert_to_rgb, covert_to_hex
from utils.clipboard import get_clipboard_value, add_to_clip
from utils.status import success, error

def main():
  initial_val = get_clipboard_value()
  success_info = "from clipboard"

  if len(sys.argv) > 1:
    initial_val = "".join(sys.argv[1:])
    success_info = "from cli argument"

  is_rgb = is_valid_rgb(initial_val)
  is_hex = is_valid_hex(initial_val)

  if not initial_val or (not is_rgb and not is_hex):
    error("missing proper value to convert")

  result_val = covert_to_hex(initial_val) if is_rgb else covert_to_rgb(initial_val)
  add_to_clip(result_val)
  success(result_val, success_info, initial_val)

main()