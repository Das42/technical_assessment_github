# Welcome! This repo will show you how to become an honorary member of the annex, and will test your knowledge of Git/GitHub concepts along the way.
### Independently complete the steps below once you have finished the [GitHub Ultimate](https://das42.udemy.com/github-ultimate/learn/lecture/4493018#overview) course on [Udemy](https://das42.udemy.com/organization/home/). All of the steps should be completed from your command line interface (henceforth referred to as CLI) unless specified otherwise. Feel free to reach out to Logan with any questions you might have about this assignment.

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
  * Clone your forked copy of this repo using SSH and move into it.
    * _**hint:**_ Review _[Session 7](https://das42.udemy.com/github-ultimate/learn/lecture/4731854#content)_ of the Udemy training course.

#### Step 4:
  * Create a new branch called `personal`, and switch to it.
  
#### Step 5:
  * Edit the `jokes.md` file by adding your name and a joke in the existing format.
  * Commit these changes.
    * Be sure to include a commit message.

#### Step 6:
  * Push your local personal branch upstream to your remote repo.
    * _**hint:**_ If you try to accomplish this using `git push` alone, you will get an error. This is because your personal branch only exists locally, and doesn't yet have an upstream origin in your remote repo. To remedy this, you will need to initialize an upstream origin for your local person branch. Review _[Lecture 94](https://das42.udemy.com/github-ultimate/learn/lecture/4732118#overview)_ of the Udemy training course if you need a refresher on how to do this.
  * Check that your branch is up to date using `git status`.

#### Step 7:
  * Open the `collaborators.txt` file and remember who the last person listed is.
    * You will need to tag this person in a moment.
  * Hop over to GitHub in your web browser and create a pull request between your forked personal branch and the origin master branch `logan-DAS42/das42_git_check`.
    * Before submitting your pull request, tag Logan and one other person who's name appeared at the end of the `collaborators.txt` file as *Reviewers* on the pull request.
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
  * Create a new branch, calling it your first name, and switch to it.
  
#### Step 11:  
  * Create a text file in your personal branch called `YOURNAME_two_truths_one_lie.txt` and populate it accordingly.
  * Stage this file and commit these changes.
    * Be sure to include a commit message.

#### Step 12:
  * Switch to your local master branch and make sure it is up to date with the upstream origin.
    * If it is not, pull down the changes.
    * _**hint:**_ `git status` `git fetch` `git pull`
    
#### Step 13:
  * In the CLI, merge your local master branch with your _FIRSTNAME_ branch.
  * After doing so, push your local master branch up to the remote repo.
  
#### Step 14:
  * Hop over to the master branch of the origin repo on GitHub and verify that:
    1.) your unique `two_truths_one_lie` file is in the master branch
    2.) your joke is present in the `jokes.md` file in the master branch
    3.) your name appears in the `collaborators.txt` file

#### Step 15:
  * Message Logan once you've completed these steps.

#### Step 16:
  * Await Curtis's approval of your joke (minimum of two chuckles required) and eagerly await your letter of acceptance as an honorary member of the annex. 

#### Step 17:
  * Pat yourself on the back, because you're done.
