#This easy script is to enumerate users on a windows machine through powershell
#Can be useful to dump very basic information about the local users of a system.

Get-LocalUser | Select -ExpandProperty Name > users.txt #With the Select and the flag -ExpandProperty we are only selecting the property Name(usernames) and removing the column name that 
#usually appears on top. We are redirecting the result to a file.
$files = Get-Content users.txt #The archive with the local users #We iterate through each user of the previous file and apply the command net user username. We are appending the results
#to another file
forEach ($user in $files) {
	net user $user >> file_name.txt
}

