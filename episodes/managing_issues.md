---
title: "Managing issues"
teaching: 30
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- How can labelling help me manage issues on a repository?
- How do I add labels to issues?
- What are the recommended labels, and when should I use them?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After following this section, participants will be ready to practice the following skills:

- explain the value of labelling issues
- apply labels to issues
- explore the set of labels recommended by The Carpentries

::::::::::::::::::::::::::::::::::::::::::::::::

## Issue Triage

Maintainers typically do not have time to respond immediately to
every new issue and comment that is added to their repository.
In a more common scenario, a Maintainer visits their repository and finds
several new issues and pull requests,
plus some new comments and changes to those that were open at the end of their previous visit.

A good first step to take in these circumstances is _issue triage_:
time spent processing the open issues and figuring out what should be prioritised,
what can be closed, what needs to be brought to the attention of others in the community
(co-Maintainers, Curriculum Advisors, would-be contributors, Core Team, etc),
and so on.

::: callout

## The Value of Teamwork

Note that this triage process is usually made much easier, more efficient, and more fun
when co-Maintainers of a lesson can meet synchronously to
work through issues and pull requests together.

Community members have reported positive experience with short,
regularly scheduled e.g. monthly coworking sessions with their Maintainer team,
using screen-sharing and focussed discussion to distribute tasks and
collaboratively determine how to process and respond to contributions on their repositories.

It can also be a good opportunity for Maintainers to get know each other better,
and to share their skills and experience with Git, GitHub, and the lesson infrastructure.

:::

## Labelling Issues

The triage process can be improved with effective use of _labels_ applied to issues.
Issues are tags that can be applied to issues (and pull requests),
annotating them according to their status, type, complexity, etc.
When labels are applied to an issue,
they appear next to it in the issue listing for the repository.
Clicking on a label will show you a list of all issues with that label.

When returning to a lesson repository after some time away,
labels applied to old issues can help to remind you of the context for each of those,
and labels can be added/updated as you triage the issue list.

::::::::::::::::::::::::::::::::::::::::::::::::: instructor

### Example Issues

Use your example repository to demonstrate how to label issues,
and to discuss the appropriate use of some important labels here.

If you are using example repositories [generated with the accompanying script](instructors/instructor-notes.md),
I recommend the following labels:

* Issue 1 ("Typos in recipe instructions"): `type:typo text`, `good first issue`, `help wanted`
* Issue 2 ("Cinnamon rolls burnt 🔥"): `type:bug`, `good first issue`, `help wanted`
* Issue 3 ("Alternative to sourdough cinnamon rolls"): `status:refer to cac`, `type:discussion`

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Inviting Community Contributions

Lesson repositories are open source and publicly-visible,
and you can expect some spontaneous contributions from the wider community.
However, in some circumstances, you may want to bring particular items
to the attention of community members.

### Refer to CAC

When you want or need to
[refer an issue/contribution to the Curriculum Advisory Committee](https://carpentries.github.io/maintainer-onboarding/04-communicate-advisors.html)
for your lesson, you should add the `status:refer to cac` label,
and tag the CAC in the relevant issue/pull request discussion thread
(e.g. `@datacarpentry/curriculum-advisors-image`).

Adding this label will help members of the CAC more easily identify and
browse through the items they need to discuss,
increasing the likelihood that you will receive a timely response.

### Help Wanted & Good First Issue

The `help wanted` and `good first issue` labels can be useful to draw attention
from new contributors.
In particular,
the `help wanted` label can be used to flag up issues that the Maintainers
would particularly appreciate external support on.
Issues with this label in any of The Carpentries official lesson repositories
will appear in the listing on
[the _Help Wanted Issues_ page of the website](https://carpentries.org/help-wanted-issues/),
where new community members are often directed to find opportunities to contribute to
a lesson repository.

The `good first issue` label is used to identify issues that do not require in-depth knowledge
of the project and its infrastructure, etc.
Newcomers to the project can use this label to find opportunities to make their first contribution.
GitHub provides a view of all of a repository's issues with the `good first issue` label
on the `/contribute` page for that repository, e.g. https://github.com/github/docs/contribute

::: callout

## Batch Labelling

Labels can be applied to issues in batches from the issue listing page.
Check the box next to each issue you want to apply a given label to,
then click the "Label" dropdown in the top bar of the listing,
and choose the label(s) you want to apply to these issues.

:::

:::::::::::::::::::::::::::::::::::::: keypoints

- Labelling issues can help you prioritise issues and bring them to the community's attention.
- Labels can be added to an issue using the right sidebar menu of the GitHub web interface.
- The Carpentries provides a recommend set of labels, and has systems and processes that work with some of these.

::::::::::::::::::::::::::::::::::::::::::::::::
