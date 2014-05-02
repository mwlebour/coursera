#!/usr/bin/env Rscript

source("helpers.R")
source("complete.R")

getCor <- function(datum) {
    cor(datum["sulfate"],datum["nitrate"],use="complete.obs")
}

corr <- function(directory, threshold = 0) {
    completeCases = complete(directory)
    aboveThreshold <- completeCases[completeCases$nobs > threshold,"id"]
    if ( length(aboveThreshold) == 0 ) {
        vector(mode="numeric")
    } else {
    data <- getAllFileData(getFilenames(directory,rapply(aboveThreshold,c)))
    x <- lapply(data,getCor)
    rapply(x,c)
    }
}

# cr <- corr("specdata", 150)
# head(cr)
# summary(cr)
# cr <- corr("specdata", 400)
# head(cr)
# summary(cr)
# cr <- corr("specdata", 5000)
# summary(cr)
# length(cr)
# cr <- corr("specdata")
# summary(cr)
# length(cr)
