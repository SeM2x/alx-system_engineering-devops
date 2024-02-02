#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(.{1,12})\].*to:(.{1,12})\].*flags:(.{4,14})\]/).join(',')
