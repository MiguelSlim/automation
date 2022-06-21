def error(message, *additional_info):
  print("\033[91m" + message + "\033[0m")
  print(*additional_info)
  exit()

def success(message, *additional_info):
  print("\033[92m" + message + "\033[0m")
  print(*additional_info)
  exit()