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
	@export ts=`/bin/date "+%Y%m%d-%H%M"`
	setsid ./runactionserver.sh >./actions/logs/`echo $$ts;`.log 2>&1 < /dev/null &
	@ps -ef | awk '/[r]unactionserver\.sh/'

stopactiond:
	ps -ef | awk '/[r]unactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -9
	@ps -ef | awk '/[r]unactionserver\.sh/'

restartactiond:
	ps -ef | awk '/[r]unactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -9
	@export ts=`/bin/date "+%Y%m%d.%H%M"`
	setsid ./runactionserver.sh >./actions/logs/`echo $$ts;`.log 2>&1 < /dev/null &
	@ps -ef | awk '/[r]unactionserver\.sh/'

training:
	bin/rasa train -vv --augmentation 0

shell:
	bin/rasa shell -vv -m $(model)

run:
	export ts=`/bin/date "+%Y%m%d-%H%M"`
	bin/rasa run -vv --log-file=logs/$(model)_run_`echo $$ts;`.log -m $(model)

formatter:
	black actions

lint:
	flake8 actions
	black --check actions

types:
	pytype --keep-going actions

timestamp:
	@export ts=`/bin/date "+%Y%m%d-%H%M"`
	echo $$ts

e2etest_main:
	bin/python e2etest/test.py --model $(model) --scriptfile e2etest/data/main_scenario.yml

e2etest_nlufallbackpolicy:
	bin/python e2etest/test.py --model $(model) --scriptfile e2etest/data/nlufallbackpolicy.yml

