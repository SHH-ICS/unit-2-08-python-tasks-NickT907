def reverseName(myName):
  result = ''
  for i in range(len(myName)):
    result += myName[len(myName)-i-1]
  return result

testName = input("what's your name?")
print(reverseName(testName))
  
def rootAge(myAge):
  
  result = myAge
  return result
