.DEFAULT_GOAL := help

MD_SOURCES := $(shell find -mindepth 2 -name '*.md' | sort)

build: dist.pdf ## create a .pdf with all the docs, nicely formatted

serve: dist.md ## run development serve with live reloading
	livedown start dist.md --open
	# TODO: Watch for changes and rebuild dist.md

dist.md: $(MD_SOURCES)
	cat $(MD_SOURCES) > dist.md

dist.pdf: dist.md
	markdown-pdf dist.md

convertlf:
	find -name '*.md' -exec dos2unix {} \;

.PHONY: help build serve convertlf
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
