install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py
	python -m pytest --nbval *.ipynb

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy


generate_report:
	python -c "from main import load_data, calculate_statistics, create_histogram, generate_md_report; \
	data = load_data('rdu-weather-history.csv'); \
	stats = calculate_statistics(data); \
	create_histogram(data, 'Temperature Maximum', 'temperature_maximum_distribution.png'); \
	generate_md_report(stats, ['temperature_maximum_distribution.png'], 'summary_report.md')"
	
   # Git commands to add, commit, and push the report and PNG files
	@if [ -n "$$(git status --porcelain)" ]; then \
	    git config --local user.email "action@github.com"; \
	    git config --local user.name "GitHub Action"; \
	    git add summary_report.md temperature_maximum_distribution.png; \
	    git commit -m 'Add generated markdown report and histogram image'; \
	    git push; \
	else \
	    echo "No changes to commit."; \
	fi