#######################################
# Pulls dev branch from remote repository
# and catches up branch_name locally and remote to dev branch
#
# Globals:
#   dev = dev branch exists in origin and locally
#   git = git installed
#   origin = remote git url
#
# Arguments:
#   branch_name string prefix for a branch name
#   branch_num integer number of feature branches prefixed 
#       with branch_num
#######################################
function catch_up(){
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