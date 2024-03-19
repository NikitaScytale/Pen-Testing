def get_user_info():
  """Prompts the user for their details and returns them as a dictionary"""
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  nickname = input("Enter your nickname (optional): ")
  email = input("Enter your email address: ")
  return {
      "first_name": first_name,
      "last_name": last_name,
      "nickname": nickname if nickname else "",
      "email": email
  }

def convert_to_numbers(text):
  """Converts a string to various number representations and returns a dictionary"""
  numbers = {
      "text": text,
      "ascii": sum(ord(char) for char in text),
      "binary": sum(int(bin(ord(char))[2:]) for char in text),
  }
  return numbers

def calculate_weight(info):
  """Calculates the weight of the user information in different systems"""
  weight = {}
  for key, value in info.items():
    weight[key] = convert_to_numbers(value)
  return weight

def print_weight(weight):
  """Prints the weight of the user information in a user-friendly format"""
  for key, value in weight.items():
    print(f"{key.capitalize()} weight:")
    for system, value in value.items():
      if system != "text":
        print(f"\tIn {system}: {value}")

if __name__ == "__main__":
  user_info = get_user_info()
  weight = calculate_weight(user_info)
  print_weight(weight)
  print("**Note:** This is a fun script and does not assign any real meaning to the weight calculated.")