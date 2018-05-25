# Git Gud at Rebase


**Don't ever use git merge**, unless you're doing the final merge of your feature branch into master, which should be done using the PR merge button.

1. `git clone <repo-name>` or `git pull --rebase` (while on the parent branch for your feature branch, this should be `master` most of the time)
1. `git checkout -B <branch-name>` to create a new local branch from the current commit you're on
1. `git push -u` to sync the remote branch with your local branch
    - You might have to set `default = current` in your `~/.gitconfig` otherwise you will have to invoke the longer `git branch --set-upstream-to origin/<branch-name>`
    - This is so that you can just invoke `git push` instead of `git push origin/<branch-name>`, which is error-prone because you can make a typo
1. Make necessary code changes
1. `git pull --rebase origin <parent-branch>` to get the latest changes from your `parent-branch`
    - NOTE: in some situations you will branch off of a feature branch, because you may be dependent on code that has not been merged into `master`, maybe pending review or requires additional work
    - If you take more than a day to write your code or if you're working on a high-traffic repo, you should probably invoke this a few times a day so you don't have to resolve a week's worth of conflicts all at once
1. `git push origin +branch-name` to force-push to your remote copy. When you invoke a `git rebase`, you're essentialy changing history, so you will need to force-push to sync up your remote branch
1. Complete the rest of your code
1. `git rebase -i origin/<parent-branch>` to start the rebase prompt to **squash your commits**
    - This will use the default editor of your terminal, you can set this to anything you want in your `~/.gitconfig`
    - Most of the time, you'll only be using `pick`, `s (squash)` or `f (fixup)`, maybe sometimes `r (reword)` if you consistently have to change your main commit message, which you shouldn't if you followed processes and best practices properly
1. `git push origin +branch-name`
1. Go to the repo on github.com and create a PR
1. If you're using ZenHub, go to the bottom of the newly-created PR and link it to the issue you were assigned
1. Go to a public slack channel (currently #engineering) and ask for a review, use the format: `@<name of reviewer> PTAL <link to PR>`
1. Fix up any feedback for your PR, squash your changes, and push to remote again
1. After you get an `LGTM`, do a final `git pull --rebase origin <parent-branch>` to make sure you have all the latest commits from master, force-push your changes to remote if there were any udpates
1. Click the green button to merge the feature branch into `master`, then click the button to delete the branch
    - We delete the branch so we can use branch names and prevent errors. There can be a situation where you have a branch named `refactor` which gets completed and merged into `master`. A few months later someone may need to refactor again and checkout the branch `refactor`. Becase this branch exists, this developer will be doing work on code that's a few months old. It's easy to catch this if you know how to use git or use a visualization tool, but this may throw off junior developers or people new to git

### Additional Resources
[Rebase Seminar Slides](rebase-work-flow.pdf)

### Scenarios

##### Multiple developers working in parallel on independent features

1. `DEV_N` ... `DEV_N+M` will branch off of `master`
1. Everyone will follow the steps above until the first PR merge
1. One of the developers will complete their PR first and merge the code to `master`
1. Everyone else does a `git pull --rebase origin master` to get the latest changes
1. Continue with rebase flow

##### Two developers working on dependent features

Assuming `DEV2` is depending on `DEV1`'s code

1. `DEV1` branches off of `master` to `FEATURE1`
1. `DEV1` writes and pushes some code that `DEV2` is dependent on
1. `DEV2` checkouts `FEATURE1` and then immediate invokes `git checkout -B FEATURE1_1`
1. `DEV1` and `DEV2` will continue to do work in isolation
1. Whenever `DEV1` pushes some commits and when `DEV2` is ready (you can't rebase if you have uncommitted code), do a `git pull --rebase origin FEATURE1` to get the latest changes, then do a force-push onto `FEATURE1_1` to sync up with its remote branch
1. `DEV1` will continue work and will eventually need to squash commits
1. `DEV1` should inform `DEV2` that commits were squashed, `DEV2` will then rebase off of `FEATURE1` to get the squashed history
2. `DEV1` will then merge the feature branch into `master`
3. `DEV2` will now rebase off of `master` to get the merged PR history and will continue to rebase off of `master` until completion of `FEATURE1_1`




# Git Commit Message Best Practices

Commit messages are important, we can use the git history to automate changelog generation. We can't automate this if we have messages like `sdjfhkjdshfjkdsfhdksj` or `fix`, which does not provide any information at all. here's a quick breakdown of main rules: 

- Use present tense for the **commit message**
- 50 characters max for **commit message** (don't end with period)
- 72 characters max per line for **commit body**, as many lines as you want
- commit message should be descriptive for the feature being implemented, something like `fixed tests` is not descriptive

Example:

```
server: add env config detection using dotenv lib

Environment will be different depending on the machine that the service
is deployed on, DEV will need to connect to the local intranet whereas
PROD deployments will need to rely on public infrastructure and will
also have a need to change configuration, like API PORT, on demand
```

The first line is the `commit message`, then the rest of the text is the `commit body`, separated by a newline.

The commit message is exactly `50 characters`. The commit body never exceeds `72 characters`, some text editors will work with git to enter a newline when a current line exceeds the `72 character` limit.

The `commit message` decribes the component affected and what was changed.

The `commit body` explains why the feature was implemented.

### Additional Resources
[How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
