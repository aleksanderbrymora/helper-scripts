import os
import urllib.request

answer = input('Do you want to include jQuery? [y/n]: ')[0].lower()
jquery = True if answer == 'y' else False
answer = input('Do you want to include Water CSS? [y/n]: ')[0].lower()
water_css = True if answer == 'y' else False

project_name = input('What\'s the name of the file?: ')

path = project_name

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    # Download jQuery
    if jquery:
        os.mkdir(f"{path}/js")
        urllib.request.urlretrieve('https://code.jquery.com/jquery-3.4.1.min.js', f"{path}/js/jquery.min.js")
        print('Added jQuery')
    # Create a readme file
    with open(f"{path}/README.md", "w+") as f:
        f.writelines(f"# {project_name}")
        f.close()
        print(f"Created README.md for {project_name}")
    with open(f"{path}/style.css", "w+") as f:
        f.writelines("""* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}""")
        f.close()
        print("Created css")
    # Create index.html
    with open(f"{path}/index.html", "w+") as f:
        f.writelines(
            f"""<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {"<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css'>" if water_css else ''} 
        <link rel="stylesheet" href="style.css">
		<title>{project_name}</title>
	</head>
	<body>
        {"<script src='js/jquery.min.js'></script>" if jquery else ''}
		<script src="js/main.js"></script>
	</body>
</html>"""
        )
    # Create main.js
    open(f'{path}/js/main.js', 'a').close()
    print('Done!\nRunning live server and opening in VS Code')
    os.system(f"code {path}")
    os.system(f"live-server {path}")