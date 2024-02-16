name = input('put in your name')
birthday = input('put in your birthday in the form of yyyymmdd. eg. 1999/ Nov. 15th =19991115')
print(name.title(), 'was born on', birthday[6:], '/', birthday[-4:-2], '/', birthday[0:4])