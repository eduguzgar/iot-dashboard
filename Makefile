git-pull:
	git pull origin master

git-push-commit:
	git add .
	git commit -m "$m"
	git push origin master

git-reset:
	git reset
	git checkout .
	git clean -fdx
