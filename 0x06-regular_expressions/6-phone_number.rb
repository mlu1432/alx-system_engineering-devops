#!/usr/bin/env ruby
# This script takes an argument from the command line and
#+ prints it if it is a valid 10-digit number
puts ARGV[0].scan(/^\d{10,10}$/).join
