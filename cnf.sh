export PATH=/usr/local/bin:$PATH
dir=$(pwd)
terminal-notifier -appIcon $dir"/icon.png" -title "Chuck Norris !" -timeout 10 -message "$(python $dir/cnf.py)" -sound "Purr"
