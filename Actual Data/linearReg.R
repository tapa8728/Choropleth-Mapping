filecsv = read.csv(file="C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\stateDict.csv", head=TRUE, sep=",")

print(summary(filecsv))

print("lets calculate linear regression")

print("we only need - gender, age and O ")
myvars = c("age", "gender", "O")
data2 = filecsv[myvars]

print(summary(data2))

results = lm(O ~ age + gender, data=data2)

print(results)