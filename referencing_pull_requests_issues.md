---
title: "Referencing pull-requests and issues"
teaching: 0
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions 

- How do I reference issues and pull requests?
- How can issues be automatically closed when a pull request is merged?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- reference issues and pull requests by their number
- implement keywords to trigger automatic closue of issues when fixed by a pull request

::::::::::::::::::::::::::::::::::::::::::::::::

- It can be helpful to refer to issues and pull requests in conversations elsewhere in a repository
- Every issue and PR has a unique number (based on the order in which they were created)
- These numbers can be used, preceded by `#`, to reference a given issue or PR.
- Additionally, PRs (and commit messages) that include particular phrases will trigger the automatic closure of an issue:
  - "closes"
  - "fixes"
  - "resolves"


:::::::::::::::::::::::::::::::::::::: keypoints 

- Issues and pull requests can be referred to by their number within a repository.
- Pull requests descriptions that include "fixes #XYZ", "resolves #XYZ", or "closes #XYZ" will all close issue number XYZ when they are merged.

::::::::::::::::::::::::::::::::::::::::::::::::
