# Rolf Niepraschk, 2011-05-18, Rolf.Niepraschk@ptb.de

CFLAGS = -g
CXX = g++

all : vxi11_transceiver

vxi11_transceiver : vxi11_transceiver.o vxi11_user.o vxi11_clnt.o vxi11_xdr.o unescape.o
	$(CXX) $(CFLAGS) -o $@ $^

vxi11_transceiver.o: vxi11_transceiver.cc vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

vxi11_user.o: vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

unescape.o: unescape.cpp unescape.h
	$(CXX) $(CFLAGS) -c $< -o $@

vxi11.h vxi11_clnt.c vxi11_xdr.c : vxi11.x
	rpcgen -M $<

clean :
	$(RM) vxi11_transceiver unescape.o vxi11_clnt.o vxi11_transceiver.o \
    vxi11_user.o vxi11_xdr.o vxi11.h vxi11_clnt.c vxi11_xdr.c
