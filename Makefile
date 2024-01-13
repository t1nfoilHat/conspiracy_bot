init:
	pdm install
	mkdir groupme_conspiracy_bot/lib
	cd groupme_conspiracy_bot/lib; \
	pip install -t . requests pyyaml

start-telegram:
	pdm run python telegram_bot/main.py --1947 --2012

start-1947:
	pdm run python telegram_bot/main.py --1947

start-2012:
	pdm run python telegram_bot/main.py --2012

deploy-groupme:
	rm -f -- groupme_conspiracy_bot.zip
	cd ./groupme_conspiracy_bot; zip -r ../groupme_conspiracy_bot.zip * -x 'lib/*'; \
	cd lib; zip -gr ../../groupme_conspiracy_bot.zip *
	zip -gr groupme_conspiracy_bot.zip conspiracy_generators
	aws lambda update-function-code --function-name groupme_conspiracy_bot --zip-file fileb://groupme_conspiracy_bot.zip