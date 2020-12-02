# Initiative Tracker

Initiative Tracker is a web app designed to solve a very specific problem during an online Dungeons and Dragons game: the length of time it takes to sort combat initiative order.

The story:  During the covid-19 quarantine, I reconnected with a gaming group from college/high school.
There was 11 of us online each week.  With that number of people coordinating in a video-conference-style game session, it could take 5-10 minutes for the players to roll, and the DM to document and sort initiative order.
We are all old now, and don't have *that* much time to play a table-top RPG, so 5-10 minutes was significant.

This project is meant to solve the question:
What if everyone could log in to a site, input their initiative number, and the site would sort and keep track of it for as long as you wanted?
Easy peasy lemon squeezy.

Initiative Tracker:
- Is built in Python with Django 2.2.
- Uses Django User authentication.
- Uses Bootstrap for responsiveness and Javascript Widgets like modals.
  - (If Initiative Tracker had any chance of being useful, it needed to be designed to be viewed on a phone.)
- Has some custom CSS for an old-school / "antique" aesthetic.
- Uses AJAX for quick, unobtrusive table-sorting.
