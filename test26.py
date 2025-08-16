import statistics

data = [1,2,3,4,5,6,7,8,9,10]
quantiles = statistics.quantiles(data, n=4, method='inclusive')
print(quantiles)