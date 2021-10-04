Intro to Using APIs

This repository is an introductory assignment for HHA 507 for APIs

The lyrics.ovh API is a simple API used to retrieve lyrics of a song.

This is the URL https://lyricsovh.docs.apiary.io/# for the API.

This the basic example GET request 'https://api.lyrics.ovh/v1/artist/title'.

Artist is a string that is the name of the artist.
Title is a string that is the title of the song.

For both artist and title the capitalization does not matter.
It is important to have correct spacing for artist names and song titles.
(e.g. 'https​://api.lyrics.ovh/v1/iMaGIne dRAgONs/WHaTEVeR it tAKeS' would work, but not
'https​://api.lyrics.ovh/v1/ImagineDragons/Whateverittakes')
Also, the API can pull songs from languages other than English. 
The other languages tested in this assignment are Japanese, Chinese, Korean, and Spanish.

[Important Note: The examples provided above will not work if copied and pasted. 
This is due to the zero width space added to prevent any auto-generated hyperlinks.]

All the songs chosen in this assignment were ones that worked and successfully returned 
information. There were several other songs in languages other than English that did not work 
and therefore were not included in the final file.