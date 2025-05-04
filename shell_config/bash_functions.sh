#!/bin/bash

# refer to catch_up function for arguements
function validate_catch_up() {
    if [ -z "$1" ]; then
        echo "Missing branch_name_prefix argument 1"
        return 1
    fi
    if [ -z "$2" ]; then
        echo "Missing remote_branch_name argument 2"
        return 1
    fi
    if [ -z "$3" ]; then
        echo "Missing start_number_suffix argument 3"
        return 1
    fi
    if [ -z "$4" ]; then
        echo "Missing final_branch_number argument 4"
        return 1
    fi
    return 0

}

#######################################
# Pulls dev branch from remote repository
# and catches up branch_name locally and
# on remote to origin/dev branch
# Example:
#   git branch -b myfeature_0
#   git branch -b myfeature_1
#   git branch -b myfeature_2
#   catch_up myfeature_ myfeature_0 2
#   catches up branches myfeature_3, myfeature_4, myfeature_5
#   catch_up myfeature_ myfeature_3 5
#
# Globals:
#   dev = dev branch exists in origin and locally
#   git = git installed
#   origin = remote git url
#
# Arguments:
#   branch_name_prefix string prefix for a branch name
#   remote_branch_name string branch in remote
#       that you need to catch up to
#   start_number_suffix integer suffix to start from
#   final_branch_number integer number of branch to finish
#       catching up to, inclusive of the branch on this number
#######################################
function catch_up(){
    validate_catch_up "$@"

    if [ $? -ne 0 ]; then
        return 1
    fi
    git fetch origin
    git checkout dev
    git merge origin/dev
    git checkout "$10"
    git merge dev
    for ((branch_num=1; branch_num<=$2; branch_num++))
        do
            git checkout "$1$branch_num"
            git merge "$((branch_num - 1))" --no-edit
            git push "$1$branch_num"
        done

}


#######################################
# Description: Branch workflow automation function that creates and switches to a new branch
#              while ensuring the local master branch is up to date with the remote.
# Usage: xb <branch-name>
# Arguments:
#   branch-name: The name of the branch to create or checkout
# Example:
#   xb feature/new-feature
#######################################
function xb() {
    if [ $# -eq 0 ]; then
        echo "Error: Please provide a branch name as an argument"
        echo "Usage: xb <branch-name>"
        return 1
    fi

    local BRANCH_NAME=$1

    # Fetch all remote changes
    echo "Fetching remote changes..."
    git fetch --all

    echo "Switching to master branch..."
    git checkout master

    echo "Deleting all branches except master..."
    git branch | grep -v "master" | xargs git branch -D

    # Pull latest changes from remote master
    echo "Pulling latest changes from remote master..."
    git pull origin master

    git checkout -b "$BRANCH_NAME"
}

#######################################
# Creates a commit with the given message and creates a pull request
# Globals:
#   git = git installed
#   gh = GitHub CLI installed
#
# Invariants:
#   The current branch is dev
#   The remote is origin
#   The remote dev branch is up to date with origin/dev
#   Logged in to github via cli
#
# Arguments:
#   commit_message: The message to use for the commit and PR title
#######################################
function xr() {
    if [ -z "$1" ]; then
        echo "Missing commit message argument"
        return 1
    fi

    # Check if there are any changes in the working directory
    if ! git diff-index --quiet HEAD --; then
        git add -A
        git commit -m "$1"
    fi

    git push origin dev

    echo "pushed to remote"

    gh pr create --title "$1" \
        --body "Automated PR creation" \
        --head dev \
        --base master

    echo "created PR"
    echo "----------------------"
    echo "deployment successful"
}
