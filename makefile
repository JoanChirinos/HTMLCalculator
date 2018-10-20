run:
	-rm -f *.html
	python3 makeHTML.py
	@echo "Number of html files: "
	@find . -name "*.html" | wc -l

clean:
	-rm -f *.html
	@echo "If you get an argument list too long error, use \"make force_clean\"."
	@echo "This will delete every HTML file in current directory, so be wary"

force_clean:
	find . -maxdepth 1 -name "*.html" -print0 | xargs -0 rm -f
