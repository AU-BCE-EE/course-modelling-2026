# course-modelling-2026

Repo for the website for the 2026 AU BCE course "Modelling".
The course website itself, with the schedule, class materials, and course info, is here:
**<https://au-bce-ee.github.io/course-modelling-2026/>**
This repo is public only so the website can be public; it is not intended to be a public front end for the course.
So to students: visit and bookmark <https://au-bce-ee.github.io/course-modelling-2026/>, *not* this repo page. 

# For instructors
This repo is the source for that site (`schedule.csv`, `classes/`, `demos/`) plus the Quarto
project config that builds it (`_quarto.yml`, rendered to `docs/`, served via GitHub Pages).

## Workflow

1. Edit only those files at the repo root directly. Most likely only `schedule.csv` will need regular edits, but `_mathjax-macros.html` (for units), `course_info.qmd` (for what shows up on the website under "Modelling 2026"), `index.qmd` (to create "Schedule" on the course website), `_quarto.yml` (to change website layout etc.), and `README.md` (this file) could need some edits at some point. *But do not directly change files in the `classes`, `docs`, `drawings`, or `_freeze` directories.* 
2. Instead, transfer class files from the private repo with the `release.sh` shell script in that repo. See that repo for details.
3. Then run `quarto render`.
4. Finally, commit and push to update the course website. Check afterwards.
