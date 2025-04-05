

all: docs/unlockdoc.md

docs/unlockdoc.md: docs/.spec docs/unlockdoc/*
	python src/main.py --input $< --output $@

clean:
	rm docs/unlockdoc.md
