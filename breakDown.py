def extract(fileName) as POD:
  with open(fileName, 'r'):
    POD = POD.readFile()
    fileName.close()


"""
# Python Oriented Data Storage

dates = {
  year:[1934]
  day:[3]
  month:[12]
}
"""
