

all: docs/unlockdoc-hlr.md docs/unlockdoc-llr.md

docs/unlockdoc-hlr.md: docs/hlr.md docs/hlr/*
	python src/main.py --input $< --output $@

docs/unlockdoc-llr.md: docs/llr.md docs/llr/* docs/hlr/*
	python src/main.py --input $< --output $@

clean:
	rm docs/unlockdoc-hlr.md docs/unlockdoc-llr.md
