#filecsv = read.csv(file="C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\stateDict.csv", head=TRUE, sep=",")
filecsv = read.csv(file="/home/tanvip/Desktop/Choropleth-Mapping/Actual Data/stateDict.csv", head=TRUE, sep=",")
#print(summary(filecsv))

print("lets calculate linear regression")

print("LINEAR REGRESSION FOR O")
results_o = lm(O ~ age + gender, data=filecsv)
rs_o<-residuals(results_o)
z_o <- scale(rs_o, center = TRUE, scale = TRUE)
print("z-score for N is done")

print("LINEAR REGRESSION FOR C")
results_c = lm(C ~ age + gender, data=filecsv)
rs_c<-residuals(results_c)
z_c <- scale(rs_c, center = TRUE, scale = TRUE)
print("z-score for C is done")

print("LINEAR REGRESSION FOR E")
results_e = lm(E ~ age + gender, data=filecsv)
rs_e<-residuals(results_e)
z_e <- scale(rs_e, center = TRUE, scale = TRUE)
print("z-score for E is done")

print("LINEAR REGRESSION FOR A")
results_a = lm(A ~ age + gender, data=filecsv)
rs_a<-residuals(results_a)
z_a <- scale(rs_a, center = TRUE, scale = TRUE)
print("z-score for A is done")

print("LINEAR REGRESSION FOR N")
results_n = lm(N ~ age + gender, data=filecsv)
	rs_n<-residuals(results_n)
z_n <- scale(rs_n, center = TRUE, scale = TRUE)
print("z-score for N is done")


#append these values to new csv file
x <- data.frame(filecsv, z_o, z_c, z_e, z_a, z_n )

#windows
#write.table(x, file = "C:\\Users\\Tanvi Parikh\\Desktop\\Choropleth-Mapping\\Actual Data\\residual.csv", row.names=FALSE,col.names=TRUE,sep=",")
#ubuntu
write.table(x, file="/home/tanvip/Desktop/Choropleth-Mapping/Actual Data/zscore.csv", row.names=FALSE, col.names=TRUE, sep=",")
print("Z-scored values added to zscore.csv")