import re
from .validate import get_rgb_vals_from_str

def covert_to_rgb(hex):
  HEX_REGEX = "([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
  hex_vals = re.match(HEX_REGEX, hex.strip().replace("#", ""))[0]
  result = []
  type = "rgb"

  if len(hex_vals) == 3:
    for num in hex_vals:
      hex_num = int(num + num, 16)
      result.append(str(hex_num))
  elif len(hex_vals) >= 6:
    for i in range(0, 3):
      hex_num = int(hex_vals[i * 2] + hex_vals[(i * 2) + 1], 16)
      result.append(str(hex_num))

  if len(hex_vals) == 8:
    alpha = round(int(hex_vals[-2] + hex_vals[-1], 16) / 255, 3)
    result.append(str(alpha))
    type = "rgba"

  return type + "(" + ", ".join(result) + ")"


def covert_to_hex(rgb):
  rgb_vals = get_rgb_vals_from_str(rgb)
  result = ""

  for i in range(0, 3):
    result += format_int_to_hex(rgb_vals[i])

  if len(rgb_vals) == 4:
    alpha_val = float(rgb_vals[3]) * 255
    result += format_int_to_hex(alpha_val)

  return "#" + result

def format_int_to_hex(num):
  hex_val = "{:x}".format(int(num))
  return hex_val if len(hex_val) == 2 else "0" + (hex_val)