filecsv = read.csv(file="C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\stateDict.csv", head=TRUE, sep=",")

print(summary(filecsv))

print("lets calculate linear regression")

# print("we only need - gender, age and O ")
# myvars = c("age", "gender", "O")
# data2 = filecsv[myvars]
# print(summary(data2))

print("LINEAR REGRESSION FOR O")
results_o = lm(O ~ age + gender, data=filecsv)
print(results_o)
print(coef(results_o))

print("LINEAR REGRESSION FOR C")
results_c = lm(C ~ age + gender, data=filecsv)
print(results_c)
print(coef(results_c))

print("LINEAR REGRESSION FOR E")
results_e = lm(E ~ age + gender, data=filecsv)
print(results_e)
print(coef(results_e))

print("LINEAR REGRESSION FOR A")
results_a = lm(A ~ age + gender, data=filecsv)
print(results_a)
print(coef(results_a))

print("LINEAR REGRESSION FOR N")
results_n = lm(N ~ age + gender, data=filecsv)
print(results_n)
print(coef(results_n))