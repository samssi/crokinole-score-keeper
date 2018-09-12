clean:
	@find . -name '*.py?' -delete
	@find . -name '.cache' -type d | xargs rm -rf
	@find . -name '__pycache__' -type d | xargs rm -rf
	@rm -rf .venv

.crokinole-score-keeper/bin/activate: requirements.txt
	@test -d .crokinole-score-keeper || python3 -m venv .crokinole-score-keeper
	.crokinole-score-keeper/bin/pip install --upgrade pip
	.crokinole-score-keeper/bin/pip install --no-cache-dir -Ur requirements.txt || exit -1
	touch .crokinole-score-keeper/bin/activate

env: .crokinole-score-keeper/bin/activate

