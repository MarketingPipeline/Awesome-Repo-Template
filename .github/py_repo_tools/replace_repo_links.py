# Define the filename here you want to replace content in
FileName = "README.md"

Text_To_Replace = "MarketingPip/Awesome-Repo-Template"

Text_To_Replace_With = "MarketingPip/Awesome-Repo-Template"

# Open the File
with open(FileName, 'r') as f:
    # Read the file contents
    contents = f.read()
    # Replace the file contents
    contents = contents.replace(Text_To_Replace, Text_To_Replace_With)

# Write the file out    
with open(FileName, 'w') as f:
    # Write the updated contents
    f.write(contents)  
