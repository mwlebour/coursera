#!/usr/bin/env Rscript

source("helpers.R")

pollutantmean <- function(directory, pollutant, id = 1:332) {
    filenames <- getFilenames(directory,id)
    allFileData <- do.call("rbind",getAllFileData(filenames))
    pollutantData = allFileData[[pollutant]]
    mean(pollutantData[!is.na(pollutantData)])
}

# pollutantmean("specdata","sulfate",1:10)
# pollutantmean("specdata","nitrate",70:72)
# pollutantmean("specdata","nitrate",23)
