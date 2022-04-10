##################################
#Documentation on where to install:
#https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-5.1#the-profile-files
#
#
#################################



foreach($alias_row in $alias_list){
    Function global:: "$alias_row.alias_name" {
        $alias_row.alias_value
    }

}

$alias_list =    "shell_config\alias_commands.csv" -Header "alias_name", "alias_value" 
for ($counter = 1 ; $counter -le 10 ; $counter++){  
    echo $alias_list[$counter].$alias_name
    
    # Function "$alias_list[$counter].alias_name" {
    #     $alias_list[$counter].alias_value

    # }
}