import re

def replace_all(text, dic):
  for i, j in dic.items():
    text = text.replace(i, j)
  return text

def is_valid_hex(hex):
  hex = hex.strip()
  HEX_REGEX = "([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
  return True if re.search(HEX_REGEX, hex) is not None else False

def is_valid_rgb(rgb):
  rgb_vals = get_rgb_vals_from_str(rgb)
  is_valid = True

  if len(rgb_vals) < 3:
    return False

  VALID_RGB_VAL_RANGE = [0, 255]
  for i in range(0, 3):
    if not is_valid_number(rgb_vals[i], *VALID_RGB_VAL_RANGE): 
      is_valid = False

  VALID_ALPHA_VAL_RANGE = [0, 1]
  if len(rgb_vals) == 4:
    if not is_valid_number(rgb_vals[3], *VALID_ALPHA_VAL_RANGE):
      is_valid = False

  return is_valid

def is_valid_number(input_num, min = 0, max = 1):
  num = None
  is_valid = True
  try:
    num = float(input_num)
  except:
    is_valid = False
  if num == None or num < min or num > max:
    is_valid = False
  return is_valid

def get_rgb_vals_from_str(rgb_str):
  to_remove = { "rgb": "", "rgba": "", "(": "", ")": "", ";": "" }
  result = replace_all(rgb_str.strip(), to_remove)
  return result.split(",")