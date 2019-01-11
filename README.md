# Car-Poolers
 This is an application that allows users to share a ride from one place to another. As a user, I would like to log on to the website, find a driver near me with space in his/her car going the same direction as me and book a space.
 # Author
 Vinny Otach
 # Application
 <img src="/home/moringaschool/Pictures/Screenshot from 2019-01-11 11-46-16.png">
# Setup and Installation
<ul>
<li>
Clone the Repo adding the following command: git clone https://github.com/vinnyotach7/Car-Poolers.git</li>
<li>Activate virtual environment using python3.6 as default handler by running python3.6 -m venv virtual then enter the virtual environment using source virtual/bin/activate.</li>
<li>Download the latest version of pip in the virtual environment: $ curl https://bootstrap.pypa.io/get-pip.py | python.</li>
<li>Install all application dependancies pip install -r requirements.txt</li>
<li>Create the Database -On the terminal,run psql</li>
<li>Create a .env file and add the following:
<ul>
<li>SECRET_KEY = <Secret_key></li>
<li>DB_NAME = awards</li>
<li>DB_USER = <Username></li>
<li>DB_PASSWORD = your db password</li>
<li>DEBUG = True</li>
</ul>
<li>Run Initial Migration python3.6 manage.py makemigrations <name of the app> python3.6 manage.py migrate</li>
<li>Run the app python3.6 manage.py runserver Open terminal on localhost:8000</li>
</ul>

# User Stories
As a passenger i would like to:
<ul>
<li>Sign in to the application to start using.</li>
<li>Set up a profile about me and a general location.</li>
<li>Find a list of drivers near me.</li>
<li>View a map with the location of all pickup points.</li>
<li>Review a driver and also be reviewed by the driver.</li>
<li>View the current space left in a driver’s car and get to book It.</li>
</ul>
As a driver i would like to:
<ul>
<li>Sign up as a driver to use the application</li>
<li>Set up my drivers profile.</li>
<li>View a map with the location of all pickup points.</li>
<li>View all the requests for a ride.</li>
<li>Review passengers coming on to your application.</li>
</ul>

# Technologies Used
<ul>
<li>python3.6.7</li>
<li>HTML5</li>
<li>CSS3</li>
<li>Bootstrap4</li>
<li>Postgresql</li>
<li>Visual Studio Code text editor</li>
</ul>

# License
MIT License Copyright(c)2018 Vinny Otach