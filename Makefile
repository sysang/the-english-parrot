help:
	@echo "Read Makefile"

neoterm:
	@/usr/bin/python3 modules/teaching_assistant/teaching_assistant/main.py
# @/usr/bin/python3 tryit.py

action:
	/usr/local/bin/rasa run actions --actions actions

actiond:
	setsid ./actions/runactionserver.sh >./actions/logs/$(shell date "+%Y%m%d-%H%M").log 2>&1 < /dev/null &
	@ps -ef | awk '/[a]ctions\/runactionserver\.sh/'

stopactiond:
	ps -ef | awk '/[a]ctions\/runactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -9
	@ps -ef | awk '/[a]ctions\/runactionserver\.sh/'

restartactiond: stopactiond actiond

training:
	/usr/local/bin/rasa train -vv --augmentation 0

train:
	rasa train -v --augmentation 0

shell:
	/usr/local/bin/rasa shell -vv --log-file=logs/$(model)_run_$(shell date "+%Y%m%d-%H%M").log -m $(model)

chat:
	/usr/local/bin/rasa shell -v --log-file=logs/$(model)_run_$(shell date "+%Y%m%d-%H%M").log -m $(model)

visualize:
	bin/rasa visualize -vv --out story-graphs/$(shell date "+%Y%m%d-%H%M").html

run:
	/usr/local/bin/rasa run -vv --log-file=logs/$(model)_run_$(shell date "+%Y%m%d-%H%M").log -m $(model)

run_silent:
	bin/rasa run -v --log-file=logs/$(model)_run_$(shell date "+%Y%m%d-%H%M").log -m $(model)

pyrun:
	poetry run python $(file)

formatter:
	black actions

lint:
	flake8 actions
	black --check actions

types:
	pytype --keep-going actions

e2etest_main__a_kiss:
	python e2etest/test.py --model $(model) --scriptfile e2etest/data/scenario__a_kiss.yml

e2etest_fallbackpolicy__a_kiss:
	python e2etest/test.py --model $(model) --scriptfile e2etest/data/fallbackpolicy__a_kiss.yml

e2etest_main__changed:
	python e2etest/test.py --model $(model) --scriptfile e2etest/data/scenario__changed.yml

compile_lectures:
	/usr/bin/python3 teaching_assistant.py

