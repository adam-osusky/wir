# Word Importance Ranker

## Description
Word Importance Ranker is a simple web application designed to engage users in the interactive task of ranking words within short text passages based on their perceived importance. This platform allows users to contribute their annotations and compare their rankings with others, fostering a sense of competition and collaboration.

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
   The Django project should now be accessible at http://localhost:8000/dashboard/ in your web browser.

## Usage
Registration: Initiate by registering for an account. Click on the "Register a new account" button to create your user profile. Registration is mandatory to track your progress and enable full participation.

Start Ranking: Upon registration, click the "Start" button to commence word-ranking tasks. You will encounter a short text passage where every word is presented as a clickable button. Your objective is to sequence these words based on perceived importance.

Rank Words: Click on the words to establish their order of importance according to your judgment. Engage with the content and thoughtfully evaluate each word's significance within the passage.

Submit and Score: After arranging the words, click "Submit Order". Your rankings will be assessed, and you will receive a score. This score is determined by the degree of alignment between your ranking and that of other participants. The scoring mechanism emphasizes precision and promotes competition and cooperation.

Learn from Feedback: The scoring system provides instructive feedback. A higher score is achieved when your rankings closely match the consensus of other users. Leverage this feedback to refine your word-ranking skills and gain insights into how others perceive word importance.

Explore Leaderboards: Interested in assessing your word-ranking abilities relative to others? Navigate to the "Leaderboards" section on the main dashboard. Here, you can view your ranking in comparison to other users. Compete with peers or global participants to establish your status as a proficient word ranker. This feature facilitates progress tracking and motivation.