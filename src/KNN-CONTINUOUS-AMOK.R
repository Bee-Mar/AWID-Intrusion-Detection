normalize <- function(x) { return ((x - min(x)) / (max(x) - min(x)))  }

wifiLog <- read.delim("C:/CIS660/project/dataset-headers-reduced-removed-null.csv",sep=",")
View(wifiLog)

wifiLog2<-wifiLog[,c(which( colnames(wifiLog)=="wlan.fc.type" ),which( colnames(wifiLog)=="frame.time_delta_displayed" ) , which( colnames(wifiLog)=="wlan.duration" ),which( colnames(wifiLog)=="class" ))]
View(wifiLog2)

wifiLog2$wlan.fc.type=normalize(as.numeric(wifiLog2$wlan.fc.type))
wifiLog2$frame.time_delta_displayed=normalize(as.numeric(wifiLog2$frame.time_delta_displayed))
wifiLog2$wlan.duration=normalize(as.numeric(wifiLog2$wlan.duration))
View(wifiLog2)


ATTACKTYPE<-"amok"

# Keep only the target class and the normal packets
wifiLog2<-wifiLog2[wifiLog2$class=="normal" | wifiLog2$class==ATTACKTYPE, ]

wifiLog2$class<-as.character(wifiLog2$class)
wifiLog2$class[wifiLog2$class=="normal"]<-as.character("0")
wifiLog2$class[wifiLog2$class==ATTACKTYPE]<-as.character("1")
wifiLog2$class<-as.factor(wifiLog2$class)

# drop the unused factor levels
wifiLog2$class<-droplevels(wifiLog2$class)
unique(wifiLog2$class)

# The sampling will be 75% training, 25% test
smp_size <- floor(0.66 * nrow(wifiLog2))
#smp_size <- 10

## set the seed to make partition reproducable
set.seed(32)
# Perform the sampling
train_ind <- sample(seq_len(nrow(wifiLog2)), size = smp_size)

# Create the training set
train <- wifiLog2[train_ind, ]

# Create the test set
test <- wifiLog2[-train_ind, ]

View(train)
View(test)

library(DMwR)
f<-formula("class~wlan.fc.type+frame.time_delta_displayed+wlan.duration")
train_smote<-SMOTE(f,train,perc.over=150,perc.under=90,k=3)
View(train_smote)
library(mlr)

#task<-makeClassifTask(data = test, target = "class")
#test_oversamp_task<-oversample(task,rate=25)
#test_oversamp<-test_oversamp_task$env$data
test_oversamp<-test

m<-kNN(f,train_smote,test_oversamp,norm=FALSE,k=5)

# Determine if a sample is a false positive
FindFP <-function(predicted,predictor)
{
  c <- 0
  #cat("IN FindFP: predictor:",predictor," predicted: ", predicted)
  for (x in 1:length(predicted))
  {
    if(predictor[x]==0&&predicted[x]==1)
      c<- c+1
  }
  return (c)
}

# Determine if a sample is a false negative
FindFN <-function(predicted,predictor)
{
  c <- 0
  #cat("IN FindFP: predictor:",predictor," predicted: ", predicted)
  for (x in 1:length(predicted))
  {
    if(predictor[x]==1&&predicted[x]==0)
      c<- c+1
  }
  return (c)
}

# Determine if a sample is a true postive
FindTP <-function(predicted,predictor)
{
  c <- 0
  #cat("IN FindFP: predictor:",predictor," predicted: ", predicted)
  for (x in 1:length(predicted))
  {
    if(predictor[x]==1&&predicted[x]==1)
      c<- c+1
  }
  return (c)
}


# determine if a sample is true negative
FindTN <-function(predicted,predictor)
{
  c <- 0
  #cat("IN FindFP: predictor:",predictor," predicted: ", predicted)
  for (x in 1:length(predicted))
  {
    if(predictor[x]==0&&predicted[x]==0)
      c<- c+1
  }
  return (c)
}



#cat("TABLE OF DISTRIBUTION OF TEST DATA FOR ATTACK TYPE ",ATTACKTYPE,":")
#w<-table(test_oversamp$class)
#t=as.data.frame(w)
#names(t)[1]="Class"
#show(t)

FP<-FindFP(m,test_oversamp$class)
TP<-FindTP(m,test_oversamp$class)
TN<-FindTN(m,test_oversamp$class)
FN<-FindFN(m,test_oversamp$class)
accuracy<-(TP+TN)/(FP+TP+TN+FN)
errorRate<-(FP+FN)/(FP+TP+TN+FN)
sensitivity<-TP/(TP+FP)
specificity<-TN/(TN+FN)
precision<-TP/(FP+TP)
recall<-TP/(TP+FN)

cat("FP:", FP," TP:", TP, "TN: ", TN, "FN: ", FN,"\n")

cat("Confusion Matrix:\n")
n<-sprintf("n=%d",TP+TN+FP+FN)

l<-sprintf("%20s%20s%20s\n",n,"Predicted: NO","Predicted: YES")
cat(l)
l<-sprintf("%20s%20d%20d%20d\n","Actual: NO", TN,FP,TN+FP)
cat(l)
l<-sprintf("%20s%20d%20d%20d\n","Actual: YES", FN,TP,FN+TP)
cat(l)
l<-sprintf("%20s%20d%20d\n","",TN+FN,FP+TP)
cat(l)
cat("Accuracy: ",accuracy,"\n")
cat("Error Rate: ",errorRate ,"\n")
cat("Sensitivity: ", sensitivity,"\n")
cat("specificity: ", specificity,"\n")
cat("precision: ",precision,"\n")
cat("recall: ", recall,"\n")



