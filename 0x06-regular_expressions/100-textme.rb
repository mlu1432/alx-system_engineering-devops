#!/usr/bin/env ruby
# This script takes an argument from the command line and
# prints it if it matches a pattern of email headers
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")