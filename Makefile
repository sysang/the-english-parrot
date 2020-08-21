help:
	@echo "make"
	@echo "    action"
	@echo "        Run action server"
	@echo "    training"
	@echo "        Training"
	@echo "    shell"
	@echo "        Start chatbot and shell I/O"
	@echo "    formatter"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    types"
	@echo "        Check for type errors using pytype."

action:
	bin/rasa run actions --actions actions

actiond:
	setsid ./actions/runactionserver.sh >./actions/logs/$(shell date "+%Y%m%d-%H%M").log 2>&1 < /dev/null &
	@ps -ef | awk '/[a]ctions\/runactionserver\.sh/'

stopactiond:
	ps -ef | awk '/[a]ctions\/runactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -9
	@ps -ef | awk '/[a]ctions\/runactionserver\.sh/'

restartactiond: stopactiond actiond

training:
	bin/rasa train -vv --augmentation 0

shell:
	bin/rasa shell -vv -m $(model)

visualize:
	bin/rasa visualize -vv --out data/graphs/$(shell date "+%Y%m%d-%H%M").html

run:
	@export ts=`/bin/date "+%Y%m%d-%H%M"`
	bin/rasa run -vv --log-file=logs/$(model)_run_$(shell date "+%Y%m%d-%H%M").log -m $(model)

formatter:
	black actions

lint:
	flake8 actions
	black --check actions

types:
	pytype --keep-going actions

e2etest_main__a_kiss:
	bin/python e2etest/test.py --model $(model) --scriptfile e2etest/data/scenario__a_kiss.yml

e2etest_fallbackpolicy__a_kiss:
	bin/python e2etest/test.py --model $(model) --scriptfile e2etest/data/fallbackpolicy__a_kiss.yml

e2etest_main__changed:
	bin/python e2etest/test.py --model $(model) --scriptfile e2etest/data/scenario__changed.yml
