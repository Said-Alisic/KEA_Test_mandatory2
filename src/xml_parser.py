import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_xml_test():

  # Name the test file
  test_name = input("Write a name for the test (only letters and numbers without spaces): ")
  items = input("How many data items to add (e.g., 2, 3, etc.): ")

  # create the file structure
  root = ET.Element('system')
  query = ET.SubElement(root, 'query')
  form = ET.SubElement(query, 'form')
  items_data = []

  # Create new test item data
  for i in range(int(items)):
    item_name = input("Item name: ")
    item_data = input("Item data: ")
    items_data.append(ET.SubElement(form, 'item')) 
    items_data[i].set('name', item_name)
    items_data[i].text = item_data

  # create a new XML file with the results
  data = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
  file = open("./tests/testcase_" + test_name + ".xml", "w")
  file.write(str(data))

  # Print data to see if it is alright
  print("------------------------Test case data------------------------")
  print(data)
    

if __name__ == '__main__':
  print("------------------------Create new test------------------------")
  create_xml_test()