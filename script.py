import sys
import re
import os


def generate_svg(svg_file_name, svg_file, filename, name):
    command = 'cp %s.svg %s.svg' % (svg_file_name, filename)
    os.system(command)

    new_certificate = open(filename + ".svg", 'r+')
    new_certificate.write(re.sub("__NAME__", name, svg_file))
    new_certificate.write()

def generate_pdf(filename, new_certis_path):
    print("    generating pdf certificate")
    command = 'inkscape %s.svg --export-pdf=%s/%s.pdf' % (filename, new_certis_path, filename)
    os.system(command)
    print("    removing svg file")
    remover = 'rm %s.svg' % (filename)
    os.system(remover)


def genrate_certificate(svg_file_name, svg_file, name_list_file, new_certis_path):

    list_names = open(name_list_file)

    if not os.path.exists(new_certis_path):
        os.makedirs(new_certis_path)
    
    for name in list_names:
        name = name.rstrip("\n")
        filename = name.replace(" ","_")
        print(filename)

        # genrate SVG for each name
        generate_svg(svg_file_name, svg_file, filename, name)
        
        #generate pdf after writing SVG
        generate_pdf(filename, new_certis_path)

if __name__ == '__main__':

    SVG_FILE_NAME = sys.argv[1] 
    NAME_LIST_FILE = sys.argv[2] # name of CSV file where participant data is stored
    NEW_CERTIS_PATH = sys.argv[3] # path where new certis will be stored

    SVG_FILE = open(SVG_FILE_NAME +".svg").read()

    genrate_certificate(SVG_FILE_NAME, SVG_FILE, NAME_LIST_FILE, NEW_CERTIS_PATH)

