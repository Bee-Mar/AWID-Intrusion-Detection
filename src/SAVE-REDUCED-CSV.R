rm(list=ls())
sessionInfo()
memory.size()
memory.limit(size=80000)
memory.limit()

wifiLog <- read.delim("C:/CIS660/project/dataset-headers-tst.csv",sep=",")
#View(wifiLog)
# Select only the columns listed on the webpage
wifiLog2<-wifiLog[,c(46, 66, 6, 65, 92, 93, 63, 121, 117, 111, 75, 89, 3, 107, 69, 76, 72, 106,which( colnames(wifiLog)=="class" ))]
write.csv(wifiLog2,"C:/CIS660/project/dataset-headers-reduced-tst.csv",row.names=FALSE)