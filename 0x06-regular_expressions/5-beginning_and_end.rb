#!/usr/bin/env ruby

# This script takes a command line argument and scans it for a string that consists of exactly 10 digits at the beginning and end.

puts ARGV[0].scan(/^\d{10}$/).join