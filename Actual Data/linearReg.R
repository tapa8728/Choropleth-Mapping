#filecsv = read.csv(file="C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\stateDict.csv", head=TRUE, sep=",")
filecsv = read.csv(file="/home/tanvip/Desktop/Choropleth-Mapping/Actual Data/stateDict.csv", head=TRUE, sep=",")
#print(summary(filecsv))

print("lets calculate linear regression")

print("LINEAR REGRESSION FOR O")
results_o = lm(O ~ age + gender, data=filecsv)
#print(results_o)
rs_o<-residuals(results_o)
#print(rs_o)

print("LINEAR REGRESSION FOR C")
results_c = lm(C ~ age + gender, data=filecsv)
#print(results_c)
rs_c<-residuals(results_c)
#print(rs_c))

print("LINEAR REGRESSION FOR E")
results_e = lm(E ~ age + gender, data=filecsv)
#print(results_e)
rs_e<-residuals(results_e)
#print(rs_e)

print("LINEAR REGRESSION FOR A")
results_a = lm(A ~ age + gender, data=filecsv)
#print(results_a)
rs_a<-residuals(results_a)
#print(rs_a)

print("LINEAR REGRESSION FOR N")
results_n = lm(N ~ age + gender, data=filecsv)
#print(results_n)
rs_n<-residuals(results_n)
#print(rs_n)

#append these values to new csv file

x <- data.frame(filecsv, rs_o, rs_c, rs_e, rs_a, rs_n)


#windows
#write.table(x, file = "C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\residual.csv", row.names=FALSE,col.names=TRUE,sep=",")
#ubuntu
write.table(x, file="/home/tanvip/Desktop/Choropleth-Mapping/Actual Data/residual.csv", row.names=FALSE, col.names=TRUE, sep=",")
print("Residual values added to residual.csv")