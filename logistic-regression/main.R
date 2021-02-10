library(pROC)
library(bestglm)
library(ggplot2)
library(MASS)
library(lmtest)
library(car)
library(tidyverse)

# Read in the data
PB <- read.csv("~/Stat 123/Stat 330/Stat 330/PineBeetle2 (1).csv", header = TRUE)
View(PB)

#Explore Data

PB$Infested <- as.numeric(PB$Infested)-1

scatter.smooth(PB$January,PB$Infested, xlab = "January Temp", ylab = "Infestation Probability")
scatter.smooth(PB$Precip,PB$Infested, xlab = "Precipitation", ylab = "Infestation Probability")
scatter.smooth(PB$August_max,PB$Infested, xlab = "August Temperature", ylab = "Infestation Probability")
scatter.smooth(PB$Slope,PB$Infested, xlab = "Slope", ylab = "Infestation Probability")
scatter.smooth(PB$Elev,PB$Infested, xlab = "Elevation", ylab = "Infestation Probability")


#Best Model

vs.res <- bestglm(PB,IC = "AIC", method = "exhaustive", family = binomial)
vs.res
vs.res$BestModels

PBLM <- glm(data = PB, family = binomial, Infested ~ January + August_max + Slope + Elev + Precip + NC + SE + SW)
PBLM
summary(PBLM)

#Effect of each coefficient

confint(PBLM)

#Threshold

thresh <- seq(0,1,length=100)
misclass <- rep(NA,length=length(thresh))
pred.probs <- predict.glm(PBLM,type="response")
for(i in 1:length(thresh)) {
  #If probability greater than threshold then 1 else 0
  my.classification <- ifelse(pred.probs>thresh[i],1,0)
  # calculate the pct where my classification not eq truth
  misclass[i] <- mean(my.classification!=PB$Infested)
}
#Find threshold which minimizes miclassification
thresh[which.min(misclass)]
T <- thresh[which.min(misclass)]
plot(thresh, misclass, pch=20, type = "l", xlab = "Cutoff", ylab = "Misclassification")
abline(v=T, col = "green")

#Matrix

pred.class <- ifelse(pred.probs>T, 1,0)
table <- table(PB$Infested,pred.class)
addmargins(table)

deviance <- PBLM$deviance
nullDeviance <- PBLM$null.deviance
1-(deviance/nullDeviance)

# Cross-validation

n.cv <- 500
n.test <- round(.1*nrow(PB))
cutoff <- T
sens <- rep(NA,n.cv)
spec <- rep(NA,n.cv)
ppv <- rep(NA,n.cv)
npv <- rep(NA,n.cv)
auc <- rep(NA,n.cv)
for(cv in 1:n.cv){
  test.obs <- sample(1:nrow(PB),n.test)
  test.set <- PB[test.obs,]
  train.set <- PB[-test.obs,]
  train.model <- glm(Infested~January+August_max+Slope+Elev+Precip+NC+SE+SW,data=train.set,family=binomial)
  pred.probs <- predict.glm(train.model,newdata=test.set,
                            type="response") 
  test.class <- ifelse(pred.probs>cutoff,1,0)
  conf.mat <- addmargins(table(test.set$Infested,test.class))
  sens[cv] <- conf.mat[2,2]/conf.mat[2,3]
  spec[cv] <- conf.mat[1,1]/conf.mat[1,3]
  ppv[cv] <- conf.mat[2,2]/conf.mat[3,2]
  npv[cv] <- conf.mat[1,1]/conf.mat[3,1]
  auc[cv] <- auc(roc(test.set$Infested,pred.probs))
} 

mean(sens)
mean(spec)
mean(ppv)
mean(npv)
mean(auc)

summary(PBLM)

#Projected
PB2018 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January = -13.98, August_max = 15.89, Precip = 771.13)
#0.8390319
PB2019 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January = -17.80,August_max = 18.07, Precip = 788.54)
#0.8951125
PB2020 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-17.27,August_max =16.74, Precip = 677.63)
#0.8628658
PB2021 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-12.52,August_max =18.06, Precip = 522.77)
#0.6178305
PB2022 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-15.99,August_max =18.23, Precip = 732.32)
#0.8407897
PB2023 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-11.97,August_max =15.81, Precip = 615.96)
#0.703202
PB2024 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-15.75,August_max =16.85, Precip = 805.90)
#0.8769379 
PB2025 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-16.19,August_max =16.51, Precip = 714.57)
#0.8571702
PB2026 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-17.87,August_max =17.84, Precip = 740.50)
#0.8840701
PB2027 <- data.frame(SE = "Yes", NC = "No", SW = "No", Slope = 18.07, Elev = 1901.95, January =-12.44,August_max =16.96, Precip = 801.22)
#0.8014825 



pred.log.odds <- predict.glm(PBLM,newdata=PB2027)
pred.prob <- exp(pred.log.odds)/(1+exp(pred.log.odds))
pred.prob <- predict.glm(PBLM,newdata=PB2027,type="response")
pred.prob

pred.probs <- predict.glm(PBLM,type="response")
a.roc <- roc(PB$Infested,pred.probs)
auc(a.roc)

plot(a.roc,legacy.axes=TRUE)