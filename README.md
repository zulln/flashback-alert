# flashback-alert
Send a push notification to your phone when a new Flashback-thread is created containing a specific keyword

keywords[] is _not_ case sensitive and should contain the keywords you are interested in.

token and user under payload comes from pushover.net. You have to register an account and download the app for it to work probably.

The script is recommended to run as a cronjob every 30 minutes, but whatever time you prefer probably works. The error handling is not really the greatest, so if the script fail to either connect to Flashback or Pushover it will simply die and not try again.

pushed.txt will contain every thread id that has been pushed. The first line is the first push. This is to prevent multiple pushes for the same thread.