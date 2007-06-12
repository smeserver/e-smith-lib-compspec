# Makefile for source rpm: e-smith-lib-compspec
# $Id: Makefile,v 1.1 2007/06/12 19:04:59 slords Exp $
NAME := e-smith-lib-compspec
SPECFILE = $(firstword $(wildcard *.spec))

define find-makefile-common
for d in ../common ../../common ; do if [ -f $$d/Makefile.common ] ; then if [ -f $$d/CVS/Root -a -w $$/Makefile.common ] ; then cd $$d ; cvs -Q update ; fi ; echo "$$d/Makefile.common" ; break ; fi ; done
endef

MAKEFILE_COMMON := $(shell $(find-makefile-common))

ifeq ($(MAKEFILE_COMMON),)
# attept a checkout
define checkout-makefile-common
test -f CVS/Root && { cd .. ; cvs -Q -d $$(cat CVS/Root) checkout common && echo "../common/Makefile.common" ; } || { echo "ERROR: I can't figure out how to checkout the 'common' module." ; exit -1 ; } >&2
endef

MAKEFILE_COMMON := $(shell $(checkout-makefile-common))
endif

include $(MAKEFILE_COMMON)
