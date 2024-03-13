#!/usr/bin/env ruby

# Define a method that checks if the input has the word "School" in it
def match_school(argument)
    if argument.include?("school")
        puts "Match found: #{argument}"
    else
        puts
    end
end

# Check if there is exactly one argument given from the command line
if ARGV.length == 1
    argument = ARGV[0]
    amtch_school(argument)
    else
        puts "Usage: ./script.rb <text_to_search>"
    end
