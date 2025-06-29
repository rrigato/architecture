#!/bin/bash

#######################################
# Description: Intelligently remote origin dev or develop branch into current branch
# Usage: g_j
# Globals:
#   git = git installed
#   origin = remote git url
#
# Arguments:
#   None
#
# Example:
#   g_j
#   # Merges current branch into dev if dev exists, otherwise into develop
#######################################
function g_j() {
    # Run in a subshell to prevent crashing invoking shell session
    (
        set -e

        local CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

        # Fetch latest from remote to check available branches
        git fetch origin

        # Check if dev branch exists in remote origin
        if git ls-remote --heads origin dev | grep -q dev; then
            local TARGET_BRANCH="dev"
        # Check if develop branch exists in remote origin
        elif git ls-remote --heads origin develop | grep -q develop; then
            local TARGET_BRANCH="develop"
        else
            echo "Error: Neither dev nor develop branch found in remote origin"
            return 1
        fi

        git fetch origin
        git fetch origin "$TARGET_BRANCH":"$TARGET_BRANCH"

        echo "merged origin $TARGET_BRANCH into local"

    )
}




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

# refer to xr function for arguments
function validate_xr() {
    if [ -z "$1" ]; then
        echo "Missing commit message argument 1"
        return 1
    fi
    if [ -z "$2" ]; then
        echo "Missing target branch argument 2"
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
    #run in a subshell to prevent crashing invoking shell session
    (
        set -e
        if [ $# -eq 0 ]; then
            echo "Error: Please provide a branch name as an argument"
            echo "Usage: xb <branch-name>"
            return 1
        fi
        local BRANCH_NAME=$1
        local DEFAULT_BRANCH=$(
            git symbolic-ref refs/remotes/origin/HEAD \
            | sed 's@^refs/remotes/origin/@@'
        )

        if [ -z "$DEFAULT_BRANCH" ]; then
            echo "Error: Could not determine default branch"
            return 1
        fi

    git fetch --all

        # If not on the default branch merge default branch into local default branch
        if [ "$(git rev-parse --abbrev-ref HEAD)" != "$DEFAULT_BRANCH" ]; then
            echo "Merging $DEFAULT_BRANCH into local $DEFAULT_BRANCH..."
            git fetch origin "$DEFAULT_BRANCH":"$DEFAULT_BRANCH"
        fi

    git checkout "$DEFAULT_BRANCH"

        echo "Deleting all branches except $DEFAULT_BRANCH..."
        git branch | grep -v "$DEFAULT_BRANCH" | xargs git branch -D


        git checkout -b "$BRANCH_NAME"
    )
}

#######################################
# Creates a commit with the given message
# and creates a pull request in the remote repository
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
    validate_xr "$@"

    if [ $? -ne 0 ]; then
        return 1
    fi

    local CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    local TARGET_BRANCH=$2

    # Check if there are any changes in the working directory
    if ! git diff-index --quiet HEAD --; then
        git add -A .
        git commit -m "$1"
    fi

    git push origin "$CURRENT_BRANCH"

    echo "pushed to remote"

    gh pr create --title "$1" \
        --body "Automated PR creation" \
        --head "$CURRENT_BRANCH" \
        --base "$TARGET_BRANCH"

    echo "created PR"
    echo "----------------------"
    echo "deployment successful"
}
