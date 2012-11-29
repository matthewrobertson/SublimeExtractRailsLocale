require 'yaml'

file_path = ARGV[0]
key       = ARGV[1]
value     = ARGV[2]


if File.exists?(file_path)
  content = YAML.load_file(file_path)
else
  content = {}
end

hash = content
key.split('.')[0...-1].each do |step|
  hash[step] = {} unless hash[step]
  hash = hash[step]
end
hash[key.split('.')[-1]] = value

puts content

File.open(file_path,'w') do|file|
  file.puts content.to_yaml
end