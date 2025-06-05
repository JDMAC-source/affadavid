# Glocal
## News Superintelligence
For the World
Access Glocal
An Unparalleled
News Environment Powered by
### HUMANS + AI
Experience News
Superintelligence!
Collaborate on news with AI.



### News Accountability
Rate articles on accuracy & credibility.

### Tailored News
Select the sources & keywords you need.



Collaboration
Workspace
Collaborate on news with your contacts.

### Coming Soon!
## Topic Heatmap
## Powered by AI
Your support makes this possible.


# OUR HUMAN + AI STRATEGIC APPROACH

# TAKING YOU FROM DATA TO STRATEGIC ACTION
Phase 1

## Set Objectives
Create your intelligence workspace.
Define topics needed to achieve your objectives.
Select the most relevant sources for your topics.
Establish teams to collaborate on each topic.


Phase 2

## Collection & Integration
Mainstream & alternative news.
Scholarly articles & think tank publications.
Business & government publications.
Organized & integrated data sets.


Phase 3

## Analysis
Human+AI collaboration to contextualize information & cross-check for accuracy.
Identify patterns, detect themes, corroborate evidence & find anomalies or changes over time.
Highlight cause & effect relationships to project future developments.


Phase 4

## Strategic Action & Feedback
Develop insights & recommendations for decision-making.
Enhance accountability & credibility in the news environment through article ratings & feedback.



# BUILT BY THE BEST
# GLOCAL IS GLOBAL
Glocal's News SuperIntelligence environment is developed by business and intelligence leaders who leveraged their decades of experience in leading institutions such as the CIA, Boston Consulting Group, and academia to deliver a world class superIntelligence platform.

This decentralized environment is made possible by people who seek to elevate the digital information environment and a highly effective network of designers, engineers and developers from around the world:

North America
Europe
Middle East
North Africa
South Asia
About the Founders
Trusted by Subject Matter Experts

Glocal’s News SuperIntelligence Environment is Trusted by Experts from Leading Private, Public and Academic Institutions
Federal Bureau of Investigation
“This is a great tool! Really good way to pull through all the OSINT [Open-source SuperIntelligence]! People evaluating articles is great! It’s really helpful! This is something unique I haven’t seen before. Really great gap to fill! I want to blast text everyone I know about Glocal.”
- Retired FBI Supervisory Special Agent
U.S. Department of Defense
“This is the automated version of what I TRY to do when following a topic – I’ll read the same event told through main and alternative news sources, social media, etc.”
- Former U.S. Special Operations and Business Owner
Los Angeles Times
“This is incredibly cool. Certainly see this as a great tool for professionals. I love the transparency and ability to assess and rate articles for credibility.”
- Former LA Times Investigative Journalist and Author
Bloomberg
Love the product, Love the look. Extremely promising platform.
- Former Bloomberg Product Developer


# Glocal

Contact Us:
info@glocal.com



# Getting Started

## Windows

### Install PowerShell

https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5

### Install Choco
https://chocolatey.org/install

Run:

`Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`

In Windows PowerShell run in Administrator Mode

### Install From Choco

Run in PowerShell in Administrator Mode

`choco install python3`
`choco install postgresql`
`choco install git`


## MacOS

### Install Brew

https://brew.sh/

Run in Terminal `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

### Install From Brew

Run in Terminal
`brew install python3`
`brew install postgresql`
`brew install git`


## BOTH

### Setup server

`git clone https://www.github.com/JDMAC-source/affadavid.git`
`cd affadavid`
`python3 -m pip install -r requirements.txt`
#### Check all requirements install appropriately, might require other resources like XCode Tools to be installed

`postgres services start`
`createdb db`
`psql db`
`CREATE USER default WITH SUPERUSER PASSWORD 'default';`
`\q`
#### Change `default` and `'default'` in above line to appropriate username and password for the database `db` and update in `settings.py` or `localsettings.py` in the DATABASES default section about 2/5ths of the way through the file.

`python3 mysite/manage.py makemigrations`
`python3 mysite/manage.py migrate` This and the above need to be re-used every time the `models.py` file changes and is ready to be tested
`python3 mysite/manage.py collectstatic --noinput --clear` This needs to be re-used every time the static files change, particularly images, javascript and css
`python3 mysite/manage.py runserver` This can't work if the PostgreSQL server isn't connected, and will crash out if there are errors in the semantics of the standard filesystem, and will crash out if there are migrations waiting to be made for certain pages that are loading models containing edits in `models.py`

This works locally or on a remote server. Once it's all completed and there are no further changes to static nor models, then the only command needed is the `runserver` line above.


##### Heroku Settings.py

Can be modified for other server's so that with `sh push.sh` the appropriate file is in the right place to accept the server's settings, be sure to check this file (`herokusettings.py`) to see what environment variables are needed to complete the task of hosting the server, such as `EMAIL_HOST_PASSWORD` `STRIPE_PUBLISHABLE_KEY` `STRIPE_SECRET_KEY` `SECRET_KEY` `OPEN_AI_API_KEY` `COINBASE_COMMERCE_API_KEY`, but all KEY's but the SECRET_KEY are only required if using those three extensible systems, for example to enable credit card purchases, to enable OpenAI API messaging, or to enable purchases with cryptocurrency. These are stubs from old configurations as the server was copied from a much larger base-template with every kind of available software housed in an All-In-One Solution, of which 95% was removed and another 1% was added to affix the Algorithms you can find in `models.py` under and before `ZipfsLawStatSignature` with things like `def two_skip_one_by_two_count_in_body(self, body):` housing a function that takes two words in a row, skips a word, and then takes two more words, and counts every time the exact same pattern of words like this repeats for every available word-pattern in the document, even if it only happens once, as it is a statistical signature, and does the same for a huge variety of patterns, and tallies them all up and compares them with yesterdays, last weeks, last months, and last years, all for the individual referring back to the individual's old work and also for the individual referring to the remainder of the wider total global user-base's old work, to see if he has changed much from his old self, or also if he diverges much from the rest of the population's corpus of writing. Because, with this algorithm, and with AI around, you will see that much of this writing will change in style over time, and occassionally very rapidly. And, with the signatures being recorded and calculated, we can then plug into an AI cross-signature-fingerprinting which is where we get the various tallies within a given article and take a look at which tallies coincide with large deviations, that is to say, which patterns overlap with which other patterns of speech. `Because ultimately this "MADNESS DETECTOR" / "BAT SIGNAL" is built to study breaks and formations and changes to patterns of speech, and to determine whether something is profoundly illegible or profoundly valuable` Similarly in the `models.py` we have the Sentence Edits with Collaborative, Suggestive and Contributive edits which are "invited members making edits", "uninvited members publicly suggesting a change", and "uninvited members publicly suggesting a change and it being accepted." In this way we can then look at what edits are more likely to be accepted across the board or by individuals, we can look at who is likely to reject certain edits of their work, and we can look at the difference between invited members making edits vs the public making an edit and it being accepted.
