import json

def create_json_test(file):
  # create the file structure
  with open(file) as f:
    data = json.load(f)

  # Name the test file
  test_name = input("Write a name for the test (only letters and numbers without spaces): ")
  items = input("How many data items to add (e.g., 2, 3, etc.): ")

   # Create new test item data
  for i in range(int(items)):
    item_name = input("Item name: ")
    item_data = input("Item data: ")
    data['system']['query']['form'][item_name] = item_data

  # Write to new file
  with open('./tests/testcase_' + test_name +'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent = 2, sort_keys=True)
  
  # Pretty Printing JSON string data to see if it is alright
  print("------------------------Test case data------------------------")
  print(json.dumps(data, indent = 2, sort_keys=True))


if __name__ == '__main__':
  print("------------------------Create new test------------------------")
  create_json_test('./data.json')