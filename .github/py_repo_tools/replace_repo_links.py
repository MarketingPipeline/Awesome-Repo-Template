# Define the filename here you want to replace content in
FileName = "README.md"

Text_To_Replace = "MarketingPip/Awesome-Repo-Template"

Text_To_Replace_With = "MarketingPip/Awesome-Repo-Template"


with open(FileName, 'r') as f:
    contents = f.read()
    # Define the first line where your content will be replaced / added 
    contents = contents.replace('Media-Element.js/media-element.min.js', 'version/1.0.1/src/media-elements.js')
    
with open(FileName, 'w') as f:
    f.write(contents)  
