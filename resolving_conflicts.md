---
title: "Resolving conflicts"
teaching: 15
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- When might I encounter merge conflicts while maintaining/developing a lesson?
- How can I resolve simple conflicts in the GitHub web interface?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After following this section, participants will be ready to practice the following skills:

- resolve merge conflicts using the GitHub web interface

::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::::::::::: instructor

### Example Conflicts

Use the example repository to show an example of a pull request that is
blocked by a simple conflict,
then demonstrate how you can resolve this using the web interface.

If you are using example repositories [generated with the accompanying script](instructors/instructor-notes.md),
a simple conflict can be introduced by merging one of the two pull requests
suggesting changes to `recipe_instructions.Rmd`.
These two pull requests ("Fix typos in recipe instructions" and "Fix oven temperature conversion")
make edits to the same line in the file.

To resolve the conflict, keep the changes made by both pull requests
(i.e. the typo fix and the temperature conversion).

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


## What is a merge conflict?

A merge conflict occurs when Git is not able to automatically integrate (_merge_)
the changes in a branch with the version of the relevant file(s) into another branch
(usually the default or main branch) of the project.

Conflicts are seen when the target branch (usually `main`)
has changed since the branch for the pull request was created.
Often, Git is able to combine the two sets of changes without any trouble.
But sometimes it gets stuck, and requires a human to intervene and
decide how multiple changes should be combined, which change should take precedence, etc.

When these conflicts arise within a file,
Git marks up the file contents to highlight them.
The conflicts looks something like this:

```
<<<<<<< pr-branch
this is one version of the line. it exists in the version of this file in the pr-branch branch.
=======
this is another version of the same line. it exists in the version of this file in the main branch.
>>>>>>> main
```

## Resolving a Merge Conflict

Before the PR can be merged,
someone (usually the contributor who opened the pull request, or one of the repository Maintainers)
needs to resolve each of these conflicts by:

1. Figuring out which version (or combination of versions) of the lines should be kept in the file.
2. Removing all other lines (including the `<`, `=`, and `>` symbols) to leave only that resolved version.

After that has been done, and no conflicts remain to be resolved,
the branch can be updated, bringing it back in line with the changes in the target branch.

GitHub provides an interface to help you do this,
with buttons for quick navigation between multiple conflicts,
highlighting of the conflicting parts of the file, etc.

::: callout

## Larger Conflicts

Sometimes the conflicts between branches will be too large or too complex to be resolved
within the GitHub web interface.
In these cases, the conflicts will need to be resolved on the command line.

GitHub provides [a guide to resolving conflicts on the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line),
and other tools exist to help with merging and resolving conflicts.

:::

::::::::::::::::::::::::::::::::::::::::::::::::: instructor

### Still Have Time Left?

If you still have time remaining in the skill-up session,
consider using it to:

1. Demonstrate the VS Code Web IDE interface to a repository,
   accessed by hitting <kbd>.</kbd> while browsing the contents of the repository.
2. Talk about [debugging strategies when GitHub Actions fail](https://carpentries.github.io/lesson-development-training/infrastructure.html#headingSpoiler1) on a repository/pull request.
3. Open up a discussion about how Maintainers could coordinate their efforts on a lesson.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- You may encounter merge conflicts in large pull requests and those that have been open for some time.
- GitHub provides an interface to resolve simple conflicts in the GitHub web interface.

::::::::::::::::::::::::::::::::::::::::::::::::
