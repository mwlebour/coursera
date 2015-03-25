outcomeOfCareMeasuresFile <- "outcome-of-care-measures.csv"

rankhospital <- function(state,outcome,num="best") {

    data <- read.csv(outcomeOfCareMeasuresFile,colClasses = "character")
    states <- sort(unique(data[,"State"]))

    if(! state %in% states) stop("invalid state")
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
    relevantData <- data[data$State==state,c(2,col)]
    relevantData[,2] <- as.numeric(relevantData[,2])
    relevantData <- relevantData[complete.cases(relevantData),]
    relevantData <- relevantData[ order(relevantData[,2],relevantData[,1]), ]

    if(num == "best") {
        relevantData[1,1]
    } else if(num == "worst") {
        relevantData[nrow(relevantData),1]
    } else {
        relevantData[num,1]
    }

}

# > source("rankhospital.R")
# > rankhospital("TX", "heart failure", 4)
# [1] "DETAR HOSPITAL NAVARRO"
# > rankhospital("MD", "heart attack", "worst")
# [1] "HARFORD MEMORIAL HOSPITAL"
# > rankhospital("MN", "heart attack", 5000)
# [1] NA
