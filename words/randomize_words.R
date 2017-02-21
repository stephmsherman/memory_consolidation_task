
participant = "01" ## two digit number in quotes
list = 1 # either 1 or 2

path="/"

one=read.csv(paste("memory_consolidation_task/words/all_words_list",list,".csv",sep=""))

head(one)

#create a sequence from 1 to however many word pairs are in the list (54)
number=seq(1,dim(one)[1])

#randomize numbers
random1=sample(number)
random2=sample(number)
random3=sample(number)

###order the list using the randomized numbers
#for the study phase (random_study)
random_study=one[random1,]

#for the first test phase (random_study_recall)
random_study_recall=one[random2,]

#for the actual recall tests
random_recall=one[random3,]

night_test= random_recall[1:((dim(one)[1])/2),]
morning_test= random_recall[(((dim(one)[1])/2)+1):(dim(one)[1]),]

#write out 
write.csv(random_study,paste("memory_consolidation_task/study_list",list,"sub",participant,".csv",sep=""),row.names=FALSE,quote=FALSE)

write.csv(random_study_recall,paste("memory_consolidation_task/study_recall_list",list,"sub",participant,".csv",sep=""),row.names=FALSE,quote=FALSE)

write.csv(night_test,paste("memory_consolidation_task/night_recall_list",list,"sub",participant,".csv",sep=""),row.names=FALSE,quote=FALSE)


write.csv(morning_test,paste("memory_consolidation_task/morning_recall_list",list,"sub",participant,".csv",sep=""),row.names=FALSE,quote=FALSE)






