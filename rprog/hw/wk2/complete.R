#!/usr/bin/env Rscript

source("helpers.R")

complete <- function(directory, id=1:332) {
    filenames <- getFilenames(directory,id)
    x <- data.frame(cbind(
        id,
        lapply(getAllFileData(filenames),getNNobs)
    ))
    names(x) <- c("id","nobs")
    x
}

# complete("specdata",1)
# complete("specdata", c(2, 4, 8, 10, 12))
# complete("specdata", 30:25)
# complete("specdata", 3)
