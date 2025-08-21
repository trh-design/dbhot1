li = ["alec", "Aric", "Alex", "Tony", "rain"]
result_list = [s for s in li if s.lower().startswith('a') and s.endswith('c')]
print(result_list)
tu = ("alec", "Aric", "Tony", "rain")
result_tuple = tuple(s for s in tu if s.lower().startswith('a') and s.endswith('c'))
print(result_tuple)