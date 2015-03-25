outcomeOfCareMeasuresFile <- "outcome-of-care-measures.csv"

rankall <- function(outcome,num="best") {

    data <- read.csv(outcomeOfCareMeasuresFile,colClasses = "character")
    if(! outcome %in% c("heart attack", "heart failure", "pneumonia") ) stop("invalid outcome")

    # c("heart attack", "heart failure", "pneumonia")
    # c(11,17,23)

    # forgive me
    col <- 0
    if( outcome == "heart attack"  )   col <- 11
    if( outcome == "heart failure" )   col <- 17
    if( outcome == "pneumonia"     )   col <- 23
    if( col == 0 ) stop("we should never ever get here")

    # save the name and the proper column just so i 
    # don't have to type as much (on the next line, yeah yeah)
    relevantData <- data[,c(2,7,col)]
    relevantData[,3] <- as.numeric(relevantData[,3])
    relevantData <- relevantData[complete.cases(relevantData),]

    if(num == "best") {
        x <- lapply(split(relevantData,relevantData[,2]),function(a) { a[order(a[,3],a[,1]),1][1] })
    } else if(num == "worst") {
        x <- lapply(split(relevantData,relevantData[,2]),function(a) { a[order(a[,3],a[,1]),1][nrow(a)] })
    } else {
        x <- lapply(split(relevantData,relevantData[,2]),function(a) { a[order(a[,3],a[,1]),1][num] })
    }

    y <- data.frame(matrix(unlist(x),length(names(x))),row.names=names(x))
    y[,2] <- names(x)
    colnames(y) <- c("hospital","state")
    y



}

