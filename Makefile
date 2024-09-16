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
	ruff check *.py mylib/*.py --fix

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy


generate_report:
	python -c "from script import load_dataset, calculate_statistics, generate_md_report, generate_visualizations; \
	data = load_dataset('rdu-weather-history.csv'); \
	stats = calculate_statistics(data); \
	image_paths = generate_visualizations('rdu-weather-history.csv'); \
	generate_md_report(stats, image_paths, 'summary_report.md')"
	
	# Git commands to add, commit, and push the report and all PNG files
	@if [ -n "$$(git status --porcelain)" ]; then \
	    git config --local user.email "action@github.com"; \
	    git config --local user.name "GitHub Action"; \
	    git add summary_report.md $$(echo $$(ls *.png)); \
	    git commit -m 'Add generated markdown report and histogram images'; \
	    git push; \
	else \
	    echo "No changes to commit."; \
	fi
