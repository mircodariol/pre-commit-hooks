# Contributing Guidelines

## Introduction

Thank you for considering contributing to this project! We appreciate your time and look forward to learning from your insights.

## Git Conventional Commit Standard

We follow the Conventional Commits standard for our git commit messages. This leads to more readable messages that are easy to follow when looking through the project history.

### Commit Message Format

Each commit message consists of a **header**, a **body**, and a **footer**. The header has a special format that includes a **type**, an optional **scope**, and a **description**:

```
<type>(<scope>): <description> <BLANK LINE> <body> <BLANK LINE> <footer>
```

#### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

#### Scope

The scope should be the name of the npm package affected (as perceived by the person reading the changelog generated from commit messages).

#### Description

The description is a short description of the change.

#### Body

Just as in the description, the body should be a brief description of the change.

#### Footer

The footer should contain any information about **Breaking Changes** and is also the place to reference GitHub issues that this commit closes.

### Example

Here is an example of the release type that will be taken from a commit message:

```
feat(user-profile): add 'graphical' option
```

In this example, the commit adds a new feature to the user-profile, namely a ‘graphical’ option.

### Conclusion
Thank you for following our contributing guidelines. We look forward to your pull requests and insightful discussions.
