
getFilenames <- function(directory,id=1:332) {
    paste(directory,"/",formatC(id,width=3,flag="0"),".csv",sep="")
}

getAllFileData <- function(filenames) {
    lapply(filenames,read.csv,header=TRUE)
}

getNNobs <- function(data) {
    sum(complete.cases(data))
}

