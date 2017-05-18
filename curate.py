from curator.platforms import *
from curator import *

output.prep_output()

print("Getting submissions...")

submissions = {
    dmoj.platform_name(): dmoj.fetch()
}

print("Writing to folder...")

for platform, items in submissions.items():
    output.write_submissions(items)

readme.write_readme(submissions)
