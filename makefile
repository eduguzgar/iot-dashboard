git-pull:
	git pull origin master

git-push-commit:
	git add .
	git commit -m "$m"
	git push origin master