# Git Cheatsheet & Tricks

A comprehensive guide to Git commands, workflows, and advanced tricks for developers.

---

## Table of Contents
1. [Basic Commands](#basic-commands)
2. [Repository Setup](#repository-setup)
3. [Branching & Merging](#branching--merging)
4. [Staging & Committing](#staging--committing)
5. [Remote Operations](#remote-operations)
6. [Viewing History](#viewing-history)
7. [Undoing Changes](#undoing-changes)
8. [Advanced Tricks](#advanced-tricks)
9. [Git Workflows](#git-workflows)
10. [Configuration](#configuration)
11. [Troubleshooting](#troubleshooting)

---

## Basic Commands

### Essential Daily Commands
```bash
# Check status of working directory
git status

# Add files to staging area
git add <file>
git add .                    # Add all files
git add -A                   # Add all files including deleted

# Commit changes
git commit -m "commit message"
git commit -am "message"     # Add and commit in one step

# Push to remote
git push
git push origin main

# Pull from remote
git pull
git pull origin main

# Clone repository
git clone <url>
git clone <url> <directory>
```

### Quick Status Check
```bash
# Short status format
git status -s

# Show branch and tracking info
git status -b

# Show ignored files
git status --ignored
```

---

## Repository Setup

### Initialize Repository
```bash
# Initialize new repository
git init

# Initialize with specific branch name
git init -b main

# Initialize bare repository (for servers)
git init --bare
```

### First Time Setup
```bash
# Set global user info
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim
```

### Connect to Remote
```bash
# Add remote origin
git remote add origin <url>

# Verify remote
git remote -v

# Change remote URL
git remote set-url origin <new-url>

# Remove remote
git remote remove origin
```

---

## Branching & Merging

### Branch Operations
```bash
# List branches
git branch                   # Local branches
git branch -r               # Remote branches
git branch -a               # All branches

# Create new branch
git branch <branch-name>
git checkout -b <branch-name>    # Create and switch
git switch -c <branch-name>      # Modern alternative

# Switch branches
git checkout <branch-name>
git switch <branch-name>         # Modern alternative

# Delete branch
git branch -d <branch-name>      # Safe delete
git branch -D <branch-name>      # Force delete

# Rename branch
git branch -m <old-name> <new-name>
git branch -m <new-name>         # Rename current branch
```

### Merging
```bash
# Merge branch into current branch
git merge <branch-name>

# Merge with no fast-forward (creates merge commit)
git merge --no-ff <branch-name>

# Squash merge (combine all commits into one)
git merge --squash <branch-name>

# Abort merge
git merge --abort
```

### Rebasing
```bash
# Rebase current branch onto another
git rebase <branch-name>

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Continue rebase after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort

# Rebase onto main and push
git rebase main
git push --force-with-lease
```

---

## Staging & Committing

### Staging Files
```bash
# Add specific file
git add <file>

# Add all files in directory
git add <directory>/

# Add all modified files
git add -u

# Add all files (new, modified, deleted)
git add -A

# Add parts of a file interactively
git add -p <file>

# Remove file from staging
git reset HEAD <file>
git restore --staged <file>     # Modern alternative
```

### Committing
```bash
# Basic commit
git commit -m "commit message"

# Commit with detailed message
git commit -m "Title" -m "Description"

# Add and commit in one step
git commit -am "message"

# Amend last commit
git commit --amend
git commit --amend -m "new message"

# Commit with specific date
git commit --date="2023-01-01 12:00:00" -m "message"

# Empty commit (useful for triggering CI)
git commit --allow-empty -m "trigger build"
```

### Commit Message Best Practices
```bash
# Good commit message format:
# <type>(<scope>): <subject>
# 
# <body>
# 
# <footer>

# Examples:
git commit -m "feat(auth): add user login functionality"
git commit -m "fix(api): resolve null pointer exception in user service"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(utils): extract common validation logic"
```

---

## Remote Operations

### Working with Remotes
```bash
# Fetch changes from remote
git fetch
git fetch origin
git fetch --all

# Pull changes (fetch + merge)
git pull
git pull origin main
git pull --rebase              # Pull with rebase instead of merge

# Push changes
git push
git push origin main
git push -u origin main        # Set upstream and push

# Push all branches
git push --all

# Push tags
git push --tags
git push origin <tag-name>

# Force push (dangerous!)
git push --force
git push --force-with-lease    # Safer force push
```

### Tracking Branches
```bash
# Set upstream branch
git branch --set-upstream-to=origin/main main
git push -u origin main

# Create local branch from remote
git checkout -b <local-branch> origin/<remote-branch>
git switch -c <local-branch> origin/<remote-branch>

# Delete remote branch
git push origin --delete <branch-name>
git push origin :<branch-name>    # Alternative syntax
```

---

## Viewing History

### Log Commands
```bash
# Basic log
git log

# One line per commit
git log --oneline

# Graph view
git log --graph --oneline --all

# Show specific number of commits
git log -n 5
git log -5

# Show commits by author
git log --author="John Doe"

# Show commits in date range
git log --since="2023-01-01" --until="2023-12-31"

# Show commits affecting specific file
git log <file>
git log -p <file>              # Show patches

# Show commits with specific message
git log --grep="bug fix"

# Beautiful log format
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

### Diff Commands
```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged
git diff --cached

# Compare branches
git diff main..feature-branch

# Compare specific commits
git diff <commit1> <commit2>

# Show changes in specific file
git diff <file>

# Word-level diff
git diff --word-diff

# Show only file names that changed
git diff --name-only
```

### Show Command
```bash
# Show specific commit
git show <commit-hash>

# Show specific file at specific commit
git show <commit-hash>:<file>

# Show changes in last commit
git show HEAD

# Show commit with stats
git show --stat <commit-hash>
```

---

## Undoing Changes

### Unstaging and Discarding
```bash
# Unstage file
git reset HEAD <file>
git restore --staged <file>

# Discard changes in working directory
git checkout -- <file>
git restore <file>

# Discard all changes
git checkout .
git restore .

# Clean untracked files
git clean -f                   # Remove untracked files
git clean -fd                  # Remove untracked files and directories
git clean -n                   # Dry run (show what would be deleted)
```

### Reset Commands
```bash
# Soft reset (keep changes in staging)
git reset --soft HEAD~1

# Mixed reset (keep changes in working directory)
git reset HEAD~1
git reset --mixed HEAD~1

# Hard reset (discard all changes)
git reset --hard HEAD~1

# Reset to specific commit
git reset --hard <commit-hash>

# Reset specific file
git reset HEAD <file>
```

### Revert Commands
```bash
# Revert specific commit (creates new commit)
git revert <commit-hash>

# Revert merge commit
git revert -m 1 <merge-commit-hash>

# Revert without committing
git revert --no-commit <commit-hash>
```

---

## Advanced Tricks

### Stashing
```bash
# Stash current changes
git stash
git stash push -m "work in progress"

# List stashes
git stash list

# Apply stash
git stash apply
git stash apply stash@{0}

# Pop stash (apply and remove)
git stash pop

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Stash specific files
git stash push <file1> <file2>

# Stash including untracked files
git stash -u

# Create branch from stash
git stash branch <branch-name> stash@{0}
```

### Cherry-picking
```bash
# Cherry-pick specific commit
git cherry-pick <commit-hash>

# Cherry-pick multiple commits
git cherry-pick <commit1> <commit2>

# Cherry-pick range of commits
git cherry-pick <start-commit>..<end-commit>

# Cherry-pick without committing
git cherry-pick --no-commit <commit-hash>
```

### Bisect (Find bugs)
```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark known good commit
git bisect good <commit-hash>

# Git will checkout middle commit, test and mark:
git bisect good    # if commit is good
git bisect bad     # if commit is bad

# Reset bisect
git bisect reset
```

### Worktrees
```bash
# List worktrees
git worktree list

# Add new worktree
git worktree add <path> <branch>

# Remove worktree
git worktree remove <path>

# Prune worktrees
git worktree prune
```

### Submodules
```bash
# Add submodule
git submodule add <url> <path>

# Initialize submodules
git submodule init

# Update submodules
git submodule update

# Clone with submodules
git clone --recursive <url>

# Update all submodules
git submodule update --remote
```

---

## Git Workflows

### Feature Branch Workflow
```bash
# 1. Create feature branch
git checkout -b feature/new-feature

# 2. Work on feature
git add .
git commit -m "implement new feature"

# 3. Push feature branch
git push -u origin feature/new-feature

# 4. Create pull request (on GitHub/GitLab)

# 5. After review, merge to main
git checkout main
git pull origin main
git merge feature/new-feature
git push origin main

# 6. Delete feature branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

### Gitflow Workflow
```bash
# Initialize gitflow
git flow init

# Start new feature
git flow feature start <feature-name>

# Finish feature
git flow feature finish <feature-name>

# Start release
git flow release start <version>

# Finish release
git flow release finish <version>

# Start hotfix
git flow hotfix start <version>

# Finish hotfix
git flow hotfix finish <version>
```

### Conventional Commits
```bash
# Format: <type>[optional scope]: <description>

# Types:
feat: new feature
fix: bug fix
docs: documentation
style: formatting
refactor: code restructuring
test: adding tests
chore: maintenance

# Examples:
git commit -m "feat(auth): add OAuth2 integration"
git commit -m "fix(api): handle null response in user endpoint"
git commit -m "docs(readme): update installation guide"
```

---

## Configuration

### Global Configuration
```bash
# User information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Default editor
git config --global core.editor "code --wait"

# Default branch name
git config --global init.defaultBranch main

# Line ending handling
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # Mac/Linux

# Color output
git config --global color.ui auto

# Default merge tool
git config --global merge.tool vimdiff

# Push behavior
git config --global push.default simple
```

### Aliases
```bash
# Useful aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# Advanced aliases
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global alias.adog "log --all --decorate --oneline --graph"
git config --global alias.pom "push origin main"
git config --global alias.poh "push origin HEAD"
```

### SSH Configuration
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add SSH key to agent
ssh-add ~/.ssh/id_ed25519

# Test SSH connection
ssh -T git@github.com

# Use SSH for GitHub
git remote set-url origin git@github.com:username/repo.git
```

---

## Troubleshooting

### Common Issues

#### Merge Conflicts
```bash
# When merge conflict occurs:
# 1. Edit conflicted files
# 2. Remove conflict markers (<<<<<<<, =======, >>>>>>>)
# 3. Add resolved files
git add <resolved-file>

# 4. Complete merge
git commit

# Or abort merge
git merge --abort
```

#### Detached HEAD
```bash
# Create branch from detached HEAD
git checkout -b <new-branch-name>

# Or return to main branch
git checkout main
```

#### Accidentally Committed to Wrong Branch
```bash
# Move commits to correct branch
git checkout correct-branch
git cherry-pick <commit-hash>

# Remove commit from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

#### Large File Issues
```bash
# Remove large file from history
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch <large-file>' \
--prune-empty --tag-name-filter cat -- --all

# Or use BFG Repo-Cleaner (faster)
java -jar bfg.jar --delete-files <large-file> .git
```

### Recovery Commands
```bash
# Find lost commits
git reflog

# Recover deleted branch
git checkout -b <branch-name> <commit-hash>

# Recover deleted file
git checkout <commit-hash> -- <file>

# Show all objects
git fsck --lost-found
```

---

## Git Hooks

### Common Hooks
```bash
# Pre-commit hook (run tests before commit)
#!/bin/sh
# .git/hooks/pre-commit
npm test
if [ $? -ne 0 ]; then
  echo "Tests failed, commit aborted"
  exit 1
fi

# Pre-push hook (run linting before push)
#!/bin/sh
# .git/hooks/pre-push
npm run lint
if [ $? -ne 0 ]; then
  echo "Linting failed, push aborted"
  exit 1
fi

# Commit message hook (enforce format)
#!/bin/sh
# .git/hooks/commit-msg
if ! grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+" "$1"; then
  echo "Invalid commit message format"
  exit 1
fi
```

---

## Performance Tips

### Speed Up Git
```bash
# Enable parallel index preload
git config --global core.preloadindex true

# Enable file system monitor
git config --global core.fsmonitor true

# Use partial clone for large repos
git clone --filter=blob:none <url>

# Shallow clone (limited history)
git clone --depth 1 <url>

# Maintenance commands
git gc                         # Garbage collection
git repack -ad                # Repack objects
git prune                     # Remove unreachable objects
```

### Large Repository Handling
```bash
# Sparse checkout (only specific directories)
git config core.sparseCheckout true
echo "src/" > .git/info/sparse-checkout
git read-tree -m -u HEAD

# LFS for large files
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

---

## Useful One-liners

```bash
# Show files changed in last commit
git diff-tree --no-commit-id --name-only -r HEAD

# Count commits by author
git shortlog -sn

# Show branch creation date
git for-each-ref --format='%(committerdate) %09 %(refname)' | sort -k5n -k2M -k3n -k4n

# Find commits that added or removed specific text
git log -S "search_term" --oneline

# Show commits not yet merged to main
git log main..HEAD --oneline

# Create patch file
git format-patch -1 <commit-hash>

# Apply patch
git apply <patch-file>

# Show file at specific commit
git show <commit>:<file>

# Blame with ignore whitespace
git blame -w <file>

# Show commits that touched specific line
git log -L <start>,<end>:<file>

# Dry run merge
git merge --no-commit --no-ff <branch>
git merge --abort

# Show remote branches that are merged
git branch -r --merged

# Delete all merged branches
git branch --merged | grep -v "\*\|main\|master" | xargs -n 1 git branch -d
```

---

## Git Best Practices

### Commit Guidelines
- Write clear, descriptive commit messages
- Make atomic commits (one logical change per commit)
- Use present tense ("Add feature" not "Added feature")
- Keep commits small and focused
- Test before committing

### Branch Naming
```bash
# Good branch names:
feature/user-authentication
bugfix/login-error
hotfix/security-patch
release/v1.2.0
```

### Repository Structure
```
.gitignore          # Ignore patterns
README.md           # Project documentation
CONTRIBUTING.md     # Contribution guidelines
LICENSE            # License information
.github/           # GitHub specific files
  workflows/       # GitHub Actions
  ISSUE_TEMPLATE/  # Issue templates
  PULL_REQUEST_TEMPLATE.md
```

### Security
- Never commit sensitive data (passwords, API keys)
- Use .gitignore for sensitive files
- Regularly audit repository for secrets
- Use signed commits for important repositories

```bash
# Enable commit signing
git config --global commit.gpgsign true
git config --global user.signingkey <key-id>
```

---

This cheatsheet covers the most important Git commands and workflows. Keep it handy for quick reference during development!