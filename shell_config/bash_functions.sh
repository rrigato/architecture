
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