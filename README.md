# chuck-norris-fact-notifier
A cool snippet to display a customized Chuck Norris fact into a notification on MacOS and Unix systems.

## How does it work?

The script *cnf.py* fetches a random fact about Chuck Norris from the [*Chuck Norris Facts API*](http://www.icndb.com/api/).

One can trigger it manually, assuming your system is up with python 3:

```sh
$ python cnf.py
```

You can eventually customize the *config* dictionary to become the hero of the fact! Just fill the values associated with the keys *firstName* and *lastName*. For example, open the file *cnf.py* and update with these elements:

```py
config = {
  'url': 'http://api.icndb.com/jokes/random',
  'key': 'joke',
  'firstName': 'Emmanuel',
  'lastName': 'Macron'
}
```

Another way to use it is to pass on the triggering to a cron task. For example, to display a Chuck Norris fact each hour, install the following task in your crontab:
```sh
@hourly /usr/local/bin/cnf.sh
```
