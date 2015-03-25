#!/usr/bin/env python

import sys,logging
import kosaraju

logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(message)s", 
    level=logging.DEBUG, 
    datefmt='%Y/%m/%d %H:%M:%S'
)

if __name__ == "__main__":
    fn = "example.txt" if len(sys.argv) != 2 else sys.argv[1]
    (vertices,edges) = (None,None)
    while True:
        if not vertices:
            (vertices,edges) = kosaraju.readInput(fn)

        try:
            kosaraju.kosaraju(vertices,edges)
        except:
            logging.exception("it crashed")

        print "Press enter to re-run the script, CTRL-C to exit"
        sys.stdin.readline()
        reload(kosaraju)
