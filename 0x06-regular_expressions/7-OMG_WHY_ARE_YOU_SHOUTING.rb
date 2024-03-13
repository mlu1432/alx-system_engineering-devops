#!/usr/bin/env ruby
# This script takes an argument from the command line and
# prints it if it contains only uppercase letters
puts ARGV[0].scan(/[A-Z]*/).join