---
title: "Reviewing pull-requests"
teaching: 30
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What features does GitHub provide to facilitate reviewing pull requests?
- What are the different options for the outcome of a pull request review, and when should I use each one?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After following this section, participants will be ready to practice the following skills:

- create comments on particular lines and ranges of lines in the changes proposed by a pull request
- suggest specific changes to a pull request
- select the "approve", "comment", or "request changes" outcomes of a pull request review

::::::::::::::::::::::::::::::::::::::::::::::::

- reviewing PRs is one of the most important tasks for a Maintainer
- the way you review a pull request, and communicate with the person who opened it,
  can have an enormous impact on their motivation to contribute again
- GitHub provides several features that can improve your experience as a reviewer,
  and make it easier for contributors to follow up on your review

## Line-by-Line Comments

- see the changes proposed in a PR via the _Files Changed_ tab
- if you want to comment on a particular line, hover your mouse over it and click the `+` symbol
- comments can be added on their own, or as part of a _Review_: a commentary on the pull request as a whole
- to comment on a range of lines, click-and-hold on the `+` for the first line in the range, and drag your cursor down the range, then release

## Suggesting Changes

- as well as adding comments line-by-line, you can also suggest specific changes, e.g. to fix a typo, suggest improved wording, etc.
- take the same approach to start a comment on a line or range of lines, then click the "add a suggestion" button, and edit the source content that appears in the input box
- this makes it much easier for contributors to a) understand reviewers' suggestions, and b) implement them

## Finishing a Review

- when you have finished commenting on particular lines, and suggesting changes, you can finish your review by clicking the "Review changes" or "Finish your review" button near the top-right of the screen
- add general comments, a summary of your review, etc - don't forget to thank them for taking the time to contribute! - and choose one of the three options:
  - "Comment" - a general comment, with no firm outcome. Can be used to complete a review before a pull request is closed.
  - "Approve" - approve the PR for merging. Some people use this when suggesting only very minor or optional changes - if you want to do this, make sure you are explicit about what changes you are suggesting etc before the PR can be merged
  - "Request changes" - indicates that changes would be required to the PR before you would be willing to merge it.

::::::::::::::::::::::::::::::::::::::::::::::::: instructor

### Reviewing Example Pull Requests

Use the example repository to show an example of reviewing a pull request,
demonstrating:

* line-specific comments
* suggesting a change
* approving/requesting changes at the end of the review

If you are using example repositories [generated with the accompanying script](instructors/instructor-notes.md),
I recommend using the "Add detail to the project README" pull request
to demonstrate line-by-line commenting and suggesting changes:
you can suggest that the contributor uses a different email address, for example.

The purpose of the other two pull requests is to:

1. Repeat the reviewing workflow two more times,
   giving you a chance to emphasise the important steps
   and encourage good communications practices.
2. Create a merge conflict that can be resolved in the GitHub web browser interface
   (see the Instructor Note for the next episode).

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


::: callout

## Saved Replies

- You can add "saved replies" to your GitHub account
- These can be used to automatically input a template response, on issues, PRs, etc
- Use these if you find that you are often saying the same or similar things to people

:::

:::::::::::::::::::::::::::::::::::::: keypoints

- What features does GitHub provide to facilitate reviewing pull requests?
- What are the different options for the outcome of a pull request review, and when should I use each one?

::::::::::::::::::::::::::::::::::::::::::::::::
