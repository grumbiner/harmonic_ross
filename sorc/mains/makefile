mains = dcheck.deformat dcheck.ross fanalyze gauss.random harmfront hcust hiter irfront ross.data.check sigdri superm t2front testing tmodulate

all : $(mains)

LIBDIR=../../lib

$(mains) : rglib.a
	gfortran $(@).f rglib.a -L$(LIBDIR) -l linpack -l blas -limsl -o $(@)

rglib.a : 
	gfortran -c -O2 -Wall ../util/*.f 
	ar rv rglib.a *.o

clean :
	rm *.o

distclean :
	rm $(mains) rglib.a
	rm *.o
