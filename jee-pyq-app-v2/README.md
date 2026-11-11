# JEE PYQ CBT Practice  (made by DIVYANSH)

Static website - no Python packages, no build step.

## Repository structure
```
your-repo/
|-- index.html                 the whole app
|-- README.md
|-- server.py                  only for hosts that ask for a start command
|-- requirements.txt
|-- lib/
|   |-- pdf.min.mjs            PDF reader (keep this folder)
|   `-- pdf.worker.min.mjs
`-- pdfs/
    |-- mathematics.pdf        your Maths PDF (rename it to this)
    |-- chemistry.pdf          your Chemistry PDF (rename it to this)
    `-- physics.pdf            optional, add when you have it
```
The site loads everything in `pdfs/` automatically. To add another book later, add its
path to `BOOK_FILES` near the bottom of `index.html`.

## Deploy
Commit the folder to GitHub and deploy the latest commit. Open the site over https.
Tip: keep the repository PRIVATE - the PDFs are not yours to share publicly.

## Using it
1. Open the site; your PDFs load by themselves.
2. (Returning) load your progress file - it also holds your folders and notes.
3. Pick chapters / question numbers / pages / saved folders, then start.
4. During a test or in the results review, the (+) button saves a question into a folder.
5. After every session click "Download progress file" and keep it safe.
