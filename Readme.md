# Model the Dynamics of Gender in Intro CS at UC Berkeley. 

A Supervised Learning Project

## Install

This project requires Python 2.7 and the following Python libraries installed:

- [Pandas](http://pandas.pydata.org/)
- [NumPy](http://www.numpy.org/)
- [Scikit-learn](http://scikit-learn.org/stable/)

## Code

The code is provided in the notebook `genderedCSExperience.ipynb`.

To open it, go to the top-level project directory `genderCSExperience/` and start the notebook server:

```jupyter notebook```

This should open a web browser to the server's dashboard (typically `http://127.0.0.1:8888`). Click on the appropriate notebook (`.ipynb`) to open it, and follow the instructions.

## Run

To run a code cell in the notebook, hit `Shift+Enter`. Any output will be displayed below the corresponding cell.


## Data

The dataset that is used in this project is unfortunately not available for mass consumption, as it contains sensitive, *personally identifiable* student data.

The dataset was generate through the use of a survey instrument which contains the following attributes for each data point based on a likert scale of 1 to 5, 1 *strongly disagree* and 5 corresponding to *strongly agree*. Some items have *yes* and *no* answers.

#### Self reported attitudes about CS
- atcs_1 I like to use computer science to solve problems.
- atcs_2 I can learn to understand computing concepts.
- atcs_3 I can achieve good grades (C or better) in computing courses.
- atcs_4 I do not like using computer science to solve problems.
- atcs_5 I am confident that I can solve problems by using computation
- atcs_6 The challenge of solving problems using computer science appeals to me.
- atcs_7 I am comfortable with learning computing concepts.
- atcs_8 I am confident about my abilities with regards to computer science.
- atcs_9 I do think I can learn to understand computing concepts.

#### Gendered belief about CS ability
- atcsgender_1 Women are less capable of success in CS than men.
- atcsgender_2 Women are smarter than men.
- atcsgender_3 Men have better math and science abilities than women.

#### Career driven beliefs about CS
- atcsjob_1 Knowledge of computing will allow me to secure a good job.
- atcsjob_2 My career goals do not require that I learn computing skills.

#### Self reported attitudes about computational thinking
- atct_1 I am good at solving a problem by thinking about similar problems I’ve solved before.
- atct_2 I have good research skills.
- atct_3 I am good at using online search tools.
- atct_4 I am persistent at solving puzzles or logic problems.
- atct_5 I know how to write computer programs
- atct_6 I am good at building things.
- atct_7 I’m good at ignoring irrelevant details to solve a problem.
- atct_8 I know how to write a computer program to solve a problem.

#### Self reported attitudes about CS class belonging
- blg_1 In this class, I feel I belong.
- blg_2 In this class, I feel awkward and out of place.
- blg_3 In this class, I feel like my ideas count.
- blg_4 In this class, I feel like I matter.

#### Self reported beliefs about collegiality
- clet_1 I work well in teams.
- clet_2 I think about the ethical, legal, and social implications of computing.
- cltrcmp_1 I am comfortable interacting with peers from different backgrounds than my own (based on race, sexuality, income, and so on.)
- cltrcmp_2 I have good cultural competence, or the ability to interact effectively with people from diverse backgrounds.

#### Demographics
- gender Could I please know your gender

#### CS mentors and role models
- mtr_1 Before I came to UC Berkeley, I knew people who have careers in Computer Science.
- mtr_2 There are people with careers in Computer Science who look like me.
- mtr_3 I have role models within the Computer Science field that look like me.

#### Prior collegiate CS exposure
- prcs_1 Did you take a CS course in High School?
- prcs_2 Did you have any exposure to Computer Science before UC Berkeley?
- prcs_3 Did a family member introduce you to Computer Science?
- prcs_4 Did you have a close family member who is a Computer Scientist or is affiliated with computing industry?
- prcs_5 Did your high school offer AP CS?


## License

The contents of this repository are covered under the [GNU GENERAL PUBLIC LICENSE](License.md).
