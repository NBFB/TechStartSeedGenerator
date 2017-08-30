import csv

##### TODOS
# doesn't rewrite a csv

##### Config

# Max number of projects per school
MAX_PROJECTS = 25;

#Minimum number of projects per school
MIN_PROJECTS = 5

# Collection of entries
project_data = []


#### Generate test entries and append them to 'project data'

# Variable to count entries.
entry_index = 0;

# 400 schools
for schoolIndex in range(1,400):

# 5 - 25 projects per school
	for projectNum in range(5,25):
		entry_index = entry_index + 1;
		project_entry = ["githubHandle_" + str(entry_index), "projectURL_" + str(entry_index), "schoolName_"+ str(schoolIndex)]
		project_data.append(project_entry)

# Write the contents of 'project_data' to csv file
with open("test_projectsubmit_data.csv", "w") as csv_file:
	csv_app = csv.writer(csv_file)
	csv_app.writerows(project_data)