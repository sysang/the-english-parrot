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
	setsid ./runactionserver.sh >./actions/actions.log 2>&1 < /dev/null &

stopactiond:
	ps -ef | awk '/[r]unactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -TERM

restartactiond:
	ps -ef | awk '/[r]unactionserver\.sh/{print $$2;}' | xargs echo "-${1}" | sed 's/\s//g' | xargs kill -TERM
	setsid ./runactionserver.sh >./actions/actions.log 2>&1 < /dev/null &

training:
	bin/rasa train -vv

shell:
	bin/rasa shell -vv -m $(model)

run:
	@export ts=`/bin/date "+%Y%m%d.%H%M"`
	bin/rasa run -vv -m $(model) --log-file=$(model)_run_$(ts).log

formatter:
	black actions

lint:
	flake8 actions
	black --check actions

types:
	pytype --keep-going actions

timestamp:
	@export ts=`/bin/date "+%Y%m%d.%H%M"`
	@echo $(ts)
