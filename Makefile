# upgrade pip
.PHONY: upgrade
upgrade:
	@echo "Upgrading pip..."
	@pip install --upgrade pip

# install required packages
.PHONY: install
install:
	@make upgrade
	@echo "Installing required packages..."
	@pip install -r requirements.txt
	@pip install -r requirements-test.txt


# run tests
.PHONY: test
test:
	@python -m pytest -v

# run tests with coverage
.PHONY: test-coverage
test-coverage:
	@python -m pytest --cov=main --cov-report=html
	# show the coverage report in the terminal
	@python -m pytest --cov=main --cov-report=term-missing

# reomve .idea from git cache
.PHONY: clean
clean:
	@echo "Removing .idea from git cache..."
	@git rm -r --cached .idea
	@clear