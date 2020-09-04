Kagojer Nouka
=============
Kagojer Nouka is a complete solution for local authorities to build
relationship with their constituents and help them in any problem
real time. This project is being developed for 
[tracthon](https://traction.robu-lab.org/) by team Kagojer Nouka. 
You can visit the site here.
* [Front End Vue Application](https://kagojer-nouka-web.herokuapp.com/dashboard)
* [Back End Django REST Application](https://kagojer-nouka.herokuapp.com/dashboard)

Problem Statement
=================
In order to stop the spread of rumors from any platform such as social media,
you have to make a platform that can evaluate information in terms of authentic
source and help people to not get flustered when a fake news spread through different medias.

Solution Abstract
=================
Title
-----
A social media focused platform to combat fake news using big data and natural language processing.

Abstract
--------
With the rise of the internet, people are getting and sharing more and more news on social media.
Due to shock value, fake news spread rapidly on social media. Available fact checking solutions require
higher technical expertise than what most of the people have. On the contrary, experts can’t get sufficient
data in a central place. So they can neither track fake news nor provide the public with proper information
fast and effectively. Thus fake news stays unchallenged and reaches millions rapidly.

So we need an accessible, intuitive, easy to use platform having a fast response time. As fake news
spreads mostly through social media, we should primarily focus on social media alongside the rest of
the web. We also need to make information available in a central database to analyse big-data to
detect and show useful information graphically. Then the authorities can understand kinds of fake
news spreading and decide how to combat them in real time.

Our proposed platform collects data from social media, blogs, forums and news websites using public
API and web-crawling. Collected data is then fed to NLP models to identify trends, change of public
perception, and long-term impacts to help experts decide combat-strategy and conduct long term research.
It allows people to verify news using Facebook Messenger and WhatsApp chatbot, mobile and web
applications and manages targeted awareness campaigns.

The problem is so prevalent in Bangladesh that the government is actively looking for a solution.
Multiple government organizations, like Startup Bangladesh, are looking for potential solutions.
Opportunities like this make us optimistic about being able to turn our solution into a sustainable
business product with a steady demand from authorities at home and abroad.

Finals
------
The tight integration of our platform with social media allows us to tackle the problem at its root.
We’ll be able to provide authentic news to all demographics and mitigate social unrest caused by fake news.

Team Members
============
1. [Tahmeed Tareq](https://github.com/tahmeed156)
2. [Priyeta Saha](https://github.com/prism97)
3. [Khondokar Ashikur Rahman](https://github.com/ashiqursuperfly)
4. [Md. Zunaed Karim](https://github.com/ZunaedSifat/)

Push code to heroku server
==========================
* For backend server, execute `git subtree push --prefix backend heroku-backend master` from root folder of the repository
* To force push to backend server, execute ```git push heroku-backend `git subtree split --prefix backend master`:master --force```
