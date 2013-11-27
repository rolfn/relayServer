
# Rolf Niepraschk, 2013/11/27, Rolf.Niepraschk@gmx.de

.SUFFIXES : .tex .dvi .ps .pdf .eps

LATEX = pdflatex


ADDINPUTS = #

BIBS =

all : nodejsServers2.pdf

%.pdf : %.eps
	epstopdf --outfile=$@ $<

%.pdf : %.tex
	pdflatex $<

clean :
	$(RM) $(addprefix $(MAIN), .log .aux .blg)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl)
