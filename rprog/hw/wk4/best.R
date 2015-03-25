outcomeOfCareMeasuresFile <- "outcome-of-care-measures.csv"

best <- function(state,outcome) {
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

    # BREAK IT DOWN
    # convert to numeric (has warnings, only works for some reason if 
    # they start as character vectors
    #       as.numeric(relevantData[,2])
    # take the min removing the NAs 
    #       min(...,na.rm=TRUE)
    # vector of TRUE/FALSE for those rows which have the min
    #       relevantData[,2] == ...
    # vector of hospital names (now the first column)
    #       relevantData[...,1]
    # sort it and get the first alpha in case there ar emore than one
    #       sort(...)[1]
    sort(relevantData[relevantData[,2] == min(as.numeric(relevantData[,2]),na.rm=TRUE),1])[1]

}


# test cases and answers:

# print(best("TX", "heart attack"))
# [1] "CYPRESS FAIRBANKS MEDICAL CENTER"
# print(best("TX", "heart failure"))
# [1] "FORT DUNCAN MEDICAL CENTER"
# print(best("MD", "heart attack"))
# [1] "JOHNS HOPKINS HOSPITAL, THE"
# print(best("MD", "pneumonia"))
# [1] "GREATER BALTIMORE MEDICAL CENTER"
# print(best("BB", "heart attack"))
# Error in best("BB", "heart attack") : invalid state
# print(best("NY", "hert attack"))
# Error in best("NY", "hert attack") : invalid outcome

