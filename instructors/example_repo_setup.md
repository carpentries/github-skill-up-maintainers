---
title: Setting Up Example Repositories
---

The `files/` directory of the source repository for this lesson includes a script,
`generate_example_repositories.py`,
which can be used to automate the setup of example repositories
for use in the skill-up.

For each participant registered for the skill-up,
the script will create a repository (owned by the skill-up host)
with:

- GitHub Pages enabled
- the participant invited to join the repo as a collaborator
- three open issues
- three open pull requests

The script takes ~2 minutes to run on the author's system.

To run the script, you will need:

1. Python >= 3.6 and Git
2. The `gh` executable installed on your system (https://cli.github.com/), with your user account authenticated
3. A file of participants' usernames
4. The folder of `supporting-files` included alongside the script inside `files/`

When you have all of these things, you can run the script with

```bash
python maintainer-skill-up-setup.py date-of-skill-up host-username usernames-file
```

where

- `date-of-skill-up` = the date that the skill-up will take place, in YYYY-MM-DD format
- `host-username` = the GitHub username/handle of the session host
- `usernames-file` = path to a file of GitHub usernames to create repositories for.
  This on is optional, and the script will look for a file called `./github_usernames.txt`
  by default.


:::::::::::::::::::::: callout

## Setting up an example repository for the host to use

To make your experience as similar as possible to the participants',
I recommend
creating a secondary GitHub account and
generating an example repository for that account to use.

You can then run the skill-up session while logged into that account,
to ensure that what displays on your screen matches the experience of
the other participants.

::::::::::::::::::::::::::::::
