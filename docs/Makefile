
# Rolf Niepraschk, 2015/02/23, Rolf.Niepraschk@gmx.de

.SUFFIXES : .tex .dvi .ps .pdf .eps

LATEX = pdflatex


ADDINPUTS = #

BIBS =

all : relayServer.pdf

%.pdf : %.eps
	epstopdf --outfile=$@ $<

%.pdf : %.tex
	pdflatex $<

clean :
	$(RM) $(addprefix $(MAIN), .log .aux .blg)

veryclean : clean
	$(RM) $(addprefix $(MAIN), .pdf .bbl)
