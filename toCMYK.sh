#!/bin/bash
gs -sOutputFile=converted.pdf -sDEVICE=pdfwrite -dProcessColorModel=/DeviceCMYK -sColorConversionStrategy=CMYK -sColorConversionStrategyForImages=CMYK -dCompatibiltyLevel=1.4 -dNOPAUSE -dBATCH $@
