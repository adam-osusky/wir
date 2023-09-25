# Word Importance Ranker

## Description
Word Importance Ranker is a powerful web application designed to engage users in the interactive task of ranking words within short text passages based on their perceived importance. This platform allows users to contribute their annotations and compare their rankings with others, fostering a sense of competition and collaboration.

Features:
- Word Ranking
  - Users are presented with short text passages and are tasked with ordering the words within them based on their importance. This annotation process helps to crowdsource valuable insights about word importance in various contexts.

- Score System
  - WordRanker implements a scoring system that rewards users for annotations that closely align with those of other participants. The closer your ranking is to the consensus, the higher your score will be. This encourages users to strive for accuracy and consensus.

- Leaderboards
  - WordRanker provides a dynamic leaderboard feature where users can see how their scores stack up against other participants. Compete with friends, colleagues, or even global users to establish yourself as a top word ranker!

- Customizable Dataset
  - Developers can easily customize the dataset of text passages on which users annotate. This flexibility allows WordRanker to be adapted for various domains and purposes, making it a valuable tool for data annotation and analysis.


## Getting started
To set up this web application, follow these steps:

1. Clone this repository and install the required dependencies.
    ```commandline
    git clone git@gitlab.mff.cuni.cz:osuskya/rocnikac.git
    cd rocnikac/
    python -m venv env  # you can change the name of your virtual env
    . env/bin/activate
    pip install -r requirements.txt
    ```

2. Run the following commands to create the database tables and apply initial migrations
    ```commandline
    cd ranker_site/
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Fill the database with text to be ranked by users
    ```commandline
    python rankings/prepare_data.py --dataset 'glue;ax' --num_samples 3
    ```
   - In `ranker_site/rankings/prepare_data.py` you can specify your own dataset from which the text is being used. Currently it is implemented for easy use of huggingface datasets.
   - The text is being tokenized by https://pypi.org/project/mosestokenizer/ tokenizer
   - Feel free to add your own preprocessing.

4. To access the Django admin panel and perform administrative tasks, create a superuser account:
    ```commandline
    python manage.py createsuperuser
    ```

5. Start the Django development server to run the application locally:
    ```commandline
    python manage.py runserver
    ```

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
