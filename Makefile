EUPHORIE_POT   = src/dsetool/policy/locales/euphorie.pot
EUPHORIE_PO_FILES = $(wildcard src/dsetool/policy/locales/*/LC_MESSAGES/euphorie.po)
MO_FILES       = $(EUPHORIE_PO_FILES:.po=.mo) $(PLONE_PO_FILES:.po=.mo)

TARGETS        = $(MO_FILES)
SHELL=/bin/bash

all: ${TARGETS}

clean::
	-rm ${TARGETS}

pot:
	i18ndude rebuild-pot --pot $(EUPHORIE_POT) src/dsetool/policy --create euphorie
	$(MAKE) $(MFLAGS) $(EUPHORIE_PO_FILES)

$(EUPHORIE_PO_FILES): src/dsetool/policy/locales/euphorie.pot
	i18ndude sync --pot src/dsetool/policy/locales/euphorie.pot src/dsetool/policy/locales/*/LC_MESSAGES/euphorie.po

.po.mo:
	msgfmt -c --statistics -o $@ $<

.PHONY: all clean pot
.SUFFIXES: .po .mo
