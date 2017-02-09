night=read.csv("/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/night_recall_list2sub1.csv")
morn=read.csv("/Volumes/schnyer/stephanie/sleep_source_memory_project/memory_consolidation_task/morning_recall_list2sub1.csv")

#should not be any rows showing there is no overlab	
merge(night,morn,by=c("word1"))

merge(night,morn,by=c("word2"))