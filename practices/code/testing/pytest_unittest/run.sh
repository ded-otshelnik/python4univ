# для запуска тестов с покрытием кода под pytest
# установите плагин pytest-cov
# pip install pytest-cov
pytest --cov=sample --cov-report=term-missing --cov-branch test.py