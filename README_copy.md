# Welcome! This repo will show you how to become an honorary member of the annex, and will help you practice Git along the way.
### Independently complete the steps below once you have finished the GitHub Ultimate course on Udemy. All of the steps should be completed from the command line unless specified otherwise. Feel free to reach out to Logan with any questions you might have about this assignment.

#### Step 1:
  * Fork this repo in GitHub.
    * _***hint:***_ Checkout the top left of the page.

#### Step 2:
  * Open your CLI of choice _(iTerm2, Terminal, etc.)_
  * In your `~/Desktop/` directory, create a new directory called `git_knowledge_check` and move into it.
      * _**hint:**_ `mkdir` `cd`
  * Once there, create another new directory named `forked_repo` and move into it.
      
#### Step 3:
  * Hop back over to GitHub in your web browser.
  * Next, clone your forked copy of this repo using SSH and move into it.
    * _**hint:**_ Review _[Session 7](https://das42.udemy.com/github-ultimate/learn/lecture/4731854#content)_ of the Udemy training course.

#### Step 4:
  * Create a new personal branch, calling it your first name, and switch to it
  
#### Step 5:
  * Create a text file in your branch called `YOURNAME_two_truths_one_lie.txt` and populate it accordingly.
  * Stage this file and commit these changes to your newly created personal branch.
    * Be sure to include a commit message.

#### Step 6:
  * Push your local personal branch upstream to your remote repo.
    * _**hint:**_ If you try to accomplish this using `git push` alone, you will get an error. This is because your personal branch only exists locally, and doesn't yet have an upstream origin in your remote repo. To remedy this, you will need to initialize an upstream origin for your local person branch. Review _[Lecture 94](https://das42.udemy.com/github-ultimate/learn/lecture/4732118#overview)_ of the Udemy training course if you need a refresher on how to do this.
  * Check that your branch is up to date using `git status`.

#### Step 7:
  * Hop over to GitHub in your web browser and create a pull request between your forked personal branch and the original master branch (`logan-DAS42/das42_git_check`).
    * Before submitting your pull request, tag Logan and one other person who's name appears in the `collaborators.txt` file as *Reviewers* on the pull request.
      * __**hint:**__ You can view this file from the CLI by switching to your local master branch and typing `vi collaborators.txt`.
  * Create the pull request.
  
#### Step 8:
  * Send Logan a message on Slack letting him know that you have created the pull request. Give him your GitHub username as well, so that he can add you as a Collaborator on the origin repo for the next steps of this assignment.

#### Step 9:
  * Once your pull request has been approved, and Logan has added you as a Collaborator, return to your CLI.
  * Create a new directory in your `~/Desktop/git_knowledge_check/` directory called `"origin_repo"`.
    * Your `~/Desktop/Git_Knowledge_Check/` directory should now contain two directories:
      * `forked_repo`
      * `origin_repo`
  * Using the same method as **Step 3** above, clone the origin repo from GitHub into `~/Desktop/git_knowledge_check/origin_repo`.

#### Step 10:
  * While on the local master branch, add your name to the `collaborators.txt` file.
  * Next, edit the `jokes.md` file by adding your name and a joke in the existing format.
  
  
# STILL WORKING ON THIS

#### Step 11:
  * From here, ensure that your local master branch contains your unique _two_truths_on_lie_ file and the _jokes.md_ file with your joke in it.
  * Push your local master branch to the remote repo.

#### Step 12:
  * Hop back over to GitHub to visually verify that your unique _two_truths_one_lie_ file has been added to the master branch, and that your joke is present in the master _jokes.md_ file. 

#### Step 13:
  * Message Logan once you've completed these steps.

#### Step 14:
  * Await King Curtis's approval of your joke (minimum of two chuckles required) and eagerly await your letter of acceptance into the annex. 
