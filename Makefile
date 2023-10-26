lint:
	pre-commit run --all-files

test:
	pytest -x -s -v --durations=0 --cache-clear

git-commit-ignore-hooks:
	git commit --no-verify

git-push-ignore-hooks:
	git push --no-verify

pre-commit-install-hooks:
	pre-commit uninstall
	pre-commit install --install-hooks
	pre-commit install --hook-type pre-push

pre-commit-uninstall-hooks:
	pre-commit uninstall

pre-commit-update-repos:
	pre-commit autoupdate
