#!/bin/env python
'''Create example lesson repositories for use in a GitHub Skill-up for Maintainers.

The script uses the GitHub API to create duplicate repositories based on the
carpentries/crispy-doodle template, and invite skill-up participants to join them.

usage: python maintainer-skill-up-setup.py date-of-skill-up host-username [usernames-file]

Input parameters:

- date-of-skill-up: the date that the skill-up will take place (YYYY-MM-DD)
- host-username: the GitHub username/handle of the session host
- usernames-file: path to a file of GitHub usernames to create repositories for (optional). Default: ./github_usernames.txt

After running, the script outputs a list of the names (slugs) of the repositories created.
In future, I hope to add a script that can handle this list to
transfer ownership of the repositories to their respective participants.

** Authenticating to GitHub **
The script makes extensive use of the `gh` command-line tool for
interacting with GitHub's API.
Before using the script for the first time, you need to do the following:
1. Download and install `gh` from https://cli.github.com/
2. Authenticate to GitHub with `gh auth login`

'''

from os import chdir
import random
import string
import subprocess
import sys
from time import sleep

# from user sth at https://stackoverflow.com/a/2030081
def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

##############################
# set up remote repositories #
##############################

def create_repo(datestring, host_username, collab_username):
    # create remote repository
    repo_name = f'github-skillup-{datestring}-{collab_username}'
    subprocess.check_output('git switch main', shell=True)
    sys.stderr.write(f'creating remote repo: {repo_name}\n')
    create_repo = subprocess.check_output(f'gh repo create {repo_name} --public --source=. --remote={collab_username} --push --description="An example lesson teaching how to bake sourdough cinnamon rolls."', shell=True)
    subprocess.check_output(f'gh repo set-default {host_username}/{repo_name}', shell=True)
    subprocess.check_output(f'git switch md-outputs', shell=True)
    subprocess.check_output(f'git push {collab_username} md-outputs', shell=True)
    subprocess.check_output(f'git switch gh-pages', shell=True)
    subprocess.check_output(f'git push {collab_username} gh-pages', shell=True)
    subprocess.check_output(f'git switch main', shell=True)
    # TODO add Pages site URL to About box?
    return repo_name

def add_labels(to_remove, to_add):
    # add standard Carpentries labels to repo
    sys.stderr.write('deleting default issue labels\n')
    for label in to_remove:
        subprocess.check_output(f'gh label delete {label} --yes', shell=True)
        sleep(1)
    sys.stderr.write('adding Carpentries standard set of issue labels to repository\n')
    for label, color, desc in to_add:
        subprocess.check_output(f'gh label create {label} --color={color} --description={desc}', shell=True)
        sleep(1)

def add_collaborator(collab_username, host_username, repo_name):
    # grant access to remote repository, commenting out role as this only applies to org-owned repos
    sys.stderr.write(f'inviting {collab_username} to join repository\n')
    subprocess.check_output(f'gh api --method PUT -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /repos/{host_username}/{repo_name}/collaborators/{collab_username}  --silent', shell=True) # add "-f permission='maintain'" if working wth repositories in an org

####################################
# open issues on remote repository #
####################################

def open_issue(title, body_file):
    sys.stderr.write(f'opening issue {title}\n')
    subprocess.check_output(f'gh issue create --title="{title}" --body-file={body_file}', shell=True)
    sleep(1)

###########################################
# open pull requests on remote repository #
###########################################

def open_pr(branch, title, body_file, username):
    sys.stderr.write(f'opening pull request "{title}"\n')
    subprocess.check_output(f'git switch {branch}', shell=True)
    subprocess.check_output(f'git push {username} {branch}', shell=True)
    subprocess.check_output(f'gh pr create --head={branch} --base=main --title="{title}" --body-file={body_file}', shell=True)
    sleep(1)

##############################
# run the script             #
##############################
if __name__ == '__main__':
    ######################################
    # hard-coded config for the skill-up #
    ######################################
    remote = 'git@github.com:carpentries/crispy-doodle.git' # the "template of templates"
    clone_name = randomword(16) # a randomised name for the folder where crispy-doodle will be cloned
    branches = ['gh-pages', 'md-outputs', 'setup', 'challenge-3', 'update-readme', 'solution-3a', 'solution-3b'] # a list of the branches that we need to set up the skill-up

    ######################################
    # user-defined parameters            #
    ######################################
    datestring = sys.argv[1]          # the date of the skill-up, used in the remote repository name
    host_username = sys.argv[2]       # the GitHub handle of the skill-up host
    try:
        usernames_file = sys.argv[3]  # the name of the file from which to read participant usernames
    except IndexError:
        usernames_file = './github_usernames.txt'

    ######################################
    # inputs to read from a file         #
    ######################################

    # populate a list of participant usernames
    usernames = []
    with open(usernames_file, 'r') as infh:
        for inline in infh.readlines():
            usernames.append(inline.strip())

    # populate a list of issue labels to delete from the generated repositories
    default_labels = []
    with open('./supporting-files/issue-labels/standard-labels.csv', 'r') as infh:
        for inline in infh.readlines():
            default_labels.append(inline.strip())

    # populate a list of issue labels to add to the generated repositories
    carpentries_labels = []
    with open('./supporting-files/issue-labels/carpentries-labels.csv', 'r') as infh:
        for inline in infh.readlines():
            # lines have format label_name, label_color, label_description
            carpentries_labels.append(inline.strip().split(','))

    # create local clone of crispy-doodle in a randomly-named folder
    subprocess.check_output(f'git clone {remote} {clone_name} && cd {clone_name}', shell=True)
    chdir(clone_name) # move into the newly-created directory

    # fetch relevant branches for this skill-up
    for branch_name in branches:
        subprocess.check_output(f'git fetch origin {branch_name}', shell=True)

    # merge setup branch
    subprocess.check_output('git merge --no-edit origin/setup', shell=True)

    # merge challenge branches for this skill-up
    subprocess.check_output('git merge --no-edit origin/challenge-3', shell=True)

    repositories = [] # initialise the list of repository names that will be generated

    for collaborator_username in usernames:
        repo_name = create_repo(datestring, host_username, collaborator_username)
        sleep(5) # prevents spurious 404 errors caused by trying to edit repository issue labels before repo creation process has completed
        add_labels(default_labels, carpentries_labels)
        add_collaborator(collaborator_username, host_username, repo_name)
        open_issue('Typos in recipe instructions', '../supporting-files/typo-fix-pr/issue-body.md')
        sleep(1) # be kind to the GitHub API server
        open_issue('Cinnamon rolls burnt 🔥', '../supporting-files/temp-conversion-fix-pr/issue-body.md')
        sleep(1) # be kind to the GitHub API server
        open_issue('Alternative to sourdough cinnamon rolls', '../supporting-files/central-example-issue/issue-body.md')
        sleep(1) # be kind to the GitHub API server
        open_pr('update-readme', 'Add detail to the project README', '../supporting-files/readme-update-pr/pr-body.md', collaborator_username)
        sleep(1) # be kind to the GitHub API server
        open_pr('solution-3a', 'Fix typos in recipe instructions', '../supporting-files/typo-fix-pr/pr-body.md', collaborator_username)
        sleep(1) # be kind to the GitHub API server
        open_pr('solution-3b', 'Fix oven temperature conversion', '../supporting-files/temp-conversion-fix-pr/pr-body.md', collaborator_username)
        repositories.append(repo_name)
        sleep(1) # be kind to the GitHub API server

    # output a list of the particpant repository names
    sys.stdout.write('\n'.join(repositories)+'\n')
