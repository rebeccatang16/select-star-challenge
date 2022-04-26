### Select Star Full-Stack Challenge

You can find my solution to the first part of the challenge in `group_strings`. Its usage is
`python group_strings.py path-to-csv destination-json-path`

You can find my attempt to the second part of the challenge in folder_view. Note that this solution does not work, as I was learning DRF on the fly and could not get a working solution within the time I alotted for myself.

I added and tested a Dockerfile that would build a proper image for the app, if it worked, as well as a simple bash build script to automate building and tagging the image with the commit hash and `latest`. These files can be found at root level.