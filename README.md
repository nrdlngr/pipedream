# pipedream
Experimental CLI to integrate AWS Code Pipeline with ECS/ECR.

## Installation
1. Clone this repo.
2. Install `python`, `pip`, and `virtualenv` (if you don't already have them).
3. Change into the `pipedream` directory and create a virtualenv: `$ cd pipedream && virtualenv venv`
4. Activate the virtualenv: `$ . venv/bin/activate`
5. Run the setup utility: `$ pip install --editable .`
6. View the help: `$ pipedream --help`
7. Run the command with some options and an arbitrary GitHub repo name: `$ pipedream nrdlngr/pipedream`

Note that this program doesn't really do anything useful yet except testing for AWS creds and printing the AWS account ID. 

